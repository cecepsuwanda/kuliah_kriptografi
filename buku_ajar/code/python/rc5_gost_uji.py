# rc5_gost_uji.py
#
# Program uji untuk Bab 9 (Algoritma Block Cipher Lainnya).
#
# Bagian pertama mengimplementasikan RC5 secara umum (parameter w, r, b)
# beserta prosedur pembangkitan kunci putarannya, lalu memeriksanya terhadap
# vektor uji resmi RFC 2040. Bagian kedua mengimplementasikan fungsi putaran
# GOST sesuai RFC 5830 dan RFC 4357, lalu memeriksa contoh pada buku.
#
# Hanya memakai pustaka standar Python. Jalankan dengan:
#     python rc5_gost_uji.py
#
# Seluruh berkas ini ASCII; tidak ada karakter di luar 7 bit.

# ----------------------------------------------------------------------
# BAGIAN 1: RC5
# ----------------------------------------------------------------------

# Konstanta P_w dan Q_w, diturunkan dari bilangan e dan phi (lihat buku,
# Tabel konstanta P_w dan Q_w).
KONSTANTA = {
    16: (0xB7E1,             0x9E37),
    32: (0xB7E15163,         0x9E3779B9),
    64: (0xB7E151628AED2A6B, 0x9E3779B97F4A7C15),
}


def rotl(x, n, w):
    """Rotasi sirkuler ke kiri sejauh n bit atas bilangan w bit."""
    n %= w
    mask = (1 << w) - 1
    return ((x << n) | (x >> (w - n))) & mask


def rotr(x, n, w):
    """Rotasi sirkuler ke kanan sejauh n bit atas bilangan w bit."""
    n %= w
    mask = (1 << w) - 1
    return ((x >> n) | (x << (w - n))) & mask


