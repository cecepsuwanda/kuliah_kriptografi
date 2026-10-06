// Simulasi tahap ShiftRows pada matriks state AES.
// Bab 8, Aktivitas 8.1.
//
// Blok 16 byte dipetakan ke matriks state 4 x 4, lalu baris ke-r digeser
// siklik ke kiri sejauh r byte (baris 0 tetap, baris 1 geser 1 byte, baris 2
// geser 2 byte, baris 3 geser 3 byte).
//
// Kompilasi: g++ -std=c++17 -O2 -o aes_shiftrows aes_shiftrows.cpp
// Jalankan  : ./aes_shiftrows   (Windows: aes_shiftrows.exe)

#include <cstdio>
#include <cstring>
#include <stdexcept>
#include <string>

const int BARIS = 4;
const int KOLOM = 4;

typedef unsigned char State[BARIS][KOLOM];

const std::string BLOK = "Kriptografi-AES!";  // tepat 16 byte, satu blok AES

// Petakan 16 byte ke state 4 x 4 dengan pengisian kolom demi kolom.
// Byte ke-i masuk ke state[i mod 4][i div 4], sama seperti AES: empat byte
// pertama mengisi kolom pertama, empat byte berikutnya kolom kedua, dan
// seterusnya.
void ke_state(const std::string& blok, State state) {
    if (blok.size() != BARIS * KOLOM) {
        throw std::invalid_argument("Blok harus tepat 16 byte");
    }
    for (int baris = 0; baris < BARIS; baris++) {
        for (int kolom = 0; kolom < KOLOM; kolom++) {
            state[baris][kolom] =
                static_cast<unsigned char>(blok[KOLOM * kolom + baris]);
        }
    }
}

// Kebalikan ke_state: susun kembali 16 byte dari matriks.
std::string dari_state(State state) {
    std::string blok;
    for (int kolom = 0; kolom < KOLOM; kolom++) {
        for (int baris = 0; baris < BARIS; baris++) {
            blok += static_cast<char>(state[baris][kolom]);
        }
    }
    return blok;
}

// Geser baris ke-r siklik ke kiri sejauh r byte.
void shift_rows(State state) {
    for (int r = 0; r < BARIS; r++) {
        unsigned char semula[KOLOM];
        std::memcpy(semula, state[r], KOLOM);
        for (int kolom = 0; kolom < KOLOM; kolom++) {
            state[r][kolom] = semula[(kolom + r) % KOLOM];
        }
    }
}

// Kebalikan ShiftRows: geser baris ke-r siklik ke kanan sejauh r byte.
void inv_shift_rows(State state) {
    for (int r = 0; r < BARIS; r++) {
        unsigned char semula[KOLOM];
        std::memcpy(semula, state[r], KOLOM);
        for (int kolom = 0; kolom < KOLOM; kolom++) {
            state[r][kolom] = semula[(kolom - r + KOLOM) % KOLOM];
        }
    }
}

// Cetak matriks sebagai bilangan sekaligus karakternya.
void tampilkan(State state, const char* judul) {
    std::printf("%s\n", judul);
    for (int baris = 0; baris < BARIS; baris++) {
        std::printf("    ");
        for (int kolom = 0; kolom < KOLOM; kolom++) {
            std::printf("%3d ", state[baris][kolom]);
        }
        std::printf("    ");
        for (int kolom = 0; kolom < KOLOM; kolom++) {
            std::printf("%c", state[baris][kolom]);
        }
        std::printf("\n");
    }
    std::printf("\n");
}

int main() {
    State state_awal, state_geser, state_kembali;

    std::printf("Blok plainteks : %s\n", BLOK.c_str());
    std::printf("Panjang        : %d byte\n\n", static_cast<int>(BLOK.size()));

    // Nomor byte 0..15, supaya perpindahan posisi mudah dilihat.
    std::printf("Nomor byte pada state awal (sebelum ShiftRows):\n");
    for (int baris = 0; baris < BARIS; baris++) {
        std::printf("    ");
        for (int kolom = 0; kolom < KOLOM; kolom++) {
            std::printf("%3d ", KOLOM * kolom + baris);
        }
        std::printf("\n");
    }
    std::printf("\n");

    ke_state(BLOK, state_awal);
    tampilkan(state_awal, "State awal (baris, kolom):");

    std::memcpy(state_geser, state_awal, sizeof(State));
    shift_rows(state_geser);
    tampilkan(state_geser, "Setelah ShiftRows:");

    std::memcpy(state_kembali, state_geser, sizeof(State));
    inv_shift_rows(state_kembali);
    tampilkan(state_kembali, "Setelah InvShiftRows (kembali ke awal):");

    std::printf("Baris 0 tidak bergeser, baris 1 bergeser 1 byte, baris 2 "
                "bergeser\n");
    std::printf("2 byte, dan baris 3 bergeser 3 byte. Akibatnya byte-byte dari "
                "satu\n");
    std::printf("kolom yang sama menyebar ke empat kolom berbeda. Inilah "
                "difusi:\n");
    std::printf("perubahan satu byte cepat memengaruhi seluruh state pada "
                "putaran\nberikutnya.\n\n");
    std::printf("InvShiftRows mengembalikan susunan semula: %s\n",
                dari_state(state_kembali) == BLOK ? "true" : "false");
    return 0;
}
