"""ElGamal: verifikasi menyeluruh atas seluruh angka pada Bab 12.

Program ini menghitung ulang setiap angka yang muncul pada contoh
terhitung, tabel, dan latihan Bab 12, lalu memeriksanya satu per
satu. Bagian yang diuji meliputi:

  1. akar primitif dan siklus pangkat modulo p,
  2. pembangkitan pasangan kunci pada dua himpunan parameter,
  3. enkripsi dan dekripsi satu blok,
  4. pesan multi-blok "HALO" dengan dua kunci efemeral berbeda,
  5. sifat enkripsi probabilistik,
  6. sifat homomorfik multiplikatif,
  7. invers modulo dengan Teorema Kecil Fermat,
  8. pembongkaran pesan karena kunci efemeral dipakai ulang,
  9. parameter kedua p = 2357 beserta jejak salah cetak 2353,
 10. aktivitas praktikum dan latihan.

Jalankan: python elgamal_uji.py
Seluruh pengujian akan mencetak LULUS bila setiap angka cocok.
"""


# ------------------------------------------------------------------
# 1. Perkakas aritmetika modular
# ------------------------------------------------------------------

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


def siklus_pangkat(g, p):
    """Daftar (e, g^e mod p) sampai nilainya kembali menjadi 1."""
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
    """Orde dari g modulo p, yaitu pangkat terkecil yang hasilnya 1."""
    return len(siklus_pangkat(g, p))


def akar_primitif(g, p):
    """Benar bila g berorde p - 1, yaitu akar primitif modulo p."""
    return 1 < g < p and prima(p) and orde(g, p) == p - 1


def phi(n):
    """Fungsi totient Euler."""
    return sum(1 for k in range(1, n + 1) if pbb(k, n) == 1)


def pbb(a, b):
    """Pembagi bersama terbesar dengan Algoritma Euclidean."""
    while b:
        a, b = b, a % b
    return a


def invers_fermat(a, x, p):
    """Invers dari a^x modulo p lewat a^(p-1-x), sesuai bab."""
    return pow(a, p - 1 - x, p)


def bangkitkan_kunci(p, g, x):
    """Kembalikan kunci publik (y, g, p) dari kunci privat x."""
    assert akar_primitif(g, p), "g bukan akar primitif dari p"
    assert 2 <= x <= p - 2, "x di luar selang 2 <= x <= p - 2"
    return (pow(g, x, p), g, p)


def enkripsi(kunci_publik, m, k):
    """Enkripsi satu blok m dengan kunci efemeral k."""
    y, g, p = kunci_publik
    assert 0 <= m <= p - 1, "blok pesan harus lebih kecil dari modulus"
    assert 1 <= k <= p - 2, "k di luar selang 1 <= k <= p - 2"
    return (pow(g, k, p), pow(y, k, p) * m % p)


def dekripsi(kunci_publik, kunci_privat, c):
    """Dekripsi pasangan (a, b) dengan kunci privat x."""
    _, _, p = kunci_publik
    x = kunci_privat
    a, b = c
    return b * invers_fermat(a, x, p) % p


def dari_kode(teks):
    """Ubah huruf A-Z menjadi rangkaian dua digit, A = 00, Z = 25."""
    return "".join("{:02d}".format(ord(h) - ord("A")) for h in teks)


def ke_kode(rangkaian, panjang=4):
    """Potong rangkaian digit menjadi blok sepanjang panjang digit."""
    sisa = len(rangkaian) % panjang
    if sisa:
        rangkaian = "0" * (panjang - sisa) + rangkaian
    return [int(rangkaian[i:i + panjang])
            for i in range(0, len(rangkaian), panjang)]


# ------------------------------------------------------------------
# 2. Pengujian
# ------------------------------------------------------------------

def uji_akar_primitif():
    siklus3 = [v for _, v in siklus_pangkat(3, 7)]
    siklus2 = [v for _, v in siklus_pangkat(2, 7)]
    assert siklus3 == [3, 2, 6, 4, 5, 1]
    assert siklus2 == [2, 4, 1]
    assert siklus2 * 2 == [2, 4, 1, 2, 4, 1]
    assert akar_primitif(3, 7)
    assert not akar_primitif(2, 7)
    assert orde(3, 7) == 6 and orde(2, 7) == 3
    assert pow(7, 3, 41) == 15
    assert akar_primitif(7, 41)
    assert phi(6) == 2 and phi(40) == 16
    print("UJI 1 LULUS  akar primitif modulo 7:")
    print("             a = 3 -> {} (panjang 6)".format(siklus3))
    print("             a = 2 -> {} berulang (panjang 3)".format(siklus2))
    print("             7^3 mod 41 = 15, phi(6) = 2, phi(40) = 16")


