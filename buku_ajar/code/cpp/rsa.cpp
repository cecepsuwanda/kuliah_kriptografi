// RSA: pembangkitan kunci, enkripsi, dan dekripsi dengan bilangan prima kecil.
// Bab 10, Aktivitas 10.1 dan Contoh Terhitung Bab 10.
//
// Kompilasi: g++ -std=c++17 -O2 -o rsa rsa.cpp
// Jalankan  : ./rsa   (Windows: rsa.exe)

#include <cstdio>
#include <stdexcept>

// Pembagi bersama terbesar dengan Algoritma Euclidean.
long long pbb(long long a, long long b) {
    while (b != 0) {
        long long sisa = a % b;
        a = b;
        b = sisa;
    }
    return a;
}

// Cari d sehingga e * d = 1 (mod phi) dengan Algoritma Euclidean diperluas.
long long invers_modulo(long long e, long long phi) {
    long long lama_d = 0, d = 1;
    long long lama_phi = phi, sisa = e;
    while (sisa != 0) {
        long long hasil_bagi = lama_phi / sisa;
        long long d_baru = lama_d - hasil_bagi * d;
        long long sisa_baru = lama_phi - hasil_bagi * sisa;
        lama_d = d;
        d = d_baru;
        lama_phi = sisa;
        sisa = sisa_baru;
    }
    if (lama_phi != 1) {
        throw std::invalid_argument("e tidak relatif prima terhadap phi(n)");
    }
    return ((lama_d % phi) + phi) % phi;
}

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

// Kembalikan n, phi, dan d untuk dua prima p, q dan eksponen publik e.
void bangkitkan_kunci(long long p, long long q, long long e,
                      long long& n, long long& phi, long long& d) {
    n = p * q;
    phi = (p - 1) * (q - 1);
    if (!(e > 1 && e < phi) || pbb(e, phi) != 1) {
        throw std::invalid_argument(
            "e harus memenuhi 1 < e < phi(n) dan PBB(e, phi(n)) = 1");
    }
    d = invers_modulo(e, phi);
}

// Jalankan satu siklus RSA lengkap dan cetak setiap langkahnya.
void jalankan(long long p, long long q, long long e, long long m,
              const char* catatan) {
    std::printf("====================================================================\n");
    std::printf("%s\n", catatan);
    std::printf("====================================================================\n");

    long long n, phi, d;
    bangkitkan_kunci(p, q, e, n, phi, d);

    long long c = pangkat_mod(m, e, n);      // enkripsi
    long long m_pulih = pangkat_mod(c, d, n);  // dekripsi

    std::printf("p = %lld, q = %lld\n", p, q);
    std::printf("n = p * q           = %lld\n", n);
    std::printf("phi(n) = (p-1)(q-1) = %lld\n", phi);
    std::printf("Kunci publik  (e, n) = (%lld, %lld)\n", e, n);
    std::printf("Kunci privat  (d, n) = (%lld, %lld)\n", d, n);
    std::printf("Periksa e * d mod phi(n) = %lld\n\n", (e * d) % phi);
    std::printf("Plainteks  m = %lld\n", m);
    std::printf("Enkripsi   c = m^e mod n = %lld^%lld mod %lld = %lld\n",
                m, e, n, c);
    std::printf("Dekripsi   m = c^d mod n = %lld^%lld mod %lld = %lld\n",
                c, d, n, m_pulih);
    std::printf("Pesan pulih dengan tepat: %s\n\n",
                m_pulih == m ? "true" : "false");
}

int main() {
    // Kasus 1: parameter kecil dari Aktivitas 10.1, dipakai untuk memeriksa
    // setiap langkah secara manual tanpa alat bantu.
    jalankan(3, 11, 3, 5,
             "Aktivitas 10.1: p = 3, q = 11, e = 3, m = 5");

    // Kasus 2: parameter pada Contoh Terhitung Bab 10.
    jalankan(47, 71, 79, 16,
             "Contoh Terhitung Bab 10: p = 47, q = 71, e = 79, m = 16");

    std::printf("Catatan keamanan:\n");
    std::printf("Pada kedua kasus di atas, n dapat difaktorkan hanya dalam "
                "hitungan\n");
    std::printf("detik, sehingga kunci privat dapat ditemukan. RSA yang dipakai\n");
    std::printf("sehari-hari menggunakan n minimal 2048 bit, yaitu sekitar 617\n");
    std::printf("digit, yang membuat pemfaktoran menjadi tidak praktis.\n");
    return 0;
}
