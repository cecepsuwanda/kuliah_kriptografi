// ElGamal: pembangkitan kunci, enkripsi, dan dekripsi pada bilangan kecil.
// Bab 12, Aktivitas 12.1 dan Contoh Terhitung Bab 12.
//
// Kompilasi: g++ -std=c++17 -O2 -o elgamal elgamal.cpp
// Jalankan  : ./elgamal   (Windows: elgamal.exe)

#include <cstdio>
#include <stdexcept>

// Hitung basis^pangkat mod modulus dengan kuadrat berulang.
// Hasil kali terbesar adalah (modulus-1)^2, aman selama modulus < 3 miliar.
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

// Kunci publik y = g^x mod p.
long long kunci_publik(long long g, long long x, long long p) {
    return pangkat_mod(g, x, p);
}

// Enkripsi: a = g^k mod p, dan b = y^k * m mod p.
// Nilai k harus dipilih acak dan berbeda untuk setiap pesan.
void enkripsi(long long m, long long y, long long g, long long p, long long k,
              long long& a, long long& b) {
    if (m < 0 || m >= p) {
        throw std::invalid_argument("Pesan m harus berada pada selang [0, p-1]");
    }
    a = pangkat_mod(g, k, p);
    b = (pangkat_mod(y, k, p) * m) % p;
}

// Dekripsi: m = b * (a^x)^-1 mod p.
// Invers a^x dihitung sebagai a^(p-1-x) mod p, karena a^(p-1) = 1 (mod p)
// menurut Teorema Kecil Fermat.
long long dekripsi(long long a, long long b, long long x, long long p) {
    long long invers_a_x = pangkat_mod(a, p - 1 - x, p);
    return (b * invers_a_x) % p;
}

// Jalankan satu siklus ElGamal lengkap dan cetak setiap langkahnya.
void jalankan(long long p, long long g, long long x, long long m, long long k,
              const char* catatan) {
    std::printf("====================================================================\n");
    std::printf("%s\n", catatan);
    std::printf("====================================================================\n");

    long long y = kunci_publik(g, x, p);
    long long a, b;
    enkripsi(m, y, g, p, k, a, b);
    long long m_pulih = dekripsi(a, b, x, p);

    std::printf("Parameter publik : p = %lld, g = %lld\n", p, g);
    std::printf("Kunci privat Bob : x = %lld\n", x);
    std::printf("Kunci publik Bob : y = g^x mod p = %lld^%lld mod %lld = %lld\n\n",
                g, x, p, y);
    std::printf("Pesan       m = %lld\n", m);
    std::printf("Kunci acak  k = %lld\n", k);
    std::printf("a = g^k mod p     = %lld^%lld mod %lld = %lld\n", g, k, p, a);
    std::printf("b = y^k * m mod p = %lld^%lld * %lld mod %lld = %lld\n",
                y, k, m, p, b);
    std::printf("Cipherteks  (a, b) = (%lld, %lld)\n\n", a, b);
    std::printf("Dekripsi m = b * (a^x)^-1 mod p = %lld\n", m_pulih);
    std::printf("Pesan pulih dengan tepat: %s\n\n",
                m_pulih == m ? "true" : "false");
}

int main() {
    jalankan(2273, 3, 243, 700, 1463,
             "Contoh Terhitung Bab 12: p = 2273, g = 3, x = 243");

    jalankan(2357, 2, 1751, 2035, 1520,
             "Aktivitas 12.1: p = 2357, g = 2, x = 1751");

    std::printf("Catatan keamanan:\n");
    std::printf("Ukuran cipherteks ElGamal dua kali ukuran plainteks, karena "
                "tiap\n");
    std::printf("pesan menghasilkan pasangan (a, b). Keamanannya bersandar pada\n");
    std::printf("persoalan logaritma diskret: penyerang yang melihat y, g, dan p\n");
    std::printf("harus mencari x. Selain itu, k harus dipilih acak dan tidak "
                "boleh\n");
    std::printf("digunakan ulang; memakai k yang sama untuk dua pesan membuat "
                "rasio\n");
    std::printf("kedua cipherteks membuka perbandingan plainteksnya.\n");
    return 0;
}
