# ------------------------------------------------------------------
# ecc_uji.py -- verifikasi angka Bab 14 (Kriptografi Kurva Eliptik)
# ------------------------------------------------------------------
# Seluruh nilai yang tercantum pada bab diuji ulang di sini: aritmetika
# polinomial GF(2^m), medan berhingga GF(p), penjumlahan dan penggandaan
# titik, enumerasi kurva, pertukaran kunci ECDH, enkripsi ECEG, metode
# Koblitz, dan penyerangan logaritma diskrit dengan baby-step giant-step.
#
# Jalankan: python ecc_uji.py
# ------------------------------------------------------------------

from fractions import Fraction


# ------------------------------------------------------------------
# Bagian 1: aritmetika bilangan bulat dan medan berhingga
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


def akar_kuadrat(v, p):
    """Seluruh akar kuadrat v modulo p (kosong bila v bukan kuadrat)."""
    return [y for y in range(p) if (y * y - v) % p == 0]


# ------------------------------------------------------------------
# Bagian 2: aritmetika polinomial di dalam GF(2^m)
# ------------------------------------------------------------------


def polinom_tambah(a, b):
    """Penjumlahan di GF(2^m): sama dengan operasi XOR bit demi bit."""
    return a ^ b


def polinom_kali(a, b, reduksi, m):
    """Perkalian di GF(2^m), hasilnya direduksi oleh polinom reduksi."""
    hasil = 0
    while b:
        if b & 1:
            hasil ^= a
        b >>= 1
        a <<= 1
        if a >> m & 1:
            a ^= reduksi
    return hasil & ((1 << m) - 1)


def polinom_bagi(a, b):
    """Bagi polinom a dengan polinom b; kembalikan (hasil bagi, sisa)."""
    hasil = 0
    while a and a.bit_length() >= b.bit_length():
        geser = a.bit_length() - b.bit_length()
        hasil ^= 1 << geser
        a ^= b << geser
    return hasil, a


