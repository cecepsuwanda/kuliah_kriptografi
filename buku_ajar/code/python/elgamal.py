"""ElGamal: pembangkitan kunci, enkripsi, dan dekripsi pada bilangan kecil.

Sesuai Aktivitas 12.1 dan Contoh Terhitung Bab 12: p = 2273, g = 3, kunci
privat x = 243, pesan m = 700, kunci efemeral k = 1463. Satu kasus tambahan
dengan parameter aktivitas (p = 2357, g = 2) dijalankan sebagai pembanding.

Jalankan: python elgamal.py
"""


def kunci_publik(g, x, p):
    """y = g^x mod p."""
    return pow(g, x, p)


def enkripsi(m, y, g, p, k):
    """Kembalikan pasangan cipherteks (a, b).

    a = g^k mod p, dan b = y^k * m mod p. Nilai k harus dipilih acak dan
    berbeda untuk setiap pesan.
    """
    if not 0 <= m < p:
        raise ValueError("Pesan m harus berada pada selang [0, p-1]")
    a = pow(g, k, p)
    b = (pow(y, k, p) * m) % p
    return a, b


def dekripsi(a, b, x, p):
    """Kembalikan plainteks m = b * (a^x)^-1 mod p.

    Invers a^x dihitung sebagai a^(p-1-x) mod p, karena a^(p-1) = 1 (mod p)
    menurut Teorema Kecil Fermat.
    """
    invers_a_x = pow(a, p - 1 - x, p)
    return (b * invers_a_x) % p


def jalankan(p, g, x, m, k, catatan):
    """Jalankan satu siklus ElGamal lengkap dan cetak setiap langkahnya."""
    print("=" * 68)
    print(catatan)
    print("=" * 68)

    y = kunci_publik(g, x, p)
    a, b = enkripsi(m, y, g, p, k)
    m_pulih = dekripsi(a, b, x, p)

    print(f"Parameter publik : p = {p}, g = {g}")
    print(f"Kunci privat Bob : x = {x}")
    print(f"Kunci publik Bob : y = g^x mod p = {g}^{x} mod {p} = {y}")
    print()
    print(f"Pesan       m = {m}")
    print(f"Kunci acak  k = {k}")
    print(f"a = g^k mod p     = {g}^{k} mod {p} = {a}")
    print(f"b = y^k * m mod p = {y}^{k} * {m} mod {p} = {b}")
    print(f"Cipherteks  (a, b) = ({a}, {b})")
    print()
    print(f"Dekripsi m = b * (a^x)^-1 mod p = {m_pulih}")
    print(f"Pesan pulih dengan tepat: {m_pulih == m}")
    print()


if __name__ == "__main__":
    jalankan(p=2273, g=3, x=243, m=700, k=1463,
             catatan="Contoh Terhitung Bab 12: p = 2273, g = 3, x = 243")

    jalankan(p=2357, g=2, x=1751, m=2035, k=1520,
             catatan="Aktivitas 12.1: p = 2357, g = 2, x = 1751")

    print("Catatan keamanan:")
    print("Ukuran cipherteks ElGamal dua kali ukuran plainteks, karena tiap")
    print("pesan menghasilkan pasangan (a, b). Keamanannya bersandar pada")
    print("persoalan logaritma diskret: penyerang yang melihat y, g, dan p")
    print("harus mencari x. Selain itu, k harus dipilih acak dan tidak boleh")
    print("digunakan ulang; memakai k yang sama untuk dua pesan membuat rasio")
    print("kedua cipherteks membuka perbandingan plainteksnya.")
