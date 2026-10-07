"""Diffie-Hellman: verifikasi menyeluruh atas seluruh angka pada Bab 11.

Program ini menghitung ulang setiap angka yang muncul pada contoh terhitung,
tabel, dan latihan Bab 11, lalu memeriksanya satu per satu. Bagian yang diuji
meliputi:

  1. pemeriksaan akar primitif dan siklus pangkat modulo p,
  2. pertukaran kunci Diffie-Hellman dua pihak,
  3. contoh kecil, contoh p = 353, dan contoh perkakas daring N = 4789,
  4. serangan logaritma diskret dengan langkah raksasa-bayi,
  5. serangan man-in-the-middle beserta kedua kunci yang direbut,
  6. pertukaran kunci tiga pihak.

Jalankan: python dh_uji.py
Seluruh pengujian akan mencetak LULUS bila setiap angka cocok.
"""


# ------------------------------------------------------------------
# 1. Perkakas aritmetika modular
# ------------------------------------------------------------------

def pbb(a, b):
    """Pembagi bersama terbesar dengan Algoritma Euclidean."""
    while b:
        a, b = b, a % b
    return a


def prima(n):
    """Benar bila n bilangan prima."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def faktorisasi(n):
    """Kembalikan kamus faktor prima beserta pangkatnya."""
    hasil = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            hasil[d] = hasil.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        hasil[n] = hasil.get(n, 0) + 1
    return hasil


def siklus_pangkat(g, p):
    """Kembalikan daftar (e, g^e mod p) sampai nilainya kembali ke 1."""
    daftar = []
    x = 1
    e = 0
    while True:
        x = x * g % p
        e += 1
        daftar.append((e, x))
        if x == 1:
            return daftar


def orde(g, p):
    """Orde dari g modulo p, yaitu pangkat terkecil yang menghasilkan 1."""
    return len(siklus_pangkat(g, p))


def akar_primitif(g, p):
    """Benar bila g adalah akar primitif modulo p, yaitu berorde p - 1."""
    return 1 < g < p and prima(p) and orde(g, p) == p - 1


def daftar_akar_primitif(p):
    """Seluruh akar primitif modulo p."""
    return [g for g in range(2, p) if akar_primitif(g, p)]


# ------------------------------------------------------------------
# 2. Protokol pertukaran kunci Diffie-Hellman
# ------------------------------------------------------------------

def kunci_publik(g, a, p):
    """Kunci publik A = g^a mod p."""
    return pow(g, a, p)


def kunci_bersama(kunci_lawan, kunci_privat, p):
    """Kunci bersama K = (g^lawan)^privat mod p."""
    return pow(kunci_lawan, kunci_privat, p)


def pertukaran(g, p, a, b):
    """Jalankan pertukaran lengkap; kembalikan seluruh nilai antara."""
    A = kunci_publik(g, a, p)
    B = kunci_publik(g, b, p)
    return {
        "A": A,
        "B": B,
        "K_alice": kunci_bersama(B, a, p),
        "K_bob": kunci_bersama(A, b, p),
        "K_langsung": pow(g, a * b, p),
    }


def tiga_pihak(g, p, a, b, c):
    """Pertukaran melingkar tiga pihak; kembalikan ketiga jalur menuju K."""
    return {
        "via_carol": pow(pow(g, a * b, p), c, p),
        "via_alice": pow(pow(g, b * c, p), a, p),
        "via_bob": pow(pow(g, c * a, p), b, p),
        "K_langsung": pow(g, a * b * c, p),
    }


# ------------------------------------------------------------------
# 3. Serangan terhadap Diffie-Hellman
# ------------------------------------------------------------------

def langkah_raksasa_bayi(g, A, p):
    """Cari a dengan g^a = A (mod p) memakai langkah raksasa-bayi.

    Kembalikan (a, m, jumlah_perkalian) dengan m = ceil(sqrt(p - 1)).
    """
    m = 1
    while m * m < p - 1:
        m += 1

    tabel = {}
    x = 1
    for j in range(m):
        if x not in tabel:
            tabel[x] = j
        x = x * g % p

    g_pangkat_minus_m = pow(pow(g, m, p), p - 2, p)
    y = A
    for i in range(m):
        if y in tabel:
            return i * m + tabel[y], m, m + i
        y = y * g_pangkat_minus_m % p
    return None, m, m + m


def serang_mitm(g, p, a, b, m):
    """Serangan man-in-the-middle dengan kunci privat m milik penyerang."""
    A = kunci_publik(g, a, p)
    B = kunci_publik(g, b, p)
    M = kunci_publik(g, m, p)
    return {
        "A": A,
        "B": B,
        "M": M,
        "K1_alice": kunci_bersama(M, a, p),
        "K2_bob": kunci_bersama(M, b, p),
        "K1_mallory": kunci_bersama(A, m, p),
        "K2_mallory": kunci_bersama(B, m, p),
    }


# ------------------------------------------------------------------
# 4. Perkiraan keamanan menurut panjang modulus
# ------------------------------------------------------------------

def perkirakan_keamanan(bit):
    """Kembalikan perkiraan tingkat keamanan untuk modulus sepanjang bit."""
    if bit <= 512:
        return "kurang dari 64 bit; pernah dipecahkan pada TLS ekspor"
    if bit <= 1024:
        return "sekitar 80 bit; dalam jangkauan penyerang yang sangat kuat"
    if bit <= 2048:
        return "sekitar 112 bit; panjang minimum yang diterima hari ini"
    if bit <= 3072:
        return "sekitar 128 bit; untuk perlindungan jangka panjang"
    if bit <= 7680:
        return "sekitar 192 bit; setara AES-192"
    return "sekitar 256 bit; setara AES-256"


# ------------------------------------------------------------------
# Pengujian
# ------------------------------------------------------------------

def uji_parameter_kecil():
    print("UJI 1 LULUS  parameter p = 11:")
    print("             akar primitif modulo 11 = {}".format(
        daftar_akar_primitif(11)))
    siklus = siklus_pangkat(7, 11)
    print("             siklus g = 7 : {}".format(
        " ".join(str(x) for _, x in siklus)))
    print("             orde(7, 11) = {} = 11 - 1".format(orde(7, 11)))
    assert daftar_akar_primitif(11) == [2, 6, 7, 8]
    assert orde(7, 11) == 10
    assert [x for _, x in siklus] == [7, 5, 2, 3, 10, 4, 6, 9, 8, 1]
    assert akar_primitif(7, 11)
    assert not akar_primitif(3, 11)
    return siklus


def uji_bukan_akar_primitif():
    siklus = siklus_pangkat(3, 11)
    assert orde(3, 11) == 5
    assert len(set(x for _, x in siklus)) == 5
    # a = 6, 1, dan 11 semuanya memberi kunci publik yang sama.
    assert kunci_publik(3, 6, 11) == kunci_publik(3, 1, 11) == 3
    assert kunci_publik(3, 6, 11) == kunci_publik(3, 11, 11)
    print("UJI 2 LULUS  g = 3 bukan akar primitif dari 11:")
    print("             orde = {}, hanya {} kunci publik yang mungkin".format(
        orde(3, 11), orde(3, 11)))
    print("             a = 6, 1, 11 semuanya memberi A = 3")


def uji_contoh_kecil():
    h = pertukaran(7, 11, a=6, b=9)
    assert h["A"] == 4 and h["B"] == 8
    assert h["K_alice"] == h["K_bob"] == h["K_langsung"] == 3
    print("UJI 3 LULUS  p = 11, g = 7, a = 6, b = 9:")
    print("             A = 7^6 mod 11 = {}, B = 7^9 mod 11 = {}".format(
        h["A"], h["B"]))
    print("             K = 8^6 mod 11 = {} = 4^9 mod 11".format(h["K_alice"]))
    return h


def uji_contoh_353():
    assert prima(353)
    assert akar_primitif(3, 353)
    assert orde(3, 353) == 352
    h = pertukaran(3, 353, a=97, b=233)
    assert h["A"] == 40 and h["B"] == 248
    assert h["K_alice"] == h["K_bob"] == h["K_langsung"] == 160
    print("UJI 4 LULUS  p = 353, g = 3, a = 97, b = 233:")
    print("             3 adalah akar primitif 353, orde = {}".format(
        orde(3, 353)))
    print("             A = 3^97 mod 353 = {}, B = 3^233 mod 353 = {}".format(
        h["A"], h["B"]))
    print("             K = 248^97 = 40^233 = {} mod 353".format(h["K_alice"]))
    return h


def uji_langkah_raksasa_bayi():
    a, m, biaya = langkah_raksasa_bayi(3, 40, 353)
    assert a == 97, a
    assert m == 19, m
    assert biaya == m + 5, biaya
    print("UJI 5 LULUS  logaritma diskret dengan langkah raksasa-bayi:")
    print("             m = ceil(sqrt(352)) = {}".format(m))
    print("             a ditemukan = {} memakai {} perkalian,".format(a, biaya))
    print("             sedangkan pencarian menyeluruh memerlukan 97 langkah")


def uji_contoh_1601():
    assert prima(4789)
    assert akar_primitif(1601, 4789)
    assert orde(1601, 4789) == 4788
    h = pertukaran(1601, 4789, a=20, b=4)
    assert h["A"] == 2716, h["A"]
    assert h["B"] == 1302, h["B"]
    assert h["K_alice"] == h["K_bob"] == 4257
    print("UJI 6 LULUS  perkakas daring, G = 1601, N = 4789:")
    print("             4789 prima; orde(1601) = 4788 = N - 1")
    print("             A = 1601^20 mod 4789 = {}".format(h["A"]))
    print("             B = 1601^4  mod 4789 = {}".format(h["B"]))
    print("             K = 1302^20 = 2716^4 = {} mod 4789".format(
        h["K_alice"]))
    return h


def uji_serangan_mitm():
    h = serang_mitm(3, 353, a=97, b=233, m=101)
    assert h["A"] == 40 and h["B"] == 248
    assert h["M"] == 63, h["M"]
    assert h["K1_alice"] == h["K1_mallory"] == 257
    assert h["K2_bob"] == h["K2_mallory"] == 249
    assert h["K1_alice"] != h["K2_bob"]
    print("UJI 7 LULUS  serangan man-in-the-middle, m = 101:")
    print("             M = 3^101 mod 353 = {}".format(h["M"]))
    print("             Alice  : K1 = 63^97  = 40^101  = {}".format(
        h["K1_alice"]))
    print("             Bob    : K2 = 63^233 = 248^101 = {}".format(
        h["K2_bob"]))
    print("             K1 != K2, sehingga kedua arah dapat dipisahkan")


def uji_tiga_pihak():
    h = tiga_pihak(3, 353, a=97, b=233, c=41)
    assert h["via_carol"] == h["via_alice"] == h["via_bob"] == 350
    assert h["K_langsung"] == 350
    print("UJI 8 LULUS  pertukaran kunci tiga pihak, c = 41:")
    print("             Carol : (g^ab)^c = {}".format(h["via_carol"]))
    print("             Alice : (g^bc)^a = {}".format(h["via_alice"]))
    print("             Bob   : (g^ca)^b = {}".format(h["via_bob"]))
    print("             K = g^abc mod 353 = {}".format(h["K_langsung"]))


def uji_latihan():
    # Latihan: p = 23, g = 5, a = 7, b = 15.
    assert prima(23) and orde(5, 23) == 22
    h = pertukaran(5, 23, a=7, b=15)
    assert h["A"] == pow(5, 7, 23)
    assert h["K_alice"] == h["K_bob"]
    print("UJI 9 LULUS  latihan p = 23, g = 5, a = 7, b = 15:")
    print("             A = 5^7 mod 23  = {}".format(h["A"]))
    print("             B = 5^15 mod 23 = {}".format(h["B"]))
    print("             K = {} = {}".format(h["K_alice"], h["K_bob"]))


def uji_perkiraan_keamanan():
    harapan = {512: "kurang dari 64 bit", 1024: "80 bit",
               2048: "112 bit", 3072: "128 bit",
               7680: "192 bit", 15360: "256 bit"}
    for bit, potongan in harapan.items():
        teks = perkirakan_keamanan(bit)
        assert potongan in teks, (bit, teks)
    print("UJI 10 LULUS  perkiraan keamanan menurut panjang modulus:")
    for bit in (512, 1024, 2048, 3072, 7680, 15360):
        print("             {:>5} bit: {}".format(bit, perkirakan_keamanan(bit)))


def main():
    print("=" * 70)
    print("VERIFIKASI SELURUH ANGKA PADA BAB 11")
    print("=" * 70)

    uji_parameter_kecil()
    print()
    uji_bukan_akar_primitif()
    print()
    uji_contoh_kecil()
    print()
    uji_contoh_353()
    print()
    uji_langkah_raksasa_bayi()
    print()
    uji_contoh_1601()
    print()
    uji_serangan_mitm()
    print()
    uji_tiga_pihak()
    print()
    uji_latihan()
    print()
    uji_perkiraan_keamanan()
    print()
    print("=" * 70)
    print("Seluruh pengujian LULUS")
    print("=" * 70)


if __name__ == "__main__":
    main()
