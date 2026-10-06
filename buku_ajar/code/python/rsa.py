"""RSA: pembangkitan kunci, enkripsi, dan dekripsi dengan bilangan prima kecil.

Sesuai Aktivitas 10.1 dan Contoh Terhitung Bab 10. Dua kasus dijalankan:
parameter kecil p = 3, q = 11 dari aktivitas, dan parameter p = 47, q = 71
yang dipakai pada contoh terhitung buku.

Jalankan: python rsa.py
"""


def pbb(a, b):
    """Pembagi bersama terbesar dengan Algoritma Euclidean."""
    while b:
        a, b = b, a % b
    return a


def invers_modulo(e, phi):
    """Cari d sehingga e * d = 1 (mod phi) dengan Algoritma Euclidean diperluas."""
    lama_d, d = 0, 1
    lama_phi, phi_sisa = phi, e
    while phi_sisa:
        hasil_bagi = lama_phi // phi_sisa
        lama_d, d = d, lama_d - hasil_bagi * d
        lama_phi, phi_sisa = phi_sisa, lama_phi - hasil_bagi * phi_sisa
    if lama_phi != 1:
        raise ValueError("e tidak relatif prima terhadap phi(n); invers tidak ada")
    return lama_d % phi


def bangkitkan_kunci(p, q, e):
    """Kembalikan (n, phi, d) untuk dua prima p, q dan eksponen publik e."""
    n = p * q
    phi = (p - 1) * (q - 1)
    if not 1 < e < phi or pbb(e, phi) != 1:
        raise ValueError("e harus memenuhi 1 < e < phi(n) dan PBB(e, phi(n)) = 1")
    return n, phi, invers_modulo(e, phi)


def enkripsi(m, e, n):
    """c = m^e mod n."""
    return pow(m, e, n)


def dekripsi(c, d, n):
    """m = c^d mod n."""
    return pow(c, d, n)


def jalankan(p, q, e, m, catatan):
    """Jalankan satu siklus RSA lengkap dan cetak setiap langkahnya."""
    print("=" * 68)
    print(catatan)
    print("=" * 68)

    n, phi, d = bangkitkan_kunci(p, q, e)
    c = enkripsi(m, e, n)
    m_pulih = dekripsi(c, d, n)

    print(f"p = {p}, q = {q}")
    print(f"n = p * q          = {n}")
    print(f"phi(n) = (p-1)(q-1) = {phi}")
    print(f"Kunci publik  (e, n) = ({e}, {n})")
    print(f"Kunci privat  (d, n) = ({d}, {n})")
    print(f"Periksa e * d mod phi(n) = {(e * d) % phi}")
    print()
    print(f"Plainteks  m = {m}")
    print(f"Enkripsi   c = m^e mod n = {m}^{e} mod {n} = {c}")
    print(f"Dekripsi   m = c^d mod n = {c}^{d} mod {n} = {m_pulih}")
    print(f"Pesan pulih dengan tepat: {m_pulih == m}")
    print()


if __name__ == "__main__":
    # Kasus 1: parameter kecil dari Aktivitas 10.1, dipakai untuk memeriksa
    # setiap langkah secara manual tanpa alat bantu.
    jalankan(p=3, q=11, e=3, m=5,
             catatan="Aktivitas 10.1: p = 3, q = 11, e = 3, m = 5")

    # Kasus 2: parameter pada Contoh Terhitung Bab 10.
    jalankan(p=47, q=71, e=79, m=16,
             catatan="Contoh Terhitung Bab 10: p = 47, q = 71, e = 79, m = 16")

    print("Catatan keamanan:")
    print("Pada kedua kasus di atas, n dapat difaktorkan hanya dalam hitungan")
    print("detik, sehingga kunci privat dapat ditemukan. RSA yang dipakai")
    print("sehari-hari menggunakan n minimal 2048 bit, yaitu sekitar 617")
    print("digit, yang membuat pemfaktoran menjadi tidak praktis.")