def tak_tereduksi(f):
    """Benar bila polinom f tidak dapat direduksi di dalam GF(2)."""
    derajat = f.bit_length() - 1
    if derajat < 1:
        return False
    for g in range(2, 1 << (derajat // 2 + 1)):
        if polinom_bagi(f, g)[1] == 0:
            return False
    return True


# ------------------------------------------------------------------
# Bagian 3: kurva eliptik di atas medan berhingga GF(p)
# ------------------------------------------------------------------


def pada_kurva(P, a, b, p):
    """Benar bila titik P memenuhi y^2 = x^3 + a*x + b (mod p)."""
    if P is None:
        return True
    x, y = P
    return (y * y - x ** 3 - a * x - b) % p == 0


def lawan(P, p):
    """Lawan titik P: pencerminan terhadap sumbu-x, lalu modulo p."""
    if P is None:
        return None
    x, y = P
    return (x, (-y) % p)


def tambah(P, Q, a, b, p):
    """Hitung R = P + Q pada kurva eliptik modulo p."""
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if (x1 - x2) % p == 0:
        if (y1 + y2) % p == 0:
            return None
        return gandakan(P, a, b, p)
    m = ((y2 - y1) * invers(x2 - x1, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)


def gandakan(P, a, b, p):
    """Hitung R = 2P; hasilnya None (titik O) bila ordinat P nol."""
    if P is None:
        return None
    x1, y1 = P
    if y1 % p == 0:
        return None
    m = ((3 * x1 * x1 + a) * invers(2 * y1, p)) % p
    x3 = (m * m - 2 * x1) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)


def kali(k, P, a, b, p):
    """Hitung kP dengan metode double-and-add."""
    hasil = None
    penambah = P
    while k > 0:
        if k & 1:
            hasil = tambah(hasil, penambah, a, b, p)
        penambah = gandakan(penambah, a, b, p)
        k >>= 1
    return hasil


def enumerasi(a, b, p):
    """Seluruh titik pada kurva, tanpa menyertakan titik O."""
    hasil = []
    for x in range(p):
        for y in range(p):
            if pada_kurva((x, y), a, b, p):
                hasil.append((x, y))
    return hasil


def orde(P, a, b, p):
    """Orde titik P, yaitu k terkecil sedemikian sehingga kP = O."""
    k = 1
    Q = P
    while Q is not None:
        Q = tambah(Q, P, a, b, p)
        k += 1
    return k


def bsgs(P, Q, a, b, p, n):
    """Cari k dengan Q = kP memakai baby-step giant-step.

    Biayanya sebanding dengan akar kuadrat orde n, yaitu cara terbaik
    yang diketahui untuk menyerang ECDLP.
    """
    langkah = int(n ** 0.5) + 1
    tabel = {}
    R = None
    for j in range(langkah):
        if R not in tabel:
            tabel[R] = j
        R = tambah(R, P, a, b, p)
    besar = lawan(kali(langkah, P, a, b, p), p)
    gamma = Q
    for i in range(langkah + 1):
        if gamma in tabel:
            return (i * langkah + tabel[gamma]) % n
        gamma = tambah(gamma, besar, a, b, p)
    return None


# ------------------------------------------------------------------
# Bagian 4: kurva eliptik di atas bilangan riil (pecahan eksak)
# ------------------------------------------------------------------


def tambah_real(P, Q, a):
    """Hitung P + Q pada kurva riil memakai pecahan eksak."""
    x1, y1 = P
    x2, y2 = Q
    m = Fraction(y2 - y1, x2 - x1)
    x3 = m * m - x1 - x2
    y3 = m * (x1 - x3) - y1
    return (x3, y3)


def gandakan_real(P, a):
    """Hitung 2P pada kurva riil memakai pecahan eksak."""
    x1, y1 = P
    m = Fraction(3 * x1 * x1 + a, 2 * y1)
    x3 = m * m - 2 * x1
    y3 = m * (x1 - x3) - y1
    return (x3, y3)


# ------------------------------------------------------------------
# Bagian 5: pengkodean pesan menjadi titik (metode Koblitz)
# ------------------------------------------------------------------


def koblitz_kode(m, k, a, b, p):
    """Cari titik (x, y) bagi nilai m dengan parameter basis k."""
    for s in range(1, k + 1):
        x = m * k + s
        akar = akar_kuadrat((x ** 3 + a * x + b) % p, p)
        if akar:
            return (x, akar[0])
    return None


def koblitz_dekode(x, k):
    """Pulihkan nilai m dari absis titik kurva."""
    return (x - 1) // k


# ------------------------------------------------------------------
# Bagian 6: pengujian
# ------------------------------------------------------------------


def periksa(nama, dapat, harap):
    """Cetak hasil satu pemeriksaan dan kembalikan kebenarannya."""
    tanda = "LULUS" if dapat == harap else "GAGAL"
    print(f"  {tanda}  {nama}")
    if dapat != harap:
        print(f"         diperoleh {dapat}, seharusnya {harap}")
    return dapat == harap


def uji_gf2m():
    """Aritmetika GF(2^8): penjumlahan XOR dan perkalian modulo AES."""
    print("UJI 1: aritmetika polinomial GF(2^8)")
    hasil = []
    hasil.append(periksa("0D + 06 = 0B",
                         polinom_tambah(0x0D, 0x06), 0x0B))
    hasil.append(periksa("57 + 83 = D4",
                         polinom_tambah(0x57, 0x83), 0xD4))
    aes = (1 << 8) | (1 << 4) | (1 << 3) | (1 << 1) | 1
    hasil.append(periksa("57 * 83 = C1",
                         polinom_kali(0x57, 0x83, aes, 8), 0xC1))
    hasil.append(periksa("polinom AES tak tereduksi", tak_tereduksi(aes), True))
    return all(hasil)


def uji_polinom():
    """Pembagian panjang polinom dan status ketereduksian."""
    print("UJI 2: pembagian polinom di dalam GF(2)")
    hasil = []
    # (x^3 + x^2 + 1)(x^2 + x) = x^5 + x^3 + x^2 + x, direduksi oleh x^4 + x + 1
    mentah = 0
    for i in range(4):
        if 0b1101 >> i & 1:
            mentah ^= 0b0110 << i
    hasil.append(periksa("hasil kali mentah = 101110", mentah, 0b101110))
    sisa = polinom_bagi(mentah, 0b10011)[1]
    hasil.append(periksa("sisanya x^3 = 1000", sisa, 0b1000))
    hasil.append(periksa("kali langsung lewat medan",
                         polinom_kali(0b1101, 0b0110, 0b10011, 4), 0b1000))
    hasil.append(periksa("x^4 + x + 1 tak tereduksi",
                         tak_tereduksi(0b10011), True))
    hasil.append(periksa("x^2 + 1 dapat direduksi",
                         tak_tereduksi(0b101), False))
    hasil.append(periksa("(x^2 + 1)(x^3 + x + 1) = x^5 + x^2 + x + 1",
                         polinom_kali(0b101, 0b1011, 1 << 6, 6), 0b100111))
    return all(hasil)


def uji_medan():
    """Aritmetika medan berhingga dan pencarian akar kuadrat."""
    print("UJI 3: aritmetika medan berhingga")
    hasil = []
    hasil.append(periksa("GF(23): 12 + 20 = 9", (12 + 20) % 23, 9))
    hasil.append(periksa("GF(23): 8 * 9 = 3", (8 * 9) % 23, 3))
    hasil.append(periksa("akar x^2 = 5 (mod 11)", akar_kuadrat(5, 11), [4, 7]))
    hasil.append(periksa("invers 3 mod 11", invers(3, 11), 4))
    hasil.append(periksa("invers 20 mod 23", invers(20, 23), 15))
    hasil.append(periksa("invers 8 mod 11", invers(8, 11), 7))
    hasil.append(periksa("invers 2 mod 11", invers(2, 11), 6))
    hasil.append(periksa("5 adalah kuadrat di GF(11)",
                         akar_kuadrat(5, 11), [4, 7]))
    return all(hasil)


def uji_geometri_real():
    """Penjumlahan dan penggandaan titik pada kurva di atas bilangan riil."""
    print("UJI 4: geometri kurva di atas bilangan riil")
    hasil = []
    hasil.append(periksa("P(1,1) + Q(-2,1) = (1,-1)",
                         tambah_real((1, 1), (-2, 1), -3), (1, -1)))
    hasil.append(periksa("2P = (-2,-1)",
                         gandakan_real((1, 1), -3), (-2, -1)))
    hasil.append(periksa("P(2,4) + Q(0,2) = (-1,-1)",
                         tambah_real((2, 4), (0, 2), 2), (-1, -1)))
    hasil.append(periksa("2P = (-15/16, 73/64)",
                         gandakan_real((2, 4), 2),
                         (Fraction(-15, 16), Fraction(73, 64))))
    hasil.append(periksa("diskriminan 4a^3 + 27b^2",
                         4 * (-3) ** 3 + 27 * 3 ** 2, 135))
    return all(hasil)


def uji_enumerasi():
    """Enumerasi titik pada kurva modulo prima kecil."""
    print("UJI 5: enumerasi titik pada kurva di atas GF(p)")
    hasil = []
    titik11 = enumerasi(1, 6, 11)
    hasil.append(periksa("banyak titik mod 11", len(titik11), 12))
    hasil.append(periksa("orde grup mod 11", len(titik11) + 1, 13))
    hasil.append(periksa("(2,4) terdaftar", (2, 4) in titik11, True))
    titik23 = enumerasi(1, 1, 23)
    hasil.append(periksa("banyak titik mod 23", len(titik23), 27))
    hasil.append(periksa("(4,0) termasuk", (4, 0) in titik23, True))
    hasil.append(periksa("orde grup mod 23 termasuk titik O",
                         orde((3, 10), 1, 1, 23), 28))
    titik5 = enumerasi(2, 1, 5)
    hasil.append(periksa("banyak titik mod 5", len(titik5), 6))
    return all(hasil)


def uji_penjumlahan():
    """Penjumlahan, penggandaan, dan pelelaran titik pada GF(11)."""
    print("UJI 6: penjumlahan dan pelelaran titik pada GF(11)")
    hasil = []
    P, Q = (2, 4), (5, 9)
    hasil.append(periksa("P + Q = (8,8)", tambah(P, Q, 1, 6, 11), (8, 8)))
    hasil.append(periksa("2P = (5,9)", gandakan(P, 1, 6, 11), (5, 9)))
    hasil.append(periksa("3P = (8,8)", kali(3, P, 1, 6, 11), (8, 8)))
    daftar = [kali(k, P, 1, 6, 11) for k in range(1, 14)]
    harap = [(2, 4), (5, 9), (8, 8), (10, 9), (3, 5), (7, 2), (7, 9),
             (3, 6), (10, 2), (8, 3), (5, 2), (2, 7), None]
    hasil.append(periksa("tabel pelelaran kP, k = 1..13", daftar, harap))
    hasil.append(periksa("orde P", orde(P, 1, 6, 11), 13))
    B = (3, 10)
    hasil.append(periksa("2B = (7,12) mod 23", gandakan(B, 1, 1, 23), (7, 12)))
    hasil.append(periksa("3B = (19,5) mod 23", kali(3, B, 1, 1, 23), (19, 5)))
    hasil.append(periksa("6B = (12,4) mod 23", kali(6, B, 1, 1, 23), (12, 4)))
    return all(hasil)


def uji_ecdh():
    """Pertukaran kunci ECDH pada dua kurva yang berbeda."""
    print("UJI 7: pertukaran kunci ECDH")
    hasil = []
    B5 = (0, 1)
    PA = kali(2, B5, 2, 1, 5)
    PB = kali(3, B5, 2, 1, 5)
    hasil.append(periksa("mod 5: kunci publik Alice (1,3)", PA, (1, 3)))
    hasil.append(periksa("mod 5: kunci publik Bob (3,3)", PB, (3, 3)))
    hasil.append(periksa("mod 5: kunci bersama (0,4)",
                         kali(2, PB, 2, 1, 5), (0, 4)))
    hasil.append(periksa("mod 5: kedua arah sama",
                         kali(2, PB, 2, 1, 5) == kali(3, PA, 2, 1, 5), True))
    hasil.append(periksa("mod 5: orde B", orde(B5, 2, 1, 5), 7))
    B23 = (3, 10)
    hasil.append(periksa("mod 23: kedua arah sama",
                         kali(2, kali(3, B23, 1, 1, 23), 1, 1, 23)
                         == kali(3, kali(2, B23, 1, 1, 23), 1, 1, 23),
                         True))
    return all(hasil)


def uji_eceg():
    """Enkripsi dan dekripsi ECEG pada kurva modulo 23."""
    print("UJI 8: enkripsi dan dekripsi ECEG")
    hasil = []
    a, b, p = 1, 1, 23
    B = (3, 10)
    b_privat = 3
    PB = kali(b_privat, B, a, b, p)
    PM = (7, 12)
    k = 5
    C1 = kali(k, B, a, b, p)
    C2 = tambah(PM, kali(k, PB, a, b, p), a, b, p)
    pulih = tambah(C2, lawan(kali(b_privat, C1, a, b, p), p), a, b, p)
    hasil.append(periksa("titik pertama cipherteks = kB", C1, (9, 16)))
    hasil.append(periksa("titik kedua cipherteks", C2, (18, 3)))
    hasil.append(periksa("hasil kali kunci sesaat", kali(k, PB, a, b, p), (1, 16)))
    hasil.append(periksa("pemulihan plainteks P_M", pulih, PM))
    hasil.append(periksa("kunci sesaat lain tetap benar",
                         tambah(tambah(PM, kali(9, PB, a, b, p), a, b, p),
                                lawan(kali(b_privat,
                                           kali(9, B, a, b, p), a, b, p), p),
                                a, b, p), PM))
    hasil.append(periksa("kunci sesaat berbeda, cipherteks berbeda",
                         kali(k, B, a, b, p) != kali(9, B, a, b, p), True))
    return all(hasil)


def uji_koblitz():
    """Pengkodean pesan menjadi titik dengan metode Koblitz."""
    print("UJI 9: metode Koblitz pada kurva modulo 751")
    hasil = []
    a, b, p = -1, 188, 751
    hasil.append(periksa("banyak titik kurva", len(enumerasi(a, b, p)) + 1, 727))
    titik = koblitz_kode(11, 20, a, b, p)
    hasil.append(periksa("huruf B menjadi titik (224, 248)", titik, (224, 248)))
    hasil.append(periksa("x = 221 tidak menghasilkan titik",
                         akar_kuadrat((221 ** 3 - 221 + 188) % 751, 751), []))
    hasil.append(periksa("titik itu memenuhi kurva",
                         pada_kurva(titik, a, b, p), True))
    hasil.append(periksa("dekode kembali menjadi 11",
                         koblitz_dekode(224, 20), 11))
    hasil.append(periksa("akar lain dari 673 modulo 751",
                         akar_kuadrat(673, 751), [248, 503]))
    return all(hasil)


def uji_penyerangan():
    """Penyerangan ECDLP dengan baby-step giant-step pada kurva mainan."""
    print("UJI 10: penyerangan logaritma diskrit kurva eliptik")
    hasil = []
    a, b, p = 1, 6, 11
    P = (2, 4)
    n = orde(P, a, b, p)
    hasil.append(periksa("orde titik basis", n, 13))
    for k in (1, 5, 9, 12):
        Q = kali(k, P, a, b, p)
        hasil.append(periksa(f"k = {k} dapat dipulihkan", bsgs(P, Q, a, b, p, n), k))
    # Pada kurva kecil penyerangan berhasil dalam sejumlah langkah akar n.
    hasil.append(periksa("langkah yang diperlukan sekitar akar orde",
                         int(13 ** 0.5) + 1, 4))
    return all(hasil)


def uji_latihan():
    """Angka-angka yang dipakai pada latihan dan aktivitas bab ini."""
    print("UJI 11: angka latihan dan aktivitas")
    hasil = []
    a, b, p = 1, 1, 23
    B = (3, 10)
    hasil.append(periksa("latihan: (3,10) + (7,12) = (19,5)",
                         tambah((3, 10), (7, 12), a, b, p), (19, 5)))
    hasil.append(periksa("latihan: (7,12) + (19,5) = (9,16)",
                         tambah((7, 12), (19, 5), a, b, p), (9, 16)))
    hasil.append(periksa("latihan: 2(12,4) = (5,4)",
                         gandakan((12, 4), a, b, p), (5, 4)))
    hasil.append(periksa("latihan: (17,3) adalah 4B",
                         kali(4, B, a, b, p), (17, 3)))
    hasil.append(periksa("latihan: (12,4) adalah 6B",
                         kali(6, B, a, b, p), (12, 4)))
    hasil.append(periksa("latihan: 14B berordinat nol",
                         kali(14, B, a, b, p), (4, 0)))
    hasil.append(periksa("aktivitas: P(2,4) + Q(0,2) = (-1,-1)",
                         tambah_real((2, 4), (0, 2), 2), (-1, -1)))
    hasil.append(periksa("kurva y^2 = x^3 - x + 188 licin",
                         4 * (-1) ** 3 + 27 * 188 ** 2 != 0, True))
    return all(hasil)


def main():
    """Jalankan kesebelas blok pengujian dan hitung yang lulus."""
    print("=" * 68)
    print("Verifikasi Bab 14 -- Kriptografi Kurva Eliptik")
    print("=" * 68)
    daftar = [uji_gf2m, uji_polinom, uji_medan, uji_geometri_real,
              uji_enumerasi, uji_penjumlahan, uji_ecdh, uji_eceg,
              uji_koblitz, uji_penyerangan, uji_latihan]
    lulus = 0
    for uji in daftar:
        if uji():
            lulus += 1
        print()
    print("=" * 68)
    print(f"Hasil: {lulus} dari {len(daftar)} blok pengujian LULUS")
    print("=" * 68)


if __name__ == "__main__":
    main()
