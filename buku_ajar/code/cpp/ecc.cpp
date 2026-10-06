// Penjumlahan dan penggandaan titik pada kurva eliptik.
// Bab 14, Aktivitas 14.1 dan Contoh Terhitung Bab 14.
//
// Kurva ditulis dalam bentuk umum y^2 = x^3 + a*x + b. Dua medan didukung:
// kurva atas bilangan real (memakai double) dan kurva atas medan berhingga
// modulo prima p (memakai bilangan bulat dan invers modulo).
//
// Kompilasi: g++ -std=c++17 -O2 -o ecc ecc.cpp
// Jalankan  : ./ecc   (Windows: ecc.exe)

#include <cmath>
#include <cstdio>

// ---------------------------------------------------------------------------
// Kurva atas bilangan real
// ---------------------------------------------------------------------------

struct TitikReal {
    double x, y;
    bool takhingga;  // true menyatakan titik di ketakhinggaan (unsur identitas)
};

TitikReal titik_takhingga_real() { return {0.0, 0.0, true}; }

// Periksa apakah titik memenuhi persamaan kurva.
bool pada_kurva_real(TitikReal P, double a, double b) {
    if (P.takhingga) return true;
    double kiri = P.y * P.y;
    double kanan = P.x * P.x * P.x + a * P.x + b;
    return std::fabs(kiri - kanan) < 1e-9;
}

// Hitung R = 2P dengan rumus penggandaan titik: m = (3x^2 + a) / (2y).
TitikReal gandakan_real(TitikReal P, double a) {
    if (P.takhingga) return P;
    if (std::fabs(P.y) < 1e-9) return titik_takhingga_real();  // garis singgung tegak

    double m = (3 * P.x * P.x + a) / (2 * P.y);
    double x3 = m * m - 2 * P.x;
    double y3 = m * (P.x - x3) - P.y;
    return {x3, y3, false};
}

// Hitung R = P + Q dengan rumus m = (y2 - y1) / (x2 - x1).
TitikReal tambah_real(TitikReal P, TitikReal Q, double a) {
    if (P.takhingga) return Q;
    if (Q.takhingga) return P;
    if (std::fabs(P.x - Q.x) < 1e-9) {
        if (std::fabs(P.y + Q.y) < 1e-9) return titik_takhingga_real();
        return gandakan_real(P, a);  // P == Q, pakai rumus penggandaan
    }
    double m = (Q.y - P.y) / (Q.x - P.x);
    double x3 = m * m - P.x - Q.x;
    double y3 = m * (P.x - x3) - P.y;
    return {x3, y3, false};
}

// ---------------------------------------------------------------------------
// Kurva modulo prima p
// ---------------------------------------------------------------------------

struct TitikMod {
    long long x, y;
    bool takhingga;
};

TitikMod titik_takhingga_mod() { return {0, 0, true}; }

// Invers perkalian nilai modulo p dengan Algoritma Euclidean diperluas.
long long invers_modulo(long long nilai, long long p) {
    long long lama_d = 0, d = 1;
    long long lama_p = p, sisa = ((nilai % p) + p) % p;
    while (sisa != 0) {
        long long hasil_bagi = lama_p / sisa;
        long long d_baru = lama_d - hasil_bagi * d;
        long long sisa_baru = lama_p - hasil_bagi * sisa;
        lama_d = d;
        d = d_baru;
        lama_p = sisa;
        sisa = sisa_baru;
    }
    return ((lama_d % p) + p) % p;
}

bool pada_kurva_mod(TitikMod P, long long a, long long b, long long p) {
    if (P.takhingga) return true;
    long long kiri = (P.y * P.y) % p;
    long long kanan = (P.x * P.x % p * P.x + a * P.x + b) % p;
    return ((kiri - kanan) % p + p) % p == 0;
}

// Hitung R = 2P pada kurva modulo p.
TitikMod gandakan_mod(TitikMod P, long long a, long long p) {
    if (P.takhingga || P.y % p == 0) return titik_takhingga_mod();
    long long m = ((3 * P.x % p * P.x + a) % p) * invers_modulo(2 * P.y % p, p) % p;
    long long x3 = ((m * m - 2 * P.x) % p + p) % p;
    long long y3 = ((m * (P.x - x3) - P.y) % p + p) % p;
    return {x3, y3, false};
}

// Hitung R = P + Q pada kurva modulo p.
TitikMod tambah_mod(TitikMod P, TitikMod Q, long long a, long long p) {
    if (P.takhingga) return Q;
    if (Q.takhingga) return P;
    if ((P.x - Q.x) % p == 0) {
        if ((P.y + Q.y) % p == 0) return titik_takhingga_mod();
        return gandakan_mod(P, a, p);
    }
    long long pembilang = ((Q.y - P.y) % p + p) % p;
    long long penyebut = ((Q.x - P.x) % p + p) % p;
    long long m = pembilang * invers_modulo(penyebut, p) % p;
    long long x3 = ((m * m - P.x - Q.x) % p + p) % p;
    long long y3 = ((m * (P.x - x3) - P.y) % p + p) % p;
    return {x3, y3, false};
}

