"""Knapsack: verifikasi menyeluruh atas seluruh angka pada Bab 13.

Program ini menghitung ulang setiap angka yang muncul pada contoh
terhitung, tabel, dan latihan Bab 13, lalu memeriksanya satu per
satu. Bagian yang diuji meliputi:

  1. knapsack dasar non-superincreasing dan ambiguitas solusinya,
  2. dekripsi greedy pada barisan superincreasing,
  3. pembangkitan kunci publik dengan m = 105 dan n = 31,
  4. enkripsi dan dekripsi tiga blok pada parameter tersebut,
  5. prosedur lengkap Merkle-Hellman dengan m = 293 dan n = 37,
  6. kerapatan barisan bobot dan ambang serangan kisi,
  7. biaya penelusuran menyeluruh bagi barisan 250 elemen,
  8. ketidakcocokan parameter yang dianjurkan sumber,
  9. pemulihan kunci privat dari kunci publik,
 10. aktivitas praktikum dan latihan.

Jalankan: python knapsack_uji.py
Seluruh pengujian akan mencetak LULUS bila setiap angka cocok.
"""

import math


# ------------------------------------------------------------------
# 1. Perkakas bilangan dan barisan
# ------------------------------------------------------------------

def pbb(a, b):
    """Pembagi bersama terbesar dua bilangan."""
    while b:
        a, b = b, a % b
    return a


def invers(a, m):
    """Invers a modulo m, atau None bila tidak ada."""
    a %= m
    if pbb(a, m) != 1:
        return None
    lama_r, r = a, m
    lama_s, s = 1, 0
    while r:
        q = lama_r // r
        lama_r, r = r, lama_r - q * r
        lama_s, s = s, lama_s - q * s
    return lama_s % m


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


def superincreasing(w):
    """Benar bila setiap elemen melampaui jumlah semua elemen sebelumnya."""
    total = 0
    for x in w:
        if x <= total:
            return False
        total += x
    return True


def greedy(w, M):
    """Bit-bit pilihan w yang berjumlah M, atau None bila tak mungkin."""
    bits = [0] * len(w)
    sisa = M
    for i in range(len(w) - 1, -1, -1):
        if w[i] <= sisa:
            bits[i] = 1
            sisa -= w[i]
    return bits if sisa == 0 else None


def semua_solusi(w, M):
    """Seluruh vektor biner yang berjumlah M."""
    hasil = []
    for mask in range(1 << len(w)):
        jum = 0
        for i in range(len(w)):
            if mask >> i & 1:
                jum += w[i]
        if jum == M:
            hasil.append(mask)
    return hasil


def bits_dari(mask, n):
    """Ubah topeng menjadi rangkaian bit dari b1 sampai bn."""
    return "".join(str(mask >> i & 1) for i in range(n))


def ke_string(bits):
    """Ubah daftar bit (indeks 0 = b1) menjadi rangkaian bit."""
    return "".join(str(b) for b in bits)


def jumlah_bobot(pub, blok):
    """Kriptogram satu blok: jumlah elemen pub pada posisi bit 1."""
    return sum(w for w, b in zip(pub, blok) if b == "1")


def urai(biner, n):
    """Potong rangkaian bit menjadi blok sepanjang n bit."""
    sisa = len(biner) % n
    if sisa:
        biner = "0" * (n - sisa) + biner
    return [biner[i:i + n] for i in range(0, len(biner), n)]


def bangkitkan_kunci(w, m, n):
    """Barisan publik dari barisan privat: w'_i = (w_i * n) mod m."""
    return [(x * n) % m for x in w]


# ------------------------------------------------------------------
# 2. Contoh terhitung
# ------------------------------------------------------------------

def uji_knapsack_dasar():
    w = [1, 5, 6, 11, 14, 20]
    assert not superincreasing(w)
    biner = "111001010110000000011000"
    assert len(biner) == 24
    blok = urai(biner, 6)
    assert blok == ["111001", "010110", "000000", "011000"]
    C = [jumlah_bobot(w, b) for b in blok]
    assert C == [32, 30, 0, 11]
    sol = semua_solusi(w, 32)
    assert len(sol) == 3
    g = greedy(w, 32)
    assert g is not None and ke_string(g) != "111001"
    print("UJI 1 LULUS  knapsack dasar non-superincreasing:")
    print("             w = {}, bukan superincreasing".format(w))
    print("             blok {} -> kriptogram {}".format(blok, C))
    print("             M = 32 punya {} solusi: {}".format(
        len(sol), [bits_dari(s, 6) for s in sol]))
    print("             greedy justru memilih {} dari plainteks semula".format(
        ke_string(g)))


