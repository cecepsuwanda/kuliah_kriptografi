// Demonstrasi kebocoran pola pada mode ECB dibandingkan mode CBC.
// Bab 6, Aktivitas 6.1.
//
// Untuk kejelasan, block cipher-nya diganti dengan permutasi sederhana
// (block cipher mainan). Tujuannya menunjukkan perilaku mode, bukan kekuatan
// algoritmanya.
//
// Kompilasi: g++ -std=c++17 -O2 -o mode_operasi mode_operasi.cpp
// Jalankan  : ./mode_operasi   (Windows: mode_operasi.exe)

#include <cstdio>
#include <string>
#include <vector>

const int BLOCK = 4;  // ukuran blok dalam karakter

// Block cipher mainan: XOR dengan kunci yang bergeser tiap posisi, lalu putar.
// Kunci bergeser per posisi (kunci + indeks) supaya tiap posisi dalam blok
// mendapat nilai berbeda. Penyandian tetap dapat dibalik, sehingga hasilnya sah
// sebagai block cipher walau sengaja dibuat lemah.
std::string kunci_putaran(const std::string& blok, int kunci) {
    std::string tergeser = blok;
    for (int posisi = 0; posisi < static_cast<int>(blok.size()); posisi++) {
        tergeser[posisi] = static_cast<char>(
            (blok[posisi] ^ (kunci + posisi)) & 0x7F);
    }
    return tergeser.substr(1) + tergeser.substr(0, 1);  // putar satu posisi
}

// Potong teks menjadi blok berukuran tetap, tambah padding bila perlu.
std::vector<std::string> bagi_blok(const std::string& teks) {
    std::string lengkap = teks;
    int padding = (BLOCK - static_cast<int>(teks.size()) % BLOCK) % BLOCK;
    lengkap.append(static_cast<std::size_t>(padding), ' ');

    std::vector<std::string> blok;
    for (std::size_t i = 0; i < lengkap.size(); i += BLOCK) {
        blok.push_back(lengkap.substr(i, BLOCK));
    }
    return blok;
}

// XOR dua blok karakter per karakter.
std::string tambah_xor(const std::string& a, const std::string& b) {
    std::string hasil = a;
    for (std::size_t i = 0; i < a.size(); i++) {
        hasil[i] = static_cast<char>(a[i] ^ b[i]);
    }
    return hasil;
}

// Setiap blok dienkripsi sendiri-sendiri, tanpa kaitan antar blok.
std::vector<std::string> enkripsi_ecb(const std::string& plainteks, int kunci) {
    std::vector<std::string> hasil;
    for (const std::string& blok : bagi_blok(plainteks)) {
        hasil.push_back(kunci_putaran(blok, kunci));
    }
    return hasil;
}

// Setiap blok di-XOR dengan cipherteks sebelumnya sebelum dienkripsi.
std::vector<std::string> enkripsi_cbc(const std::string& plainteks, int kunci,
                                      const std::string& iv) {
    std::vector<std::string> hasil;
    std::string sebelumnya = iv;
    for (const std::string& blok : bagi_blok(plainteks)) {
        std::string blok_cipher =
            kunci_putaran(tambah_xor(blok, sebelumnya), kunci);
        hasil.push_back(blok_cipher);
        sebelumnya = blok_cipher;
    }
    return hasil;
}

// Tampilkan blok sebagai heksadesimal agar tiap byte terbaca jelas.
void tampilkan_hex(const std::string& blok) {
    for (std::size_t i = 0; i < blok.size(); i++) {
        if (i > 0) std::printf(" ");
        std::printf("%02X", static_cast<unsigned char>(blok[i]));
    }
    std::printf("\n");
}

int main() {
    // Pola berulang yang mencolok, seperti area warna rata pada sebuah gambar.
    const std::string plainteks = "AAAAAAAABBBBBBBBAAAAAAAA";
    const int kunci = 0x5A;
    const std::string iv = "INIT";

    const std::vector<std::string> blok_ecb = enkripsi_ecb(plainteks, kunci);
    const std::vector<std::string> blok_cbc =
        enkripsi_cbc(plainteks, kunci, iv);

    std::printf("Plainteks   : %s\n", plainteks.c_str());
    std::printf("Blok        : ");
    for (const std::string& blok : bagi_blok(plainteks)) {
        std::printf("%s | ", blok.c_str());
    }
    std::printf("\n\n");

    std::printf("ECB (blok identik -> cipher identik):\n");
    for (const std::string& blok : blok_ecb) {
        std::printf("   ");
        tampilkan_hex(blok);
    }

    std::printf("\nCBC (blok identik -> cipher berbeda):\n");
    for (const std::string& blok : blok_cbc) {
        std::printf("   ");
        tampilkan_hex(blok);
    }

    std::printf(
        "\nPada ECB, blok 1 dan 2 (AAAA) menghasilkan cipherteks yang sama,\n");
    std::printf("demikian pula blok 3 dan 4 (BBBB), sehingga pola data asli "
                "terbaca.\n");
    std::printf("Pada CBC, setiap blok terkait dengan blok sebelumnya, sehingga\n");
    std::printf("blok yang sama menghasilkan cipherteks yang berbeda.\n");
    return 0;
}
