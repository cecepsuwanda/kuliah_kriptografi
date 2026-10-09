// Tanda tangan digital RSA: penandatanganan, verifikasi, dan uji pemalsuan.
// Bab 16, Aktivitas 16.1.
//
// Padanan C++ dari code/python/tanda_tangan.py. Pasangan kunci diambil dari
// Contoh Terhitung Bab 10 (p = 47, q = 71, e = 79, d = 1019) supaya hasilnya
// dapat diperiksa dengan angka yang sudah dikenal.
//
// SHA-256 tidak tersedia pada pustaka standar C++, jadi fungsi kompresinya
// diimplementasikan sendiri. Versi ini sengaja dibatasi pada pesan yang muat
// dalam satu blok 512 bit, yaitu pesan yang lebih pendek dari 56 byte; pesan
// yang lebih panjang memerlukan pemrosesan blok demi blok. Kedua kalimat uji
// pada bab ini hanya 43 byte, sehingga hasilnya sama dengan SHA-256 yang
// dihitung Python.
//
// Kompilasi: g++ -std=c++17 -O2 -o tanda_tangan tanda_tangan.cpp
// Jalankan  : ./tanda_tangan   (Windows: tanda_tangan.exe)

#include <cstdint>
#include <cstdio>
#include <stdexcept>
#include <string>

// Konstanta putaran SHA-256: 64 bit pertama bagian pecahan akar kubik
// bilangan prima ke-2 sampai ke-64.
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

// Nilai awal hash: 32 bit pertama bagian pecahan akar kuadrat delapan prima
// pertama.
const uint32_t H0[8] = {0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};

// Geser kanan siklik (rotate right) sejauh n bit.
uint32_t rotr(uint32_t x, int n) { return (x >> n) | (x << (32 - n)); }