def uji_greedy_superincreasing():
    w = [2, 3, 6, 13, 27, 52]
    assert superincreasing(w)
    assert sum(w) == 103
    bits = greedy(w, 70)
    assert ke_string(bits) == "110101"
    assert sum(x for x, b in zip(w, bits) if b) == 70
    assert 70 - 2 != 0
    print("UJI 2 LULUS  dekripsi greedy barisan superincreasing:")
    print("             w = {}, jumlah seluruhnya {}".format(w, sum(w)))
    print("             M = 70 -> {} (2 + 3 + 13 + 52)".format(
        ke_string(bits)))
    print("             sisa akhir nol; b1 = 1, bukan 0 seperti sumber")


def uji_kunci_105():
    w = [2, 3, 6, 13, 27, 52]
    m, n = 105, 31
    assert m > sum(w)
    assert pbb(n, m) == 1
    inv = invers(n, m)
    assert inv == 61
    assert n * inv % m == 1
    pub = bangkitkan_kunci(w, m, n)
    assert pub == [62, 93, 81, 88, 102, 37]
    assert not superincreasing(pub)
    print("UJI 3 LULUS  pembangkitan kunci m = 105, n = 31:")
    print("             Wpriv = {} (jumlah {})".format(w, sum(w)))
    print("             Wpub  = {}".format(pub))
    print("             sifat superincreasing hilang dari Wpub")
    print("             n^-1 = {} karena {} * {} mod 105 = 1".format(
        inv, n, inv))


def uji_enkripsi_105():
    w = [2, 3, 6, 13, 27, 52]
    m, n = 105, 31
    pub = bangkitkan_kunci(w, m, n)
    inv = invers(n, m)
    biner = "011000110101101110"
    assert len(biner) == 18
    blok = urai(biner, 6)
    C = [jumlah_bobot(pub, b) for b in blok]
    assert C == [174, 280, 333]
    C_aksen = [(c * inv) % m for c in C]
    bak = [ke_string(greedy(w, r)) for r in C_aksen]
    assert C_aksen == [9, 70, 48]
    assert bak == ["011000", "110101", "101110"]
    assert "".join(bak) == biner
    assert C[1] > m and C[2] > m
    print("UJI 4 LULUS  enkripsi dan dekripsi tiga blok:")
    print("             plainteks {} (18 bit)".format(biner))
    print("             blok {} -> kriptogram {}".format(blok, C))
    print("             C * 61 mod 105 = {}".format(C_aksen))
    print("             greedy {} -> pulih".format(bak))
    print("             dua kriptogram melampaui m = 105, tetap sah")


def uji_parameter_293():
    w = [1, 2, 4, 9, 18, 36, 72, 144]
    assert superincreasing(w)
    assert sum(w) == 286
    m, n = 293, 37
    assert prima(m) and m > sum(w)
    assert pbb(n, m) == 1
    pub = bangkitkan_kunci(w, m, n)
    assert pub == [37, 74, 148, 40, 80, 160, 27, 54]
    assert not superincreasing(pub)
    inv = invers(n, m)
    assert inv == 198
    assert n * inv % m == 1
    C = [jumlah_bobot(pub, "10110010"), jumlah_bobot(pub, "01101001")]
    assert C == [252, 356]
    C_aksen = [(c * inv) % m for c in C]
    assert C_aksen == [86, 168]
    bak = [ke_string(greedy(w, r)) for r in C_aksen]
    assert bak == ["10110010", "01101001"]
    print("UJI 5 LULUS  prosedur lengkap m = 293, n = 37:")
    print("             Wpriv = {} (jumlah {})".format(w, sum(w)))
    print("             Wpub  = {}".format(pub))
    print("             n^-1 = {}; blok {} -> C = {}".format(
        inv, bak, C))
    print("             C * 198 mod 293 = {} -> pulih".format(C_aksen))
    print("             356 melampaui m = 293, tetap terdekripsi")


# ------------------------------------------------------------------
# 3. Kerapatan, parameter, dan keamanan
# ------------------------------------------------------------------

