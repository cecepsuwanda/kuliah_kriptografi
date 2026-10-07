"""RSA: verifikasi menyeluruh atas seluruh angka pada Bab 10.

Program ini menghitung ulang setiap angka yang muncul pada contoh terhitung,
tabel, dan latihan Bab 10, lalu memeriksanya satu per satu. Bagian yang diuji
meliputi:

  1. pembangkitan kunci dan invers modulo dengan Algoritma Euclidean diperluas,
  2. enkripsi satu blok,
  3. enkripsi dan dekripsi pesan multi-blok "HELLO ALICE" beserta penjagaan
     angka nol di depan,
  4. sifat deterministik RSA telanjang dan serangan kamus,
  5. kerapuhan perubahan (malleability) pada RSA tanpa padding,
  6. perkiraan usaha pemfaktoran menurut panjang modulus.

Jalankan: python rsa_uji.py
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


def euclid_diperluas(a, b):
    """Algoritma Euclidean diperluas.

    Kembalikan (pbb, s, t) sehingga s * a + t * b = pbb(a, b), beserta
    jejak setiap langkahnya seperti Tabel 10.1 pada buku.
    """
    lama_r, r = a, b
    lama_s, s = 1, 0
    lama_t, t = 0, 1
    jejak = [(0, None, lama_r, lama_s, lama_t)]
    langkah = 0
    while r:
        hasil_bagi = lama_r // r
        lama_r, r = r, lama_r - hasil_bagi * r
        lama_s, s = s, lama_s - hasil_bagi * s
        lama_t, t = t, lama_t - hasil_bagi * t
        langkah += 1
        jejak.append((langkah, hasil_bagi, lama_r, lama_s, lama_t))
    return lama_r, lama_s, lama_t, jejak


def invers_modulo(e, phi):
    """Balikan e modulo phi, yaitu d dengan e * d = 1 (mod phi)."""
    pbb_e_phi, _, t, _ = euclid_diperluas(phi, e)
    if pbb_e_phi != 1:
        raise ValueError("e tidak relatif prima terhadap phi(n); invers tidak ada")
    return t % phi


# ------------------------------------------------------------------
# 2. Pembangkitan kunci, enkripsi, dan dekripsi
# ------------------------------------------------------------------

def bangkitkan_kunci(p, q, e):
    """Kembalikan (n, phi, d) untuk dua bilangan prima p, q dan eksponen e."""
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


# ------------------------------------------------------------------
# 3. Pengodean pesan menjadi blok bilangan bulat
# ------------------------------------------------------------------

def kodekan(pesan):
    """Ubah teks menjadi deretan digit, A = 00 sampai Z = 25, spasi dibuang."""
    pesan = pesan.upper()
    return "".join("{:02d}".format(ord(h) - ord("A")) for h in pesan if h != " ")


def blokkan(kode, panjang=4):
    """Potong deretan digit menjadi blok sepanjang `panjang` digit."""
    if len(kode) % panjang:
        kode = kode + "0" * (panjang - len(kode) % panjang)
    return [int(kode[i:i + panjang]) for i in range(0, len(kode), panjang)]


def rangkaikan(blok, panjang=4):
    """Kembalikan blok-blok menjadi deretan digit dengan nol di depan utuh."""
    return "".join("{:0{}}".format(m, panjang) for m in blok)


def baca_kode(kode):
    """Terjemahkan deretan digit kembali menjadi huruf."""
    return "".join(chr(ord("A") + int(kode[i:i + 2])) for i in range(0, len(kode), 2))


def enkripsi_pesan(pesan, e, n, panjang=4):
    """Enkripsi seluruh pesan; kembalikan daftar (blok, cipher) dan cipherteksnya."""
    kode = kodekan(pesan)
    blok = blokkan(kode, panjang)
    pasangan = [(m, enkripsi(m, e, n)) for m in blok]
    cipherteks = [c for _, c in pasangan]
    return kode, pasangan, cipherteks


def dekripsi_pesan(cipherteks, d, n, panjang=4):
    """Dekripsi seluruh cipherteks; kembalikan plainteks berbentuk huruf."""
    blok = [dekripsi(c, d, n) for c in cipherteks]
    return baca_kode(rangkaikan(blok, panjang)), blok


# ------------------------------------------------------------------
# 4. Serangan kamus pada RSA telanjang
# ------------------------------------------------------------------

def kamus_huruf(e, n):
    """Bangun kamus cipherteks untuk seluruh huruf abjad, hanya dari kunci publik."""
    return {enkripsi(k, e, n): chr(ord("A") + k) for k in range(26)}


def serang_kamus(cipherteks, kamus):
    """Baca cipherteks blok demi blok dengan kamus; '?' bila tidak ada di kamus."""
    return "".join(kamus.get(c, "?") for c in cipherteks)


# ------------------------------------------------------------------
# 5. Kerapuhan perubahan (malleability)
# ------------------------------------------------------------------

def perlihatkan_kerapuhan(m, e, d, n, s):
    """Ganti cipherteks c menjadi c * s^e mod n dan lihat hasil dekripsinya."""
    c = enkripsi(m, e, n)
    s_pangkat_e = enkripsi(s, e, n)
    c_palsu = (c * s_pangkat_e) % n
    m_palsu = dekripsi(c_palsu, d, n)
    return {
        "c": c,
        "s_pangkat_e": s_pangkat_e,
        "c_palsu": c_palsu,
        "m_palsu": m_palsu,
        "m_kali_s": (m * s) % n,
    }


# ------------------------------------------------------------------
# 6. Perkiraan usaha pemfaktoran
# ------------------------------------------------------------------

def perkirakan_pemfaktoran(bit):
    """Kembalikan perkiraan usaha pemfaktoran modulus n sepanjang `bit` bit."""
    if bit <= 256:
        return "kurang dari sehari dengan satu komputer pribadi"
    if bit <= 512:
        return "beberapa ratus komputer yang bekerja bersama"
    if bit <= 768:
        return "sudah pernah dipecahkan (RSA-768, 2009) dengan biaya besar"
    if bit <= 1024:
        return "belum pernah dipecahkan secara publik, tetapi dianggap terlalu tipis"
    if bit <= 2048:
        return "di luar jangkauan teknologi sekarang"
    return "diperkirakan aman sampai beberapa dekade mendatang"


# ------------------------------------------------------------------
# Pengujian
# ------------------------------------------------------------------

def uji_pembangkitan_kunci():
    n, phi, d = bangkitkan_kunci(47, 71, 79)
    assert (n, phi, d) == (3337, 3220, 1019), (n, phi, d)
    assert (79 * d) % phi == 1
    assert 79 * 1019 == 1 + 25 * 3220
    print("UJI 1 LULUS  pembangkitan kunci: n = 3337, phi = 3220, d = 1019")
    print("             phi(n) = 46 x 70 = 3220 (bukan 46 x 60)")
    print("             e * d = 79 x 1019 = 80501 = 1 + 25 x 3220")
    return n, phi, d


def uji_euclid_diperluas(n, phi):
    pbb_phi_e, s, t, jejak = euclid_diperluas(phi, 79)
    assert pbb_phi_e == 1
    assert s * phi + t * 79 == 1, (s, t)
    assert t % phi == 1019
    print("UJI 2 LULUS  Algoritma Euclidean diperluas, jejak lima langkah:")
    print("             {:>8} {:>7} {:>6} {:>7} {:>7}".format(
        "langkah", "q", "r", "s", "t"))
    for langkah, hasil_bagi, r, s_i, t_i in jejak:
        q_teks = "-" if hasil_bagi is None else str(hasil_bagi)
        print("             {:>8} {:>7} {:>6} {:>7} {:>7}".format(
            langkah, q_teks, r, s_i, t_i))
    print("             -25 x 3220 + 1019 x 79 = {}".format(s * phi + t * 79))
    print("             d = t mod phi = 1019, tanpa menebak nilai k")


def uji_satu_blok(n, d):
    c = enkripsi(16, 79, n)
    assert c == 1493, c
    assert dekripsi(c, d, n) == 16
    print("UJI 3 LULUS  satu blok: 16^79 mod 3337 = 1493, dan 1493^1019 mod 3337 = 16")


def uji_hello_alice(n, d):
    kode, pasangan, cipherteks = enkripsi_pesan("HELLO ALICE", 79, n)
    assert kode == "07041111140011080204", kode
    assert len(kode) == 20, len(kode)
    assert cipherteks == [328, 301, 2653, 2986, 1164], cipherteks
    pulih, _ = dekripsi_pesan(cipherteks, d, n)
    assert pulih == "HELLOALICE", pulih
    print("UJI 4 LULUS  pesan multi-blok:")
    print("             kode  = {} ({} digit)".format(kode, len(kode)))
    for i, (m, c) in enumerate(pasangan, 1):
        print("             m_{} = {:04d} -> c_{} = {:04d}".format(i, m, i, c))
    print("             cipherteks ditulis empat digit: 0328, 0301, 2653, 2986, 1164")
    print("             hasil dekripsi = {}".format(pulih))


def uji_angka_nol_di_depan(n, d):
    # Tanpa penjagaan nol di depan, blok 0704 dan 0204 berubah panjangnya.
    benar = rangkaikan([704, 1111, 1400, 1108, 204], 4)
    assert benar == "07041111140011080204", benar
    salah = "".join(str(x) for x in [704, 1111, 1400, 1108, 204])
    assert salah == "704111114001108204", salah
    assert len(salah) == 18 and len(benar) == 20
    # Sisi cipherteks: c_2 = 301 harus tetap ditulis empat digit menjadi 0301.
    cipher = [328, 301, 2653, 2986, 1164]
    assert "{:04d}".format(cipher[1]) == "0301"
    assert "{:04d}".format(cipher[0]) == "0328"
    print("UJI 5 LULUS  penjagaan angka nol di depan:")
    print("             benar : {} ({} digit)".format(benar, len(benar)))
    print("             salah : {} ({} digit)".format(salah, len(salah)))
    print("             cipherteks: {} -> {}".format(
        "{:04d}".format(cipher[1]), cipher[1]))
    print("             batas antrablok bergeser bila nol di depan dibuang")


def uji_determinisme_dan_kamus(n, d):
    c_pertama = enkripsi(203, 79, n)
    c_kedua = enkripsi(203, 79, n)
    assert c_pertama == c_kedua == 1488, (c_pertama, c_kedua)
    kamus = kamus_huruf(79, n)
    assert len(kamus) == 26
    # Enkripsi huruf Q (kode 16) lalu baca kembali hanya dengan kamus.
    c = enkripsi(16, 79, n)
    assert kamus[c] == "Q", kamus[c]
    print("UJI 6 LULUS  RSA telanjang bersifat deterministik dan kamus dapat dibangun:")
    print("             blok 0203 dienkripsi dua kali -> {} dan {}".format(
        c_pertama, c_kedua))
    print("             kamus 26 huruf dibangun dari kunci publik saja")
    print("             c = 1493 terbaca sebagai huruf {}".format(kamus[c]))


def uji_kerapuhan(n, d):
    hasil = perlihatkan_kerapuhan(m=16, e=79, d=d, n=n, s=3)
    assert hasil["c"] == 1493
    assert hasil["s_pangkat_e"] == 158, hasil["s_pangkat_e"]
    assert hasil["c_palsu"] == 2304, hasil["c_palsu"]
    assert hasil["m_palsu"] == 48
    assert hasil["m_palsu"] == hasil["m_kali_s"]
    print("UJI 7 LULUS  kerapuhan perubahan (malleability):")
    print("             c = 1493, s = 3, s^79 mod 3337 = {}".format(
        hasil["s_pangkat_e"]))
    print("             c' = 1493 x 158 mod 3337 = {}".format(hasil["c_palsu"]))
    print("             dekripsi c' = {}, padahal m x s = 16 x 3 = {}".format(
        hasil["m_palsu"], hasil["m_kali_s"]))


def uji_parameter_kedua():
    n2, phi2, d2 = bangkitkan_kunci(7, 11, 7)
    assert (n2, phi2, d2) == (77, 60, 43), (n2, phi2, d2)
    c2 = enkripsi(8, 7, n2)
    assert c2 == 57, c2
    assert dekripsi(c2, d2, n2) == 8
    print("UJI 8 LULUS  parameter kedua: p = 7, q = 11 -> n = 77, phi = 60, d = 43")
    print("             8^7 mod 77 = 57, dan 57^43 mod 77 = 8")


def uji_perkiraan_pemfaktoran():
    harapan = {256: "kurang dari sehari", 512: "beberapa ratus komputer",
               768: "RSA-768", 1024: "terlalu tipis", 2048: "di luar jangkauan",
               3072: "beberapa dekade"}
    for bit, potongan in harapan.items():
        teks = perkirakan_pemfaktoran(bit)
        assert potongan in teks, (bit, teks)
    print("UJI 9 LULUS  perkiraan pemfaktoran menurut panjang modulus:")
    for bit in (256, 512, 768, 1024, 2048, 3072):
        print("             {:>5} bit: {}".format(bit, perkirakan_pemfaktoran(bit)))


def main():
    print("=" * 74)
    print("VERIFIKASI SELURUH ANGKA PADA BAB 10")
    print("=" * 74)

    n, phi, d = uji_pembangkitan_kunci()
    print()
    uji_euclid_diperluas(n, phi)
    print()
    uji_satu_blok(n, d)
    print()
    uji_hello_alice(n, d)
    print()
    uji_angka_nol_di_depan(n, d)
    print()
    uji_determinisme_dan_kamus(n, d)
    print()
    uji_kerapuhan(n, d)
    print()
    uji_parameter_kedua()
    print()
    uji_perkiraan_pemfaktoran()
    print()
    print("=" * 74)
    print("Seluruh pengujian LULUS")
    print("=" * 74)


if __name__ == "__main__":
    main()
