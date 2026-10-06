// Perhitungan waktu brute force DES, Double DES, Triple DES, dan AES.
// Bab 7, Aktivitas 7.1.
//
// Karena 2^128 dan 2^256 jauh melampaui jangkauan bilangan bulat 64 bit,
// perhitungan dilakukan pada skala logaritma: log10(detik) = bit * log10(2).
// Hasil akhirnya ditampilkan dalam satuan waktu yang mudah dibaca.
//
// Kompilasi: g++ -std=c++17 -O2 -o kompleksitas_kunci kompleksitas_kunci.cpp
// Jalankan  : ./kompleksitas_kunci   (Windows: kompleksitas_kunci.exe)

#include <cmath>
#include <cstdio>

const double KECEPATAN_LOG10 = 9.0;  // 10^9 kunci per detik

// Tiap langkah: bagi nilai dengan faktor, lalu satuan berganti ke nama berikut.
struct Langkah {
    double faktor_log10;
    const char* nama;
};

const Langkah LANGKAH[] = {
    {std::log10(60.0), "menit"},
    {std::log10(60.0), "jam"},
    {std::log10(24.0), "hari"},
    {std::log10(365.25), "tahun"},
    {std::log10(1000.0), "ribu tahun"},
    {std::log10(1000.0), "juta tahun"},
    {std::log10(1000.0), "miliar tahun"},
};

const int JUMLAH_LANGKAH = sizeof(LANGKAH) / sizeof(LANGKAH[0]);

// Ubah log10(detik) menjadi satuan waktu yang mudah dibaca manusia.
void cetak_waktu(double log10_detik) {
    double nilai = log10_detik;
    const char* nama = "detik";
    for (int i = 0; i < JUMLAH_LANGKAH; i++) {
        if (nilai < LANGKAH[i].faktor_log10) {
            std::printf("%.2f %s\n", std::pow(10.0, nilai), nama);
            return;
        }
        nilai -= LANGKAH[i].faktor_log10;
        nama = LANGKAH[i].nama;
    }
    std::printf("%.2e %s\n", std::pow(10.0, nilai), nama);
}

// Waktu terburuk pencarian menyeluruh (seluruh ruang kunci dicoba).
double waktu_brute_force_log10(int panjang_efektif) {
    return panjang_efektif * std::log10(2.0) - KECEPATAN_LOG10;
}

int main() {
    // (nama, panjang kunci, panjang efektif, ruang kunci efektif)
    // Panjang efektif inilah yang menentukan waktu pencarian: Double DES hanya
    // menyisakan 2^57 karena serangan meet-in-the-middle (Bab 7 bagian 3),
    // sedangkan Triple DES dua kunci menyisakan 2^112.
    struct Percobaan {
        const char* nama;
        int panjang;
        int efektif;
        const char* ruang;
    };

    const Percobaan percobaan[] = {
        {"DES", 56, 56, "2^56"},
        {"Double DES", 112, 57, "2^57 efektif"},
        {"Triple DES", 168, 112, "2^112 efektif"},
        {"AES-128", 128, 128, "2^128"},
        {"AES-256", 256, 256, "2^256"},
    };
    const int JUMLAH = sizeof(percobaan) / sizeof(percobaan[0]);

    std::printf("Asumsi kecepatan penyerang: 1,000,000,000 kunci per detik\n\n");
    std::printf("%-13s%-8s%-18s%s\n", "Algoritma", "Kunci", "Ruang kunci",
                "Waktu");
    std::printf("----------------------------------------------------------------------\n");

    for (int i = 0; i < JUMLAH; i++) {
        char label_kunci[16];
        std::snprintf(label_kunci, sizeof(label_kunci), "%d bit",
                      percobaan[i].panjang);
        std::printf("%-13s%-8s%-18s", percobaan[i].nama, label_kunci,
                    percobaan[i].ruang);
        cetak_waktu(waktu_brute_force_log10(percobaan[i].efektif));
    }

    std::printf("\nCatatan: Double DES hanya menambah satu bit keamanan efektif "
                "(2^57, bukan 2^112)\n");
    std::printf("karena serangan meet-in-the-middle. Karena itu, memperpanjang "
                "kunci (AES-128)\n");
    std::printf("jauh lebih efektif daripada mengulang algoritma yang sama.\n");
    return 0;
}