def uji_kerapatan():
    d_kecil = 6 / math.log(102, 2)
    assert abs(d_kecil - 0.8992) < 0.0001
    d_praktis = 100 / 299
    assert abs(d_praktis - 0.3344) < 0.0001
    assert d_praktis < 0.645 < 0.9408
    assert d_kecil > 0.645
    print("UJI 6 LULUS  kerapatan barisan dan ambang serangan kisi:")
    print("             barisan 6 elemen, terbesar 102 -> d = {:.4f}".format(
        d_kecil))
    print("             di atas ambang, jadi relatif aman")
    print("             MH praktis, 100 elemen 299 bit -> d = {:.4f}".format(
        d_praktis))
    print("             di bawah 0,645 Lagarias-Odlyzko dan 0,9408 Coster")


def uji_bruteforce():
    detik_setahun = 3600 * 24 * 365.25
    tahun = 2 ** 250 / 1e6 / detik_setahun
    assert 5.7e61 < tahun < 5.8e61
    percobaan = 10 ** 46 * detik_setahun * 1e6
    log2_percobaan = math.log(percobaan, 2)
    assert 197 < log2_percobaan < 199
    print("UJI 7 LULUS  biaya penelusuran menyeluruh:")
    print("             2^250 vektor pada 10^6 percobaan per detik")
    print("             waktu = {:.2e} tahun".format(tahun))
    print("             usia alam semesta hanya 1,4 * 10^10 tahun")
    print("             angka 10^46 tahun sepadan 2^{:.0f} percobaan".format(
        log2_percobaan))
    print("             yaitu barisan sekitar 200 elemen, bukan 250")


def uji_parameter_sumber():
    assert 250 * 2 ** 200 > 2 ** 201
    w = [2 ** 200 - 1]
    while len(w) < 100:
        w.append(sum(w) + 1)
    total = sum(w)
    assert superincreasing(w)
    assert total.bit_length() >= 299
    assert total.bit_length() > 200
    print("UJI 8 LULUS  ketidakcocokan parameter yang dianjurkan:")
    print("             sumber: 250 elemen 200-400 bit, m hanya 100-200 bit")
    print("             jumlah terkecil 250 elemen 200 bit sudah > 2^201,")
    print("             jadi m sependek itu mustahil melampaui jumlahnya")
    print("             barisan 100 elemen dari 200 bit:")
    print("             jumlahnya {} bit, sehingga m perlu >= 300 bit".format(
        total.bit_length()))


def uji_pembalik_kunci():
    for w, m, n in (([2, 3, 6, 13, 27, 52], 105, 31),
                    ([1, 2, 4, 9, 18, 36, 72, 144], 293, 37)):
        pub = bangkitkan_kunci(w, m, n)
        inv = invers(n, m)
        bak = [(x * inv) % m for x in pub]
        assert bak == w
        assert superincreasing(bak)
    print("UJI 9 LULUS  pemulihan kunci privat dari kunci publik:")
    print("             Wpub * n^-1 mod m mengembalikan Wpriv")
    print("             itulah jalan yang dipakai Shamir pada 1982")
    print("             kedua himpunan parameter berhasil dibalik")


# ------------------------------------------------------------------
# 4. Praktikum dan latihan
# ------------------------------------------------------------------

def uji_praktikum_latihan():
    w = [2, 3, 6, 13, 27, 52]
    m, n = 105, 31
    pub = bangkitkan_kunci(w, m, n)
    inv = invers(n, m)
    c = jumlah_bobot(pub, "011000")
    assert c == 174
    assert ke_string(greedy(w, c * inv % m)) == "011000"
    w8 = [1, 2, 4, 9, 18, 36, 72, 144]
    pub8 = bangkitkan_kunci(w8, 293, 37)
    c8 = jumlah_bobot(pub8, "10110010")
    assert c8 == 252
    assert ke_string(greedy(w8, c8 * invers(37, 293) % 293)) == "10110010"
    assert ke_string(greedy(w, 70)) == "110101"
    print("UJI 10 LULUS  praktikum dan latihan:")
    print("             Aktivitas 13.1: blok 011000 -> {} -> pulih".format(c))
    print("             Latihan: blok 10110010 -> {} -> pulih".format(c8))
    print("             Latihan: M = 70 -> 110101")


def main():
    print("=" * 70)
    print("VERIFIKASI SELURUH ANGKA PADA BAB 13")
    print("=" * 70)
    print()
    for uji in (uji_knapsack_dasar, uji_greedy_superincreasing,
                uji_kunci_105, uji_enkripsi_105, uji_parameter_293,
                uji_kerapatan, uji_bruteforce, uji_parameter_sumber,
                uji_pembalik_kunci, uji_praktikum_latihan):
        uji()
        print()
    print("=" * 70)
    print("Seluruh pengujian LULUS")
    print("=" * 70)


if __name__ == "__main__":
    main()