def jadwal_kunci_rc5(kunci, w, r):
    """Membangkitkan larik kunci putaran S[0..2r+1].

    kunci : bytes, panjang 0..255 byte
    w     : ukuran kata, 16 / 32 / 64
    r     : jumlah putaran
    """
    b = len(kunci)
    u = w // 8                     # banyak byte per kata
    c = max(1, (b + u - 1) // u)   # banyak kata pada larik L
    t = 2 * r + 2                  # banyak kunci putaran
    mask = (1 << w) - 1

    # Tahap 1: salin kunci ke larik L, little-endian, sisa byte diisi nol.
    L = [0] * c
    for i in range(c):
        for j in range(u):
            pos = i * u + j
            if pos < b:
                L[i] |= kunci[pos] << (8 * j)

    # Tahap 2: inisialisasi S dengan barisan aritmetika dari P_w dan Q_w.
    P, Q = KONSTANTA[w]
    S = [0] * t
    S[0] = P
    for i in range(1, t):
        S[i] = (S[i - 1] + Q) & mask

    # Tahap 3: pencampuran L dan S sebanyak n = 3 * max(t, c) langkah.
    i = j = 0
    X = Y = 0
    n = 3 * max(t, c)
    for _ in range(n):
        S[i] = rotl((S[i] + X + Y) & mask, 3, w)
        X = S[i]
        i = (i + 1) % t
        L[j] = rotl((L[j] + X + Y) & mask, X + Y, w)
        Y = L[j]
        j = (j + 1) % c

    return S


def enkripsi_rc5(blok, S, w, r):
    """Enkripsi satu blok (dua kata) RC5."""
    mask = (1 << w) - 1
    A, B = blok
    A = (A + S[0]) & mask
    B = (B + S[1]) & mask
    for i in range(1, r + 1):
        A = (rotl(A ^ B, B, w) + S[2 * i]) & mask
        B = (rotl(B ^ A, A, w) + S[2 * i + 1]) & mask
    return A, B


def dekripsi_rc5(blok, S, w, r):
    """Dekripsi satu blok RC5; kebalikan urutan enkripsi."""
    mask = (1 << w) - 1
    A, B = blok
    for i in range(r, 0, -1):
        B = (rotr((B - S[2 * i + 1]) & mask, A, w) ^ A) & mask
        A = (rotr((A - S[2 * i]) & mask, B, w) ^ B) & mask
    B = (B - S[1]) & mask
    A = (A - S[0]) & mask
    return A, B


def blok_ke_bytes(blok, w):
    """Susun dua kata menjadi barisan byte little-endian."""
    u = w // 8
    keluar = bytearray()
    for kata in blok:
        for j in range(u):
            keluar.append((kata >> (8 * j)) & 0xFF)
    return bytes(keluar)


def bytes_ke_blok(data, w):
    """Kebalikan blok_ke_bytes."""
    u = w // 8
    kata = []
    for i in range(len(data) // u):
        nilai = 0
        for j in range(u):
            nilai |= data[i * u + j] << (8 * j)
        kata.append(nilai)
    return tuple(kata)


def enkripsi_cbc(plainteks, kunci, w, r, iv):
    """Enkripsi mode CBC untuk masukan kelipatan ukuran blok."""
    S = jadwal_kunci_rc5(kunci, w, r)
    ukuran = 2 * (w // 8)
    keluar = bytearray()
    sebelumnya = iv
    for pos in range(0, len(plainteks), ukuran):
        blok = bytes(plainteks[pos:pos + ukuran])
        campur = bytes(a ^ b for a, b in zip(blok, sebelumnya))
        hasil = enkripsi_rc5(bytes_ke_blok(campur, w), S, w, r)
        sebelumnya = blok_ke_bytes(hasil, w)
        keluar += sebelumnya
    return bytes(keluar)


# ----------------------------------------------------------------------
# BAGIAN 2: GOST (Magma)
# ----------------------------------------------------------------------

# Kedelapan kotak-S GOST. Nibble paling kanan masuk ke S1.
SBOX_GOST = [
    [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
    [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
    [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
    [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
    [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
    [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 14, 15],
    [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
    [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12],
]


def substitusi_gost(x):
    """Substitusi 32 bit oleh kedelapan kotak-S GOST."""
    keluar = 0
    for j in range(8):
        nibble = (x >> (4 * j)) & 0xF
        keluar |= SBOX_GOST[j][nibble] << (4 * j)
    return keluar


def fungsi_f_gost(R, K):
    """Fungsi f GOST: jumlah modulo 2^32, substitusi, geser kiri 11 bit."""
    return rotl(substitusi_gost((R + K) & 0xFFFFFFFF), 11, 32)


def putaran_gost(L, R, K):
    """Satu putaran Jaringan Feistel GOST."""
    return R, L ^ fungsi_f_gost(R, K)


# ----------------------------------------------------------------------
# BAGIAN 3: PENGUJIAN MANDIRI
# ----------------------------------------------------------------------

VEKTOR_RFC2040 = [
    # (r, kunci, iv, plainteks, cipherteks)
    (0,  "00", "0000000000000000", "0000000000000000", "7a7bba4d79111d1e"),
    (0,  "00", "0000000000000000", "ffffffffffffffff", "797bba4d78111d1e"),
    (0,  "00", "0102030405060708", "1020304050607080", "8b9ded91ce7794a6"),
    (1,  "11", "0000000000000000", "0000000000000000", "2f759fe7ad86a378"),
    (2,  "00", "0000000000000000", "0000000000000000", "dca2694bf40e0788"),
    (8,  "00", "0000000000000000", "0000000000000000", "dcfe098577eca5ff"),
    (8,  "00", "0102030405060708", "1020304050607080", "9646fb77638f9ca8"),
    (12, "00", "0102030405060708", "1020304050607080", "b2b3209db6594da4"),
    (16, "00", "0102030405060708", "1020304050607080", "545f7f32a5fc3836"),
    (8,  "0102030405", "0000000000000000", "ffffffffffffffff", "7875dbf6738c6478"),
    (12, "0102030405", "0000000000000000", "ffffffffffffffff", "97e0787837ed317f"),
    (8,  "0102030405060708", "0102030405060708", "1020304050607080",
         "5c4c041e0f217ac3"),
    (12, "0102030405060708", "0102030405060708", "1020304050607080",
         "921f12485373b4f7"),
    (16, "0102030405060708", "0102030405060708", "1020304050607080",
         "5ba0ca6bbe7f5fad"),
    (8,  "01020304050607081020304050607080", "0102030405060708",
         "1020304050607080", "c533771cd0110e63"),
    (12, "01020304050607081020304050607080", "0102030405060708",
         "1020304050607080", "294ddb46b3278d60"),
    (16, "01020304050607081020304050607080", "0102030405060708",
         "1020304050607080", "dad6bda9dfe8f7e8"),
]


def uji_rc5():
    print("=" * 68)
    print("UJI 1: RC5 terhadap vektor resmi RFC 2040 (mode CBC, w = 32)")
    print("=" * 68)
    print("%-14s %-34s %-18s %s" % ("Varian", "Kunci", "Cipherteks", "Hasil"))
    print("-" * 68)
    cocok = 0
    for r, kunci, iv, plain, harap in VEKTOR_RFC2040:
        kb = bytes.fromhex(kunci)
        hasil = enkripsi_cbc(bytes.fromhex(plain), kb, 32, r, bytes.fromhex(iv))
        benar = hasil.hex() == harap
        cocok += benar
        print("%-14s %-34s %-18s %s" % (
            "RC5-32/%d/%d" % (r, len(kb)), kunci, hasil.hex(),
            "BENAR" if benar else "SALAH (harap %s)" % harap))
    print("-" * 68)
    print("Cocok %d dari %d vektor." % (cocok, len(VEKTOR_RFC2040)))
    return cocok == len(VEKTOR_RFC2040)


def uji_rc5_putar_balik():
    print()
    print("=" * 68)
    print("UJI 2: Enkripsi dan dekripsi RC5 harus saling membatalkan")
    print("=" * 68)
    kunci = bytes.fromhex("deadbeefcafebabe")
    S = jadwal_kunci_rc5(kunci, 32, 12)
    semua = True
    for nilai in (0, 1, 0x12345678, 0xFFFFFFFF):
        blok = (nilai, nilai ^ 0x5A5A5A5A)
        C = enkripsi_rc5(blok, S, 32, 12)
        P = dekripsi_rc5(C, S, 32, 12)
        benar = P == blok
        semua = semua and benar
        print("  P = %08X %08X  ->  C = %08X %08X  ->  P' = %08X %08X  %s" % (
            blok[0], blok[1], C[0], C[1], P[0], P[1],
            "BENAR" if benar else "SALAH"))
    return semua


def uji_gost():
    print()
    print("=" * 68)
    print("UJI 3: Fungsi putaran GOST sesuai contoh pada buku")
    print("=" * 68)

    # Setiap kotak-S harus merupakan permutasi dari 0..15.
    for j, kotak in enumerate(SBOX_GOST):
        assert sorted(kotak) == list(range(16)), "S%d bukan permutasi" % (j + 1)
    print("  Kedelapan kotak-S adalah permutasi dari 0..15: BENAR")

    # Jumlah modulo 2^32.
    jumlah = (0x12345678 + 0x61626364) & 0xFFFFFFFF
    print("  R + K            = 12345678 + 61626364 = %08X  (harap 7396B9DC) %s"
          % (jumlah, "BENAR" if jumlah == 0x7396B9DC else "SALAH"))

    # Substitusi kedelapan nibble.
    sub = substitusi_gost(jumlah)
    print("  Substitusi       = %08X                      (harap 416DCF77) %s"
          % (sub, "BENAR" if sub == 0x416DCF77 else "SALAH"))

    # Pergeseran sirkuler 11 bit.
    geser = rotl(sub, 11, 32)
    print("  Rotasi kiri 11   = %08X                      (harap 6E7BBA0B) %s"
          % (geser, "BENAR" if geser == 0x6E7BBA0B else "SALAH"))

    # Satu putaran penuh.
    L, R = putaran_gost(0x01020304, 0x12345678, 0x61626364)
    print("  Satu putaran     = (L, R) = (%08X, %08X)" % (L, R))
    print("                     harap    (12345678, 6F79B90F) %s"
          % ("BENAR" if (L, R) == (0x12345678, 0x6F79B90F) else "SALAH"))
    return (jumlah == 0x7396B9DC and sub == 0x416DCF77
            and geser == 0x6E7BBA0B and (L, R) == (0x12345678, 0x6F79B90F))


def rapi(nilai):
    """Ubah jumlah byte menjadi satuan yang mudah dibaca."""
    for satuan, batas in (("GiB", 2 ** 30), ("MiB", 2 ** 20), ("KiB", 2 ** 10)):
        if nilai >= batas:
            return "%.3g %s" % (nilai / batas, satuan)
    return "%d byte" % nilai


def uji_serangan_ulang_tahun():
    print()
    print("=" * 68)
    print("UJI 4: Batas rekeying akibat paradoks ulang tahun")
    print("=" * 68)
    for n in (32, 64, 128):
        blok = 2 ** (n // 2)
        byte = blok * (n // 8)
        print("  Blok %3d bit: 2^(%d/2) = 2^%-2d blok x %2d byte = %s"
              % (n, n, n // 2, n // 8, rapi(byte)))
    print()
    print("  Untuk n = 64: 2^32 blok x 8 byte = 2^35 byte = 32 GiB.")
    print("  Itulah batas pemakaian satu kunci GOST maupun Blowfish.")
    return True


if __name__ == "__main__":
    hasil = []
    hasil.append(("Uji RC5 terhadap RFC 2040", uji_rc5()))
    hasil.append(("Enkripsi/dekripsi RC5", uji_rc5_putar_balik()))
    hasil.append(("Fungsi putaran GOST", uji_gost()))
    hasil.append(("Batas rekeying", uji_serangan_ulang_tahun()))
    print()
    print("=" * 68)
    print("RINGKASAN")
    print("=" * 68)
    for nama, lulus in hasil:
        print("  %-28s %s" % (nama, "LULUS" if lulus else "GAGAL"))
    print("  %-28s %s" % ("Seluruh pengujian",
                          "LULUS" if all(h for _, h in hasil) else "GAGAL"))
