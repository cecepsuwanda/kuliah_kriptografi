// Pertukaran kunci Diffie-Hellman pada bilangan kecil.
// Bab 11, Aktivitas 11.1 dan Contoh Terhitung Bab 11.
//
// Kompilasi: g++ -std=c++17 -O2 -o diffie_hellman diffie_hellman.cpp
// Jalankan  : ./diffie_hellman   (Windows: diffie_hellman.exe)

#include <cstdio>
#include <vector>

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

// Kunci publik A = g^x mod p dari kunci privat x.
long long kunci_publik(long long g, long long x, long long p) {
    return pangkat_mod(g, x, p);
}

// Periksa apakah g membangkitkan seluruh 1..p-1 modulo p.
// Pangkat g^1, g^2, ... harus menghasilkan (p-1) nilai berbeda sebelum kembali
// ke 1. Cara memeriksa langsung ini hanya terjangkau untuk p kecil.
bool akar_primitif(long long g, long long p) {
    std::vector<bool> pernah(static_cast<std::size_t>(p), false);
    long long pangkat = 1;
    int jumlah = 0;
    for (long long i = 0; i < p - 1; i++) {
        pangkat = (pangkat * g) % p;
        if (!pernah[static_cast<std::size_t>(pangkat)]) {
            pernah[static_cast<std::size_t>(pangkat)] = true;
            jumlah++;
        }
    }
    return jumlah == p - 1;
}

// Jalankan satu pertukaran lengkap dan cetak setiap langkahnya.
void jalankan(long long p, long long g, long long a, long long b,
              const char* catatan) {
    std::printf("====================================================================\n");
    std::printf("%s\n", catatan);
    std::printf("====================================================================\n");

    if (!akar_primitif(g, p)) {
        std::printf("PERINGATAN: %lld bukan akar primitif dari %lld\n", g, p);
        return;
    }

    long long A = kunci_publik(g, a, p);
    long long B = kunci_publik(g, b, p);
    // Kunci bersama dihitung dari kunci publik lawan.
    long long K_alice = pangkat_mod(B, a, p);
    long long K_bob = pangkat_mod(A, b, p);

    std::printf("Parameter publik : p = %lld, g = %lld  (g akar primitif dari p)\n",
                p, g);
    std::printf("Kunci privat Alice a = %lld\n", a);
    std::printf("Kunci privat Bob   b = %lld\n\n", b);
    std::printf("Alice -> A = g^a mod p = %lld^%lld mod %lld = %lld\n", g, a, p, A);
    std::printf("Bob   -> B = g^b mod p = %lld^%lld mod %lld = %lld\n\n", g, b, p, B);
    std::printf("Alice menghitung K = B^a mod p = %lld^%lld mod %lld = %lld\n",
                B, a, p, K_alice);
    std::printf("Bob   menghitung K = A^b mod p = %lld^%lld mod %lld = %lld\n",
                A, b, p, K_bob);
    std::printf("Kedua kunci rahasia sama: %s (K = %lld)\n\n",
                K_alice == K_bob ? "true" : "false", K_alice);
}

int main() {
    jalankan(11, 7, 6, 9,
             "Contoh Terhitung Bab 11 (1): p = 11, g = 7, a = 6, b = 9");

    jalankan(353, 3, 97, 233,
             "Aktivitas 11.1: p = 353, g = 3, a = 97, b = 233");

    std::printf("Catatan keamanan:\n");
    std::printf("Semua nilai yang dipertukarkan (p, g, A, B) bersifat publik. "
                "Penyerang\n");
    std::printf("yang menyadapnya harus mencari a atau b dari A = g^a mod p, "
                "yaitu\n");
    std::printf("persoalan logaritma diskret. Untuk p = 353 persoalan itu dapat\n");
    std::printf("diselesaikan seketika; untuk p berukuran 2048 bit atau lebih, "
                "cara\n");
    std::printf("terbaik yang diketahui tetap tidak praktis. Karena itu p harus "
                "prima\n");
    std::printf("dan g harus akar primitif, supaya rentang nilai g^x mencakup "
                "seluruh\n");
    std::printf("grup dan tidak menyisakan celah yang mempermudah "
                "penyerangan.\n");
    return 0;
}
