// Efek longsoran (avalanche effect) pada fungsi hash SHA-256.
// Bab 15, Aktivitas 15.1.
//
// SHA-256 tidak tersedia pada pustaka standar C++, jadi fungsi kompresinya
// diimplementasikan sendiri. Versi ini sengaja dibatasi pada pesan yang muat
// dalam satu blok 512 bit, yaitu pesan yang lebih pendek dari 56 byte; pesan
// yang lebih panjang memerlukan pemrosesan blok demi blok. Kedua kalimat pada
// Aktivitas 15.1 jauh lebih pendek dari batas itu, sehingga hasilnya sama
// dengan SHA-256 yang dihitung alat bantu seperti CyberChef.
//
// Kompilasi: g++ -std=c++17 -O2 -o hash_avalanche hash_avalanche.cpp
// Jalankan  : ./hash_avalanche   (Windows: hash_avalanche.exe)

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

// Hitung SHA-256 untuk pesan yang muat dalam satu blok 512 bit.
void sha256_satu_blok(const std::string& pesan, uint32_t hash[8]) {
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

    uint32_t a = hash[0], b = hash[1], c = hash[2], d = hash[3];
    uint32_t e = hash[4], f = hash[5], g = hash[6], h = hash[7];

    for (int t = 0; t < 64; t++) {
        uint32_t s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25);
        uint32_t ch = (e & f) ^ (~e & g);
        uint32_t temp1 = h + s1 + ch + K[t] + w[t];
        uint32_t s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22);
        uint32_t maj = (a & b) ^ (a & c) ^ (b & c);
        uint32_t temp2 = s0 + maj;

        h = g;
        g = f;
        f = e;
        e = d + temp1;
        d = c;
        c = b;
        b = a;
        a = temp1 + temp2;
    }

    hash[0] += a;
    hash[1] += b;
    hash[2] += c;
    hash[3] += d;
    hash[4] += e;
    hash[5] += f;
    hash[6] += g;
    hash[7] += h;
}

// Hitung digest SHA-256 dari pesan sebagai 8 kata 32 bit.
void sha256(const std::string& pesan, uint32_t hash[8]) {
    for (int i = 0; i < 8; i++) hash[i] = H0[i];
    sha256_satu_blok(pesan, hash);
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

// Hitung jumlah bit 1 pada sebuah kata.
int jumlah_bit(uint32_t nilai) {
    int jumlah = 0;
    while (nilai) {
        jumlah += nilai & 1;
        nilai >>= 1;
    }
    return jumlah;
}

// Hitung jumlah bit yang berbeda antara dua digest.
int selisih_bit(const uint32_t a[8], const uint32_t b[8]) {
    int beda = 0;
    for (int i = 0; i < 8; i++) beda += jumlah_bit(a[i] ^ b[i]);
    return beda;
}

// Cetak perbandingan longsoran antara acuan dan satu varian pesan.
void bandingkan(const std::string& acuan, const std::string& varian) {
    uint32_t hash_acuan[8], hash_varian[8];
    sha256(acuan, hash_acuan);
    sha256(varian, hash_varian);
    std::printf("  %-34s -> %3d bit berbeda\n", varian.c_str(),
                selisih_bit(hash_acuan, hash_varian));
}

int main() {
    const std::string pesan_a = "Kriptografi itu Menyenangkan";
    const std::string pesan_b = "Kriptografi itu menyenangkan";  // satu karakter

    uint32_t hash_a[8], hash_b[8];
    sha256(pesan_a, hash_a);
    sha256(pesan_b, hash_b);

    const int jumlah_bit_keluar = 256;  // SHA-256 menghasilkan 256 bit
    const int beda = selisih_bit(hash_a, hash_b);

    std::printf("Pesan A : %s\n", pesan_a.c_str());
    std::printf("Hash A  : %s\n\n", ke_heks(hash_a).c_str());
    std::printf("Pesan B : %s\n", pesan_b.c_str());
    std::printf("Hash B  : %s\n\n", ke_heks(hash_b).c_str());
    std::printf("Ukuran digest        : %d bit\n", jumlah_bit_keluar);
    std::printf("Bit yang berbeda     : %d bit\n", beda);
    std::printf("Persentase perbedaan : %.1f%%\n\n",
                100.0 * beda / jumlah_bit_keluar);

    std::printf("Perbandingan tambahan (satu karakter diubah pada tiap baris):\n");
    bandingkan("Kriptografi", "kriptografi");
    bandingkan("Kriptografi", "Kriptografj");
    bandingkan("Kriptografi", "Kriptografi ");
    bandingkan("Kriptografi", "Kriptograf");
    std::printf("\n");

    std::printf("Jika keluaran hash bersifat acak, sekitar separuh bitnya (128 "
                "dari\n");
    std::printf("256) diharapkan berbeda. Perubahan satu karakter saja sudah\n");
    std::printf("mengubah sekitar separuh digest. Sifat inilah yang membuat "
                "hash\n");
    std::printf("berguna untuk pemeriksaan keutuhan: perubahan sekecil apa pun "
                "pada\n");
    std::printf("pesan langsung terdeteksi, dan penyerang tidak dapat menyusun "
                "pesan\n");
    std::printf("lain dengan hash yang sama tanpa memecahkan sifat "
                "tahan-kolisi.\n");
    return 0;
}
