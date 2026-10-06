// Tanda tangan digital RSA: penandatanganan, verifikasi, dan uji pemalsuan.
// Bab 16, melengkapi Aktivitas 16.1.
//
// Alur yang dipakai sama seperti pada Bab 16: pesan di-hash lebih dulu, nilai
// hash ditandatangani dengan kunci privat pengirim, dan penerima
// memverifikasinya dengan kunci publik pengirim. Pasangan kunci diambil dari
// Contoh Terhitung Bab 10 (p = 47, q = 71, e = 79, d = 1019) supaya hasilnya
// dapat diperiksa dengan angka yang sudah dikenal.
//
// Fungsi hash SHA-256 di sini dibatasi pada pesan yang muat dalam satu blok
// (lebih pendek dari 56 byte); salinannya lengkap dengan penjelasan ada pada
// hash_avalanche.cpp.
//
// Kompilasi: g++ -std=c++17 -O2 -o tanda_tangan tanda_tangan.cpp
// Jalankan  : ./tanda_tangan   (Windows: tanda_tangan.exe)

#include <cstdint>
#include <cstdio>
#include <stdexcept>
#include <string>

// --- SHA-256 satu blok -----------------------------------------------------

const uint32_t K[64] = {
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
    0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
    0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
    0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
    0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2};

const uint32_t H0[8] = {0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};

uint32_t rotr(uint32_t x, int n) { return (x >> n) | (x << (32 - n)); }

void sha256(const std::string& pesan, uint32_t hash[8]) {
    if (pesan.size() >= 56) {
        throw std::invalid_argument(
            "Versi ini hanya menangani pesan yang lebih pendek dari 56 byte");
    }
    for (int i = 0; i < 8; i++) hash[i] = H0[i];

    uint8_t blok[64] = {0};
    for (std::size_t i = 0; i < pesan.size(); i++) {
        blok[i] = static_cast<uint8_t>(pesan[i]);
    }
    blok[pesan.size()] = 0x80;
    const uint64_t panjang_bit = static_cast<uint64_t>(pesan.size()) * 8;
    for (int i = 0; i < 8; i++) {
        blok[63 - i] = static_cast<uint8_t>(panjang_bit >> (8 * i));
    }

    uint32_t w[64];
    for (int t = 0; t < 16; t++) {
        w[t] = (static_cast<uint32_t>(blok[4 * t]) << 24) |
               (static_cast<uint32_t>(blok[4 * t + 1]) << 16) |
               (static_cast<uint32_t>(blok[4 * t + 2]) << 8) |
               static_cast<uint32_t>(blok[4 * t + 3]);
    }
    for (int t = 16; t < 64; t++) {
        uint32_t s0 = rotr(w[t - 15], 7) ^ rotr(w[t - 15], 18) ^ (w[t - 15] >> 3);
        uint32_t s1 = rotr(w[t - 2], 17) ^ rotr(w[t - 2], 19) ^ (w[t - 2] >> 10);
        w[t] = w[t - 16] + s0 + w[t - 7] + s1;
    }

    uint32_t a = hash[0], b = hash[1], c = hash[2], d = hash[3];
    uint32_t e = hash[4], f = hash[5], g = hash[6], h = hash[7];
    for (int t = 0; t < 64; t++) {
        uint32_t s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25);
        uint32_t ch = (e & f) ^ (~e & g);
        uint32_t temp1 = h + s1 + ch + K[t] + w[t];
        uint32_t s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22);
        uint32_t maj = (a & b) ^ (a & c) ^ (b & c);
        uint32_t temp2 = s0 + maj;
        h = g; g = f; f = e; e = d + temp1;
        d = c; c = b; b = a; a = temp1 + temp2;
    }
    hash[0] += a; hash[1] += b; hash[2] += c; hash[3] += d;
    hash[4] += e; hash[5] += f; hash[6] += g; hash[7] += h;
}

// Nilai hash sebagai bilangan bulat modulo n.
// Pada RSA nyata n berukuran 2048 bit atau lebih sehingga digest 256 bit muat
// tanpa pemangkasan; di sini modulusnya kecil, jadi pemangkasan diperlukan.
// Perhitungan dilakukan kata demi kata (metode Horner) agar tidak melampaui
// jangkauan bilangan bulat 64 bit.
long long hash_pesan(const std::string& pesan, long long n) {
    uint32_t hash[8];
    sha256(pesan, hash);

    long long nilai = 0;
    const long long basis = 4294967296LL % n;  // 2^32 mod n
    for (int i = 0; i < 8; i++) {
        nilai = (nilai * basis + hash[i] % n) % n;
    }
    return nilai;
}

