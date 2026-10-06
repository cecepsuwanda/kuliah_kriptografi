// Stream cipher sederhana berbasis XOR dan demonstrasi efek bit-flip.
// Bab 5, Aktivitas 5.1.
//
// Kompilasi: g++ -std=c++17 -O2 -o stream_cipher stream_cipher.cpp
// Jalankan  : ./stream_cipher   (Windows: stream_cipher.exe)

#include <iostream>
#include <stdexcept>
#include <string>

// Ubah teks menjadi string biner 8 bit per karakter.
std::string ke_biner(const std::string& teks) {
    std::string biner;
    for (unsigned char karakter : teks) {
        for (int bit = 7; bit >= 0; bit--) {
            biner += ((karakter >> bit) & 1) ? '1' : '0';
        }
    }
    return biner;
}

// Ubah string biner (kelipatan 8 bit) kembali menjadi teks.
std::string dari_biner(const std::string& biner) {
    if (biner.size() % 8 != 0) {
        throw std::invalid_argument("Panjang string biner harus kelipatan 8");
    }
    std::string teks;
    for (std::size_t i = 0; i < biner.size(); i += 8) {
        unsigned char nilai = 0;
        for (std::size_t j = 0; j < 8; j++) {
            nilai = static_cast<unsigned char>(nilai << 1);
            if (biner[i + j] == '1') nilai |= 1;
        }
        teks += static_cast<char>(nilai);
    }
    return teks;
}

// XOR dua string biner dengan panjang sama.
std::string xor_biner(const std::string& a, const std::string& b) {
    if (a.size() != b.size()) {
        throw std::invalid_argument("Panjang kedua string biner harus sama");
    }
    std::string hasil = a;
    for (std::size_t i = 0; i < a.size(); i++) {
        hasil[i] = (a[i] != b[i]) ? '1' : '0';
    }
    return hasil;
}

int main() {
    const std::string plainteks = "KRIPTO";
    const std::string kunci = "RAHASI";  // panjang kunci harus sama dengan pesan

    if (kunci.size() != plainteks.size()) {
        std::cerr << "Panjang kunci harus sama dengan panjang plainteks\n";
        return 1;
    }

    const std::string biner_plainteks = ke_biner(plainteks);
    const std::string biner_kunci = ke_biner(kunci);

    // Enkripsi dan dekripsi adalah operasi yang sama: XOR dengan kunci.
    const std::string cipherteks = xor_biner(biner_plainteks, biner_kunci);
    const std::string hasil_dekripsi = dari_biner(xor_biner(cipherteks, biner_kunci));

    std::cout << "Plainteks      : " << plainteks << "\n";
    std::cout << "Kunci          : " << kunci << "\n";
    std::cout << "Biner plainteks: " << biner_plainteks << "\n";
    std::cout << "Biner kunci    : " << biner_kunci << "\n";
    std::cout << "Biner cipher   : " << cipherteks << "\n";
    std::cout << "Dekripsi       : " << hasil_dekripsi << "\n\n";

    // Ubah bit pertama cipherteks, lalu dekripsi kembali.
    std::string cipherteks_rusak = cipherteks;
    cipherteks_rusak[0] = (cipherteks_rusak[0] == '0') ? '1' : '0';
    const std::string hasil_rusak =
        dari_biner(xor_biner(cipherteks_rusak, biner_kunci));

    std::cout << "Cipherteks dengan bit pertama dibalik: "
              << cipherteks_rusak << "\n";
    std::cout << "Hasil dekripsinya                   : "
              << hasil_rusak << "\n\n";
    std::cout << "Perhatikan bahwa satu bit yang berubah hanya merusak satu "
                 "karakter.\n";
    std::cout << "Pada mode operasi seperti CBC, kesalahan itu menjalar ke blok "
                 "berikutnya.\n";
    return 0;
}