// Hitung digest SHA-256 dari pesan yang muat dalam satu blok 512 bit.
void sha256(const std::string& pesan, uint32_t hash[8]) {
    if (pesan.size() >= 56) {
        throw std::invalid_argument(
            "Versi ini hanya menangani pesan yang lebih pendek dari 56 byte");
    }

    // Padding: bit 1, lalu nol secukupnya, lalu panjang pesan dalam bit.
    uint8_t blok[64] = {0};
    for (std::size_t i = 0; i < pesan.size(); i++) {
        blok[i] = static_cast<uint8_t>(pesan[i]);
    }
    blok[pesan.size()] = 0x80;
    const uint64_t panjang_bit = static_cast<uint64_t>(pesan.size()) * 8;
    for (int i = 0; i < 8; i++) {
        blok[63 - i] = static_cast<uint8_t>(panjang_bit >> (8 * i));
    }

    // Jadwal pesan: 16 kata pertama dari blok, sisanya diperluas.
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

    for (int i = 0; i < 8; i++) hash[i] = H0[i];

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

// Tampilkan digest sebagai 64 digit heksadesimal.
std::string ke_heks(const uint32_t hash[8]) {
    std::string teks;
    char buf[9];
    for (int i = 0; i < 8; i++) {
        std::snprintf(buf, sizeof(buf), "%08x", hash[i]);
        teks += buf;
    }
    return teks;
}

// Hash pesan sebagai bilangan bulat modulo n. Digest 256 bit direduksi kata
// demi kata dengan basis 2^32; cara ini sama dengan menghitung
// int(hexdigest, 16) % n seperti pada Python.
uint64_t hash_pesan(const std::string& pesan, uint64_t n) {
    uint32_t digest[8];
    sha256(pesan, digest);
    uint64_t nilai = 0;
    for (int i = 0; i < 8; i++) {
        nilai = (nilai * 4294967296ULL + digest[i]) % n;
    }
    return nilai;
}

// Perpangkatan modular: basis^eksponen mod modulus.
uint64_t pangkat_mod(uint64_t basis, uint64_t eksponen, uint64_t modulus) {
    uint64_t hasil = 1;
    basis %= modulus;
    while (eksponen > 0) {
        if (eksponen & 1ULL) hasil = (hasil * basis) % modulus;
        basis = (basis * basis) % modulus;
        eksponen >>= 1;
    }
    return hasil;
}

// Cari d sehingga e * d = 1 (mod phi), memakai Algoritma Euclidean lanjar.
uint64_t invers_modulo(uint64_t e, uint64_t phi) {
    int64_t lama_d = 0, d = 1;
    int64_t lama_phi = static_cast<int64_t>(phi), sisa = static_cast<int64_t>(e);
    while (sisa != 0) {
        int64_t hasil_bagi = lama_phi / sisa;
        int64_t d_baru = lama_d - hasil_bagi * d;
        lama_d = d; d = d_baru;
        int64_t sisa_baru = lama_phi - hasil_bagi * sisa;
        lama_phi = sisa; sisa = sisa_baru;
    }
    if (lama_phi != 1) {
        throw std::invalid_argument("e tidak relatif prima terhadap phi(n)");
    }
    return static_cast<uint64_t>((lama_d % static_cast<int64_t>(phi) +
                                  static_cast<int64_t>(phi)) %
                                 static_cast<int64_t>(phi));
}

// Buat tanda tangan: S = hash(pesan)^d mod n, memakai kunci privat.
uint64_t tanda_tangani(const std::string& pesan, uint64_t d, uint64_t n) {
    return pangkat_mod(hash_pesan(pesan, n), d, n);
}

// Verifikasi tanda tangan dengan kunci publik.
bool verifikasi(const std::string& pesan, uint64_t tanda_tangan,
                uint64_t e, uint64_t n) {
    return pangkat_mod(tanda_tangan, e, n) == hash_pesan(pesan, n);
}

int main() {
    // Kunci Bob: publik untuk memverifikasi, privat untuk menandatangani.
    const uint64_t p = 47, q = 71, e = 79;
    const uint64_t n = p * q;
    const uint64_t d = invers_modulo(e, (p - 1) * (q - 1));

    std::printf("Kunci publik  (e, n) = (%llu, %llu)\n",
                static_cast<unsigned long long>(e),
                static_cast<unsigned long long>(n));
    std::printf("Kunci privat  (d, n) = (%llu, %llu)\n\n",
                static_cast<unsigned long long>(d),
                static_cast<unsigned long long>(n));

    const std::string pesan = "Transfer Rp5.000.000 ke rekening 1234567890";
    const uint64_t tanda_tangan = tanda_tangani(pesan, d, n);

    std::printf("Pesan        : %s\n", pesan.c_str());
    std::printf("Hash (mod n) : %llu\n",
                static_cast<unsigned long long>(hash_pesan(pesan, n)));
    std::printf("Tanda tangan : %llu\n\n",
                static_cast<unsigned long long>(tanda_tangan));
    std::printf("Verifikasi pesan asli        : %s\n\n",
                verifikasi(pesan, tanda_tangan, e, n) ? "true" : "false");

    // Penyerang mengubah isi pesan, tetapi tanda tangannya tetap yang lama.
    const std::string pesan_palsu =
        "Transfer Rp5.000.000 ke rekening 9999999999";
    std::printf("Pesan diubah : %s\n", pesan_palsu.c_str());
    std::printf("Hash (mod n) : %llu\n",
                static_cast<unsigned long long>(hash_pesan(pesan_palsu, n)));
    std::printf("Verifikasi pesan yang diubah : %s\n\n",
                verifikasi(pesan_palsu, tanda_tangan, e, n) ? "true" : "false");

    std::printf("Tanda tangan tidak lagi cocok karena hash pesan yang diubah berbeda\n");
    std::printf("dari nilai hash yang dipulihkan dengan kunci publik. Penyerang yang\n");
    std::printf("ingin memalsukan tanda tangan harus menemukan kolisi SHA-256, yaitu\n");
    std::printf("dua pesan berbeda dengan hash sama, dan itu tidak praktis. Inilah\n");
    std::printf("yang memberi sifat nirpenyangkalan (non-repudiation): hanya pemegang\n");
    std::printf("kunci privat yang dapat membuat tanda tangan yang sah.\n");
    return 0;
}
