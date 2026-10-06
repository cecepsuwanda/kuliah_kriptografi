// Cipher Caesar: enkripsi, dekripsi, dan pemecahan dengan analisis frekuensi.
// Bab 4, Aktivitas 4.1.
//
// Kompilasi: g++ -std=c++17 -O2 -o caesar caesar.cpp
// Jalankan  : ./caesar   (Windows: caesar.exe)

#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

const std::string ABJAD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// Urutan kemunculan huruf dalam bahasa Indonesia, dipakai sebagai tebakan awal.
const std::string URUTAN_BAHASA = "AENIRSTUDKMLGBOPWYHFCJZVXQ";

// Geser setiap huruf sejauh k posisi (Caesar cipher).
std::string enkripsi(const std::string& plainteks, int k) {
    std::string hasil;
    for (char karakter : plainteks) {
        char huruf = static_cast<char>(
            std::toupper(static_cast<unsigned char>(karakter)));
        std::size_t posisi = ABJAD.find(huruf);
        if (posisi == std::string::npos) {
            hasil += huruf;  // spasi dan tanda baca tidak diubah
        } else {
            int geser = ((static_cast<int>(posisi) + k) % 26 + 26) % 26;
            hasil += ABJAD[static_cast<std::size_t>(geser)];
        }
    }
    return hasil;
}

// Kebalikan enkripsi: geser balik sejauh k posisi.
std::string dekripsi(const std::string& cipherteks, int k) {
    return enkripsi(cipherteks, -k);
}

// Pasangan (huruf, jumlah) terurut dari yang paling sering muncul.
std::vector<std::pair<char, int>> hitung_frekuensi(const std::string& teks) {
    std::vector<std::pair<char, int>> jumlah;
    for (char huruf : ABJAD) jumlah.push_back({huruf, 0});
    for (char karakter : teks) {
        char huruf = static_cast<char>(
            std::toupper(static_cast<unsigned char>(karakter)));
        std::size_t posisi = ABJAD.find(huruf);
        if (posisi != std::string::npos) jumlah[posisi].second++;
    }
    std::sort(jumlah.begin(), jumlah.end(),
              [](const auto& a, const auto& b) { return a.second > b.second; });
    return jumlah;
}

// Tebak kunci dengan menyelaraskan huruf tersering ke urutan huruf bahasa.
int pecahkan(const std::string& cipherteks, std::string& hasil) {
    std::vector<std::pair<char, int>> terurut = hitung_frekuensi(cipherteks);
    std::size_t i = 0;
    while (i < terurut.size() && terurut[i].second == 0) i++;
    if (i == terurut.size()) return -1;  // tidak ada huruf yang bisa dianalisis

    int posisi_tertinggi = static_cast<int>(ABJAD.find(terurut[i].first));
    int posisi_bahasa = static_cast<int>(ABJAD.find(URUTAN_BAHASA[0]));
    int tebakan_kunci = ((posisi_tertinggi - posisi_bahasa) % 26 + 26) % 26;
    hasil = dekripsi(cipherteks, tebakan_kunci);
    return tebakan_kunci;
}

int main() {
    const std::string plainteks =
        "KRIPTOGRAFI ADALAH ILMU DAN SENI MENJAGA KEAMANAN PESAN";
    const int kunci = 3;

    std::string cipherteks = enkripsi(plainteks, kunci);
    std::cout << "Plainteks : " << plainteks << "\n";
    std::cout << "Kunci     : " << kunci << "\n";
    std::cout << "Cipherteks: " << cipherteks << "\n";
    std::cout << "Dekripsi  : " << dekripsi(cipherteks, kunci) << "\n\n";

    std::cout << "Frekuensi huruf cipherteks (10 teratas):\n";
    std::vector<std::pair<char, int>> frekuensi = hitung_frekuensi(cipherteks);
    for (std::size_t i = 0; i < 10 && i < frekuensi.size(); i++) {
        std::cout << "  " << frekuensi[i].first << ": "
                  << frekuensi[i].second << "\n";
    }

    std::string hasil;
    int kunci_tebakan = pecahkan(cipherteks, hasil);
    std::cout << "\nKunci hasil analisis frekuensi: " << kunci_tebakan << "\n";
    std::cout << "Hasil pemecahan              : " << hasil << "\n";
    return 0;
}
