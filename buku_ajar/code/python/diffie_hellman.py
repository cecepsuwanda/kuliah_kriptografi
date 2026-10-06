"""Pertukaran kunci Diffie-Hellman pada bilangan kecil.

Sesuai Aktivitas 11.1 dan kedua Contoh Terhitung Bab 11: satu kasus dengan
p = 11, g = 7 untuk diperiksa tangan, dan satu kasus dengan p = 353, g = 3.

Jalankan: python diffie_hellman.py
"""


def akar_primitif(g, p):
    """Periksa apakah g membangkitkan seluruh 1..p-1 modulo p.

    Pangkat g^1, g^2, ... harus menghasilkan (p-1) nilai berbeda sebelum
    kembali ke 1. Cara memeriksa langsung ini hanya terjangkau untuk p kecil.
    """
    nilai = set()
    pangkat = 1
    for _ in range(p - 1):
        pangkat = (pangkat * g) % p
        nilai.add(pangkat)
    return len(nilai) == p - 1


def kunci_publik(g, x, p):
    """Kunci publik A = g^x mod p dari kunci privat x."""
    return pow(g, x, p)


def kunci_rahasia(kunci_publik_lawan, x, p):
    """Kunci bersama K = B^x mod p (dihitung dari kunci publik lawan)."""
    return pow(kunci_publik_lawan, x, p)


def jalankan(p, g, a, b, catatan):
    """Jalankan satu pertukaran lengkap dan cetak setiap langkahnya."""
    print("=" * 68)
    print(catatan)
    print("=" * 68)

    if not akar_primitif(g, p):
        print(f"PERINGATAN: {g} bukan akar primitif dari {p}")
        return

    A = kunci_publik(g, a, p)
    B = kunci_publik(g, b, p)
    K_alice = kunci_rahasia(B, a, p)
    K_bob = kunci_rahasia(A, b, p)

    print(f"Parameter publik : p = {p}, g = {g}  (g akar primitif dari p)")
    print(f"Kunci privat Alice a = {a}")
    print(f"Kunci privat Bob   b = {b}")
    print()
    print(f"Alice -> A = g^a mod p = {g}^{a} mod {p} = {A}")
    print(f"Bob   -> B = g^b mod p = {g}^{b} mod {p} = {B}")
    print()
    print(f"Alice menghitung K = B^a mod p = {B}^{a} mod {p} = {K_alice}")
    print(f"Bob   menghitung K = A^b mod p = {A}^{b} mod {p} = {K_bob}")
    print(f"Kedua kunci rahasia sama: {K_alice == K_bob} (K = {K_alice})")
    print()


if __name__ == "__main__":
    jalankan(p=11, g=7, a=6, b=9,
             catatan="Contoh Terhitung Bab 11 (1): p = 11, g = 7, a = 6, b = 9")

    jalankan(p=353, g=3, a=97, b=233,
             catatan="Aktivitas 11.1: p = 353, g = 3, a = 97, b = 233")

    print("Catatan keamanan:")
    print("Semua nilai yang dipertukarkan (p, g, A, B) bersifat publik. Penyerang")
    print("yang menyadapnya harus mencari a atau b dari A = g^a mod p, yaitu")
    print("persoalan logaritma diskret. Untuk p = 353 persoalan itu dapat")
    print("diselesaikan seketika; untuk p berukuran 2048 bit atau lebih, cara")
    print("terbaik yang diketahui tetap tidak praktis. Karena itu p harus prima")
    print("dan g harus akar primitif, supaya rentang nilai g^x mencakup seluruh")
    print("grup dan tidak menyisakan celah yang mempermudah penyerangan.")