// Hitung k*P dengan metode double-and-add.
TitikMod kali_mod(long long k, TitikMod P, long long a, long long p) {
    TitikMod hasil = titik_takhingga_mod();
    TitikMod penambah = P;
    while (k > 0) {
        if (k & 1) hasil = tambah_mod(hasil, penambah, a, p);
        penambah = gandakan_mod(penambah, a, p);
        k >>= 1;
    }
    return hasil;
}

// ---------------------------------------------------------------------------
// Penyajian hasil
// ---------------------------------------------------------------------------

void cetak_real(const char* label, TitikReal P) {
    if (P.takhingga) {
        std::printf("  %s = O (titik di ketakhinggaan)\n", label);
    } else {
        std::printf("  %s = (%.10g, %.10g)\n", label, P.x, P.y);
    }
}

void cetak_mod(const char* label, TitikMod P) {
    if (P.takhingga) {
        std::printf("  %s = O (titik di ketakhinggaan)\n", label);
    } else {
        std::printf("  %s = (%lld, %lld)\n", label, P.x, P.y);
    }
}

int main() {
    // --- Kurva atas bilangan real: contoh terhitung bab ---------------------
    const double a_real = -3, b_real = 3;
    TitikReal P = {1, 1, false}, Q = {-2, 1, false};
    std::printf("Kurva y^2 = x^3 - 3x + 3\n");
    std::printf("  P pada kurva: %s\n", pada_kurva_real(P, a_real, b_real) ? "true" : "false");
    std::printf("  Q pada kurva: %s\n", pada_kurva_real(Q, a_real, b_real) ? "true" : "false");
    cetak_real("P + Q", tambah_real(P, Q, a_real));
    cetak_real("2P   ", gandakan_real(P, a_real));
    std::printf("\n");

    // --- Kurva dari Aktivitas 14.1 -----------------------------------------
    const double a_akt = 2, b_akt = 4;
    TitikReal P2 = {2, 4, false}, Q2 = {0, 2, false};
    std::printf("Kurva y^2 = x^3 + 2x + 4 (Aktivitas 14.1)\n");
    cetak_real("P + Q", tambah_real(P2, Q2, a_akt));
    cetak_real("2P   ", gandakan_real(P2, a_akt));
    std::printf("\n");

    // --- Kurva modulo prima 23 ---------------------------------------------
    const long long a_mod = 1, b_mod = 1, p = 23;
    TitikMod Pm = {3, 10, false};
    TitikMod dua_p = gandakan_mod(Pm, a_mod, p);
    TitikMod tiga_p = tambah_mod(dua_p, Pm, a_mod, p);
    std::printf("Kurva y^2 = x^3 + x + 1 (mod 23)\n");
    std::printf("  P pada kurva: %s\n", pada_kurva_mod(Pm, a_mod, b_mod, p) ? "true" : "false");
    cetak_mod("2P    ", dua_p);
    cetak_mod("3P    ", tiga_p);
    std::printf("\n");

    // --- Pertukaran kunci ECDH pada kurva yang sama -------------------------
    const long long a_privat = 2, b_privat = 3;
    TitikMod basis = {3, 10, false};
    TitikMod PA = kali_mod(a_privat, basis, a_mod, p);
    TitikMod PB = kali_mod(b_privat, basis, a_mod, p);
    TitikMod K_alice = kali_mod(a_privat, PB, a_mod, p);
    TitikMod K_bob = kali_mod(b_privat, PA, a_mod, p);
    std::printf("Pertukaran kunci ECDH pada kurva yang sama\n");
    std::printf("  Kunci privat Alice a = %lld, publik A = aB\n", a_privat);
    cetak_mod("A    ", PA);
    std::printf("  Kunci privat Bob   b = %lld, publik B = bB\n", b_privat);
    cetak_mod("B    ", PB);
    cetak_mod("a*(bB)", K_alice);
    cetak_mod("b*(aB)", K_bob);
    std::printf("  Kunci bersama sama: %s\n\n",
                (K_alice.x == K_bob.x && K_alice.y == K_bob.y) ? "true" : "false");
    std::printf("Penyerang yang melihat B, PA, dan PB harus menyelesaikan ECDLP\n");
    std::printf("untuk memperoleh a atau b. Dengan modulus 23 persoalan itu "
                "dapat\n");
    std::printf("diselesaikan dengan mencoba seluruh kemungkinan; pada kurva "
                "nyata\n");
    std::printf("modulusnya berukuran 256 bit atau lebih.\n");
    return 0;
}