// --- Aritmetika RSA --------------------------------------------------------

// Cari d sehingga e * d = 1 (mod phi) dengan Algoritma Euclidean diperluas.
long long invers_modulo(long long e, long long phi) {
    long long lama_d = 0, d = 1;
    long long lama_phi = phi, sisa = e;
    while (sisa != 0) {
        long long hasil_bagi = lama_phi / sisa;
        long long d_baru = lama_d - hasil_bagi * d;
        long long sisa_baru = lama_phi - hasil_bagi * sisa;
        lama_d = d; d = d_baru;
        lama_phi = sisa; sisa = sisa_baru;
    }
    if (lama_phi != 1) {
        throw std::invalid_argument("e tidak relatif prima terhadap phi(n)");
    }
    return ((lama_d % phi) + phi) % phi;
}

// Hitung basis^pangkat mod modulus dengan kuadrat berulang.
long long pangkat_mod(long long basis, long long pangkat, long long modulus) {
    long long hasil = 1;
    basis %= modulus;
    while (pangkat > 0) {
        if (pangkat & 1) hasil = (hasil * basis) % modulus;
        basis = (basis * basis) % modulus;
        pangkat >>= 1;
    }
    return hasil;
}

// Buat tanda tangan: S = hash(pesan)^d mod n, memakai kunci privat.
long long tanda_tangani(const std::string& pesan, long long d, long long n) {
    return pangkat_mod(hash_pesan(pesan, n), d, n);
}

// Verifikasi: nilai hash yang dipulihkan dengan kunci publik dibandingkan
// dengan hash pesan yang diterima.
bool verifikasi(const std::string& pesan, long long tanda_tangan, long long e,
                long long n) {
    long long hash_dipulihkan = pangkat_mod(tanda_tangan, e, n);
    return hash_dipulihkan == hash_pesan(pesan, n);
}

int main() {
    // Kunci Bob: publik untuk memverifikasi, privat untuk menandatangani.
    const long long p = 47, q = 71, e = 79;
    const long long n = p * q;
    const long long d = invers_modulo(e, (p - 1) * (q - 1));

    std::printf("Kunci publik  (e, n) = (%lld, %lld)\n", e, n);
    std::printf("Kunci privat  (d, n) = (%lld, %lld)\n\n", d, n);

    const std::string pesan = "Transfer Rp5.000.000 ke rekening 1234567890";
    const long long tt = tanda_tangani(pesan, d, n);

    std::printf("Pesan        : %s\n", pesan.c_str());
    std::printf("Hash (mod n) : %lld\n", hash_pesan(pesan, n));
    std::printf("Tanda tangan : %lld\n\n", tt);
    std::printf("Verifikasi pesan asli        : %s\n\n",
                verifikasi(pesan, tt, e, n) ? "true" : "false");

    // Penyerang mengubah isi pesan, tetapi tanda tangannya tetap yang lama.
    const std::string pesan_palsu = "Transfer Rp5.000.000 ke rekening 9999999999";
    std::printf("Pesan diubah : %s\n", pesan_palsu.c_str());
    std::printf("Hash (mod n) : %lld\n", hash_pesan(pesan_palsu, n));
    std::printf("Verifikasi pesan yang diubah : %s\n\n",
                verifikasi(pesan_palsu, tt, e, n) ? "true" : "false");

    std::printf("Tanda tangan tidak lagi cocok karena hash pesan yang diubah "
                "berbeda\n");
    std::printf("dari nilai hash yang dipulihkan dengan kunci publik. Penyerang "
                "yang\n");
    std::printf("ingin memalsukan tanda tangan harus menemukan kolisi SHA-256, "
                "yaitu\n");
    std::printf("dua pesan berbeda dengan hash sama, dan itu tidak praktis. "
                "Inilah\n");
    std::printf("yang memberi sifat nirpenyangkalan (non-repudiation): hanya "
                "pemegang\n");
    std::printf("kunci privat yang dapat membuat tanda tangan yang sah.\n");
    return 0;
}