def uji_kunci():
    assert prima(2273) and akar_primitif(3, 2273)
    y, g, p = bangkitkan_kunci(2273, 3, 243)
    assert y == 461
    print("UJI 2 LULUS  pembangkitan kunci, p = 2273, g = 3:")
    print("             ord(3, 2273) = {}".format(orde(3, 2273)))
    print("             y = 3^243 mod 2273 = {}".format(y))


def uji_enkripsi_dekripsi():
    kp = bangkitkan_kunci(2273, 3, 243)
    c = enkripsi(kp, 700, 1463)
    assert c == (1439, 74)
    inv = invers_fermat(c[0], 243, 2273)
    assert inv == 1791
    assert dekripsi(kp, 243, c) == 700
    print("UJI 3 LULUS  enkripsi dan dekripsi satu blok:")
    print("             m = 700, k = 1463 -> (a, b) = {}".format(c))
    print("             (a^x)^(-1) = 1439^2029 mod 2273 = {}".format(inv))
    print("             m = 74 * 1791 mod 2273 = {}".format(
        dekripsi(kp, 243, c)))


def uji_multi_blok():
    kp = bangkitkan_kunci(2273, 3, 243)
    kode = dari_kode("HALO")
    assert kode == "07001114"
    blok = ke_kode(kode)
    assert blok == [700, 1114]
    kunci_efemeral = [1463, 2001]
    c1 = enkripsi(kp, blok[0], kunci_efemeral[0])
    c2 = enkripsi(kp, blok[1], kunci_efemeral[1])
    assert c1 == (1439, 74)
    assert c2 == (1220, 1682)
    assert dekripsi(kp, 243, c1) == 700
    assert dekripsi(kp, 243, c2) == 1114
    assert c1[0] != c2[0], "kunci efemeral harus berbeda"
    print("UJI 4 LULUS  pesan multi-blok \"HALO\":")
    print("             H=07 A=00 L=11 O=14 -> m = {}".format(kode))
    print("             blok {} dengan k = {}".format(blok,
                                                       kunci_efemeral))
    print("             c1 = {}  c2 = {}".format(c1, c2))
    print("             dekripsi -> {} = \"HALO\"".format(kode))


def uji_probabilistik():
    kp = bangkitkan_kunci(2273, 3, 243)
    hasil = [enkripsi(kp, 700, k) for k in (1463, 2001, 300)]
    assert len({a for a, _ in hasil}) == 3
    assert len(set(hasil)) == 3
    for c in hasil:
        assert dekripsi(kp, 243, c) == 700
    print("UJI 5 LULUS  enkripsi probabilistik, m = 700 diulang:")
    for k, c in zip((1463, 2001, 300), hasil):
        print("             k = {:>4} -> {}".format(k, c))
    print("             tiga cipherteks berbeda, plainteksnya sama")


def uji_homomorfik():
    kp = bangkitkan_kunci(2273, 3, 243)
    c1 = enkripsi(kp, 700, 1463)
    c2 = enkripsi(kp, 1114, 2001)
    gabungan = (c1[0] * c2[0] % 2273, c1[1] * c2[1] % 2273)
    assert dekripsi(kp, 243, gabungan) == 700 * 1114 % 2273
    assert 700 * 1114 % 2273 == 161
    print("UJI 6 LULUS  sifat homomorfik multiplikatif:")
    print("             c1 = {}  c2 = {}".format(c1, c2))
    print("             hasil kali = {}".format(gabungan))
    print("             dekripsi = 700*1114 mod 2273 = 161")
    print("             (bukan 779800, sebab perkaliannya modulo p)")


def uji_invers_fermat():
    p = 2273
    for a in (1439, 1220, 74, 2):
        x = 243
        kali = pow(a, x, p) * invers_fermat(a, x, p) % p
        assert kali == 1
    assert invers_fermat(1439, 243, 2273) == 1791
    assert invers_fermat(1220, 243, 2273) == 1125
    print("UJI 7 LULUS  invers lewat Teorema Kecil Fermat:")
    for a in (1439, 1220):
        print("             {}^243 * {}^{} mod 2273 = 1".format(
            a, a, 2273 - 1 - 243))
    print("             (a^x)^(-1) = a^(p-1-x), tanpa algoritma Euclidean")


def uji_k_ulang():
    kp = bangkitkan_kunci(2273, 3, 243)
    k = 1463
    c1 = enkripsi(kp, 700, k)
    c2 = enkripsi(kp, 1114, k)
    assert c1[0] == c2[0] == 1439, "komponen pertama harus sama"
    assert c1[1] == 74 and c2[1] == 988
    rasio = c1[1] * pow(c2[1], -1, 2273) % 2273
    assert rasio == 474
    assert rasio == 700 * pow(1114, -1, 2273) % 2273
    m2 = 700 * c2[1] * pow(c1[1], -1, 2273) % 2273
    assert m2 == 1114
    yk = c1[1] * pow(700, -1, 2273) % 2273
    assert yk == pow(461, 1463, 2273)
    print("UJI 8 LULUS  kunci efemeral dipakai ulang, k = {}:".format(k))
    print("             c1 = {}  c2 = {}".format(c1, c2))
    print("             a1 = a2 = {}, jadi k sama".format(c1[0]))
    print("             b1/b2 = 74/988 = {}".format(rasio))
    print("             m1/m2 = 700/1114 = {} (cocok)".format(rasio))
    print("             m2 = m1 * b2 * b1^(-1) = {}".format(m2))
    print("             y^k = b1 * m1^(-1) = {} (bocor)".format(yk))


def uji_parameter_2357():
    assert prima(2357) and akar_primitif(2, 2357)
    assert orde(2, 2357) == 2356
    kp = bangkitkan_kunci(2357, 2, 1751)
    assert kp[0] == 1185
    c = enkripsi(kp, 2035, 1520)
    assert c == (1430, 697)
    inv = invers_fermat(c[0], 1751, 2357)
    assert inv == 872
    assert dekripsi(kp, 1751, c) == 2035
    assert pow(2, 1751, 2353) == 1008
    print("UJI 9 LULUS  parameter kedua, p = 2357, g = 2:")
    print("             ord(2, 2357) = {}".format(orde(2, 2357)))
    print("             x = 1751 -> y = 2^1751 mod 2357 = {}".format(kp[0]))
    print("             m = 2035, k = 1520 -> (a, b) = {}".format(c))
    print("             m = 697 * 872 mod 2357 = {}".format(
        dekripsi(kp, 1751, c)))
    print("             jejak salah cetak: 2^1751 mod 2353 = 1008, "
          "bukan 1185")


def uji_praktikum_latihan():
    kp = bangkitkan_kunci(2357, 2, 1751)
    assert bangkitkan_kunci(2357, 2, 1751)[0] == 1185
    c = enkripsi(kp, 2035, 1520)
    assert dekripsi(kp, 1751, c) == 2035
    # Latihan: p = 2357, g = 2, x = 900, m = 1234, k = 1000.
    kp2 = bangkitkan_kunci(2357, 2, 900)
    c2 = enkripsi(kp2, 1234, 1000)
    assert dekripsi(kp2, 900, c2) == 1234
    print("UJI 10 LULUS  praktikum dan latihan:")
    print("             Aktivitas 12.1: y = {}, (a, b) = {}".format(
        kp[0], c))
    print("             dekripsi = 2035")
    print("             Latihan: x = 900 -> y = {}, c = {}".format(
        kp2[0], c2))
    print("             dekripsi = 1234")


def main():
    print("=" * 70)
    print("VERIFIKASI SELURUH ANGKA PADA BAB 12")
    print("=" * 70)
    print()
    for uji in (uji_akar_primitif, uji_kunci, uji_enkripsi_dekripsi,
                uji_multi_blok, uji_probabilistik, uji_homomorfik,
                uji_invers_fermat, uji_k_ulang, uji_parameter_2357,
                uji_praktikum_latihan):
        uji()
        print()
    print("=" * 70)
    print("Seluruh pengujian LULUS")
    print("=" * 70)


if __name__ == "__main__":
    main()
