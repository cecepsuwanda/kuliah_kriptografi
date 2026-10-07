"""
aes_uji.py -- Implementasi AES/Rijndael yang dapat diuji sendiri.

Program ini membangun S-box AES dari nol (inversi di GF(2^8) + transformasi
affine), membangkitkan kunci putaran, lalu mengenkripsi dan mendekripsi blok
128 bit. Seluruh hasilnya diperiksa terhadap vektor uji resmi FIPS PUB 197
(Lampiran B dan C) sehingga tabel dan rumus di dalam buku dapat diverifikasi.

Jalankan:  python aes_uji.py
"""

# ----------------------------------------------------------------------
# Aritmetika GF(2^8): polinom biner modulo x^8 + x^4 + x^3 + x + 1
# ----------------------------------------------------------------------
POLINOM = 0x11B          # x^8 + x^4 + x^3 + x + 1


def kali_x(a):
    """Kalikan a dengan x (= byte 0x02), lalu reduksi bila derajatnya 8."""
    a <<= 1
    if a & 0x100:
        a ^= POLINOM
    return a & 0xFF


def kali(a, b):
    """Perkalian dua elemen GF(2^8) dengan metode petani Rusia (shift-and-add)."""
    hasil = 0
    while b:
        if b & 1:
            hasil ^= a
        a = kali_x(a)
        b >>= 1
    return hasil


def balikan(a):
    """Invers perkalian a di GF(2^8); balikan 0 didefinisikan 0."""
    if a == 0:
        return 0
    for x in range(1, 256):
        if kali(a, x) == 1:
            return x
    raise ValueError("invers tidak ditemukan")


def affine(bit):
    """Transformasi affine S-box: bit masukan b0..b7 (b0 = LSB) -> byte keluaran."""
    hasil = 0
    for i in range(8):
        b = (bit[i] ^ bit[(i + 4) % 8] ^ bit[(i + 5) % 8]
             ^ bit[(i + 6) % 8] ^ bit[(i + 7) % 8] ^ ((0x63 >> i) & 1))
        hasil |= (b & 1) << i
    return hasil


def buat_sbox():
    """Bangun S-box: tiap byte a dipetakan ke affine(balikan(a))."""
    sbox = [0] * 256
    for a in range(256):
        inv = balikan(a)
        sbox[a] = affine([(inv >> i) & 1 for i in range(8)])
    return sbox


SBOX = buat_sbox()
INV_SBOX = [0] * 256
for _i, _v in enumerate(SBOX):
    INV_SBOX[_v] = _i


# ----------------------------------------------------------------------
# Pembangkitan kunci putaran (KeyExpansion)
# ----------------------------------------------------------------------
def rcon():
    """RC[1..10]; RC[j] = 02 * RC[j-1] di GF(2^8)."""
    rc = [0x01]
    for _ in range(9):
        rc.append(kali(0x02, rc[-1]))
    return rc


def rot_word(w):
    """Geser satu byte ke kiri secara siklik."""
    return w[1:] + w[:1]


def sub_word(w):
    """Substitusi setiap byte word dengan S-box."""
    return [SBOX[b] for b in w]


def kunci_putaran(key, nk):
    """Hasilkan daftar word w[0..4*(Nr+1)-1] dari kunci eksternal.

    nk = panjang kunci dalam word (4 untuk AES-128, 6 untuk AES-192,
    8 untuk AES-256). AES-256 memakai SubWord tambahan ketika i mod 8 = 4.
    """
    nr = nk + 6
    rc = rcon()
    w = [list(key[4 * i:4 * i + 4]) for i in range(nk)]
    for i in range(nk, 4 * (nr + 1)):
        temp = list(w[i - 1])
        if i % nk == 0:
            temp = sub_word(rot_word(temp))
            temp[0] ^= rc[i // nk - 1]
        elif nk > 6 and i % nk == 4:
            temp = sub_word(temp)
        w.append([w[i - nk][j] ^ temp[j] for j in range(4)])
    return w, nr


# ----------------------------------------------------------------------
# Transformasi putaran
# ----------------------------------------------------------------------
def state_ke_matriks(s):
    """16 byte (urutan masukan) menjadi matriks state 4x4."""
    return [[s[4 * c + r] for c in range(4)] for r in range(4)]


def matriks_ke_state(m):
    """Matriks state 4x4 kembali menjadi 16 byte berurutan kolom."""
    out = [0] * 16
    for c in range(4):
        for r in range(4):
            out[4 * c + r] = m[r][c]
    return out


def shift_rows(s, arah=1):
    """Permutasi siklik baris ke-r sejauh r byte; arah -1 untuk kebalikannya."""
    m = state_ke_matriks(s)
    for r in range(1, 4):
        baris = m[r]
        g = (r * arah) % 4
        m[r] = baris[g:] + baris[:g]
    return matriks_ke_state(m)


def _perkalian_matriks(matriks, v):
    """Kalikan matriks 4x4 dengan vektor kolom v di GF(2^8)."""
    out = []
    for r in range(4):
        akum = 0
        for c in range(4):
            akum ^= kali(matriks[r][c], v[c])
        out.append(akum)
    return out


MIX = [[0x02, 0x03, 0x01, 0x01],
       [0x01, 0x02, 0x03, 0x01],
       [0x01, 0x01, 0x02, 0x03],
       [0x03, 0x01, 0x01, 0x02]]

INV_MIX = [[0x0E, 0x0B, 0x0D, 0x09],
           [0x09, 0x0E, 0x0B, 0x0D],
           [0x0D, 0x09, 0x0E, 0x0B],
           [0x0B, 0x0D, 0x09, 0x0E]]


def mix_columns(s, balik=False):
    """Terapkan MixColumns (atau InvMixColumns bila balik=True)."""
    matriks = INV_MIX if balik else MIX
    m = state_ke_matriks(s)
    for c in range(4):
        kolom = _perkalian_matriks(matriks, [m[r][c] for r in range(4)])
        for r in range(4):
            m[r][c] = kolom[r]
    return matriks_ke_state(m)


def tambah_kunci(s, kata):
    """AddRoundKey: XOR state dengan kunci putaran yang bersangkutan."""
    return [s[i] ^ kata[i] for i in range(16)]


def _kunci_putaran_16(w, putaran):
    return [w[4 * putaran + c][r] for c in range(4) for r in range(4)]


# ----------------------------------------------------------------------
# Enkripsi dan dekripsi
# ----------------------------------------------------------------------
def enkripsi(pt, key, jejak=False):
    """Enkripsi satu blok 16 byte; jejak=True mengembalikan state tiap putaran."""
    nk = len(key) // 4
    w, nr = kunci_putaran(key, nk)
    s = list(pt)
    riwayat = [state_ke_matriks(s)]
    s = tambah_kunci(s, _kunci_putaran_16(w, 0))
    riwayat.append(state_ke_matriks(s))
    for putaran in range(1, nr + 1):
        s = [SBOX[b] for b in s]
        s = shift_rows(s, 1)
        if putaran != nr:
            s = mix_columns(s, False)
        s = tambah_kunci(s, _kunci_putaran_16(w, putaran))
        riwayat.append(state_ke_matriks(s))
    return (bytes(s), riwayat) if jejak else bytes(s)


def dekripsi(ct, key):
    """Dekripsi satu blok 16 byte: urutan putaran dibalik, subkunci dibalik."""
    nk = len(key) // 4
    w, nr = kunci_putaran(key, nk)
    s = list(ct)
    s = tambah_kunci(s, _kunci_putaran_16(w, nr))
    for putaran in range(nr - 1, -1, -1):
        s = shift_rows(s, -1)
        s = [INV_SBOX[b] for b in s]
        s = tambah_kunci(s, _kunci_putaran_16(w, putaran))
        if putaran != 0:
            s = mix_columns(s, True)
    return bytes(s)


# ----------------------------------------------------------------------
# Utilitas tampilan
# ----------------------------------------------------------------------
def hx(data):
    return "".join("%02X" % b for b in data)


def tabel_16x16(tab, judul):
    print(judul)
    print("     " + " ".join("%2X" % c for c in range(16)))
    for r in range(16):
        print("  %X  " % r + " ".join("%02X" % tab[16 * r + c] for c in range(16)))
    print()


def garis(judul):
    print()
    print("=" * 68)
    print(judul)
    print("=" * 68)


# ----------------------------------------------------------------------
def main():
    garis("1. Vektor uji resmi FIPS PUB 197 (Lampiran C)")
    pt = bytes.fromhex("00112233445566778899AABBCCDDEEFF")
    kasus = [
        ("AES-128", "000102030405060708090A0B0C0D0E0F",
         "69C4E0D86A7B0430D8CDB78070B4C55A", 10),
        ("AES-192", "000102030405060708090A0B0C0D0E0F1011121314151617",
         "DDA97CA4864CDFE06EAF70A0EC0D7191", 12),
        ("AES-256", "000102030405060708090A0B0C0D0E0F"
                    "101112131415161718191A1B1C1D1E1F",
         "8EA2B7CA516745BFEAFC49904B496089", 14),
    ]
    print("Plainteks :", hx(pt))
    for nama, k, harus, nr in kasus:
        key = bytes.fromhex(k)
        c = enkripsi(pt, key)
        p = dekripsi(c, key)
        print("%s : Nr=%2d  C=%s  %s" %
              (nama, nr, hx(c), "BENAR" if hx(c) == harus else "SALAH"))
        print("            D(C)=%s  %s" %
              (hx(p), "BENAR" if p == pt else "SALAH"))

    garis("2. Pembangkitan S-box dari nol, dibandingkan FIPS PUB 197 Tabel 4")
    baris0 = "637C777BF26B6FC53001672B" + "FED7AB76"
    print("S[00..0F] =", "".join("%02X" % SBOX[i] for i in range(16)))
    print("Tabel 4   =", baris0)
    print("S[53] =", "%02X" % SBOX[0x53], "  S[6F] =", "%02X" % SBOX[0x6F])
    tabel_16x16(SBOX, "S-box lengkap (baris = nibble atas, kolom = nibble bawah):")
    tabel_16x16(INV_SBOX, "S-box invers (dipakai InvSubBytes):")

    garis("3. Aritmetika GF(2^8)")
    print("0xD + 0x06 = %02X   (penjumlahan = XOR)" % (0x0D ^ 0x06))
    print("0x57 + 0x83 = %02X" % (0x57 ^ 0x83))
    print("0x02 * 0x26 = %02X" % kali(0x02, 0x26))
    print("0x03 * 0x7B = %02X" % kali(0x03, 0x7B))
    print("0x57 * 0x83 = %02X" % kali(0x57, 0x83))
    # 0x83 = 0x80 + 0x02 + 0x01, jadi 0x57*0x83 = 0x57*0x80 ^ 0x57*0x02 ^ 0x57
    print("   cara lain: 0x57*0x80 ^ 0x57*0x02 ^ 0x57 = %02X"
          % (kali(0x57, 0x80) ^ kali(0x57, 0x02) ^ 0x57))
    print()
    print("Tabel perkalian 0x02 (kali_x) dan 0x03 untuk beberapa nilai:")
    for v in (0x26, 0x7B, 0x57, 0x83, 0xD4, 0xBD, 0x43):
        print("  02*%02X = %02X   03*%02X = %02X" %
              (v, kali(0x02, v), v, kali(0x03, v)))
    print()
    print("Invers beberapa elemen:", end=" ")
    for v in (0x01, 0x02, 0x03, 0x53, 0x57, 0x6F, 0xFF):
        print("%02X->%02X" % (v, balikan(v)), end="  ")
    print()

    garis("4. Contoh MixColumns dan InvMixColumns")
    kolom = [0x26, 0x7B, 0xBD, 0x43]
    hasil = _perkalian_matriks(MIX, kolom)
    kembali = _perkalian_matriks(INV_MIX, hasil)
    print("MixColumns([26,7B,BD,43])    = ", ["%02X" % x for x in hasil])
    print("InvMixColumns(hasil)        = ", ["%02X" % x for x in kembali])

    garis("5. Pembangkitan kunci putaran, kunci 'Two One Nine Two'")
    key = bytes.fromhex("54776F204F6E65204E696E652054776F")
    w, nr = kunci_putaran(key, 4)
    print("kunci dalam ASCII :", "Two One Nine Two")
    print("kunci dalam hex   :", hx(key))
    print("jumlah word       :", len(w), " (4 x (Nr+1) = 4 x 11 = 44)")
    print("RC[1..10]         :", " ".join("%02X" % x for x in rcon()))
    for i in range(4):
        print("w[%d] = %s" % (i, hx(w[i])))
    print("RotWord(w[3])     =", hx(rot_word(w[3])))
    print("SubWord(RotWord)  =", hx(sub_word(rot_word(w[3]))))
    g = sub_word(rot_word(w[3]))
    g[0] ^= rcon()[0]
    print("g(w[3])           =", hx(g))
    for i in range(4, 8):
        print("w[%d] = %s" % (i, hx(w[i])))
    print("kunci putaran ke-0:", [["%02X" % x for x in r]
                                  for r in state_ke_matriks(_kunci_putaran_16(w, 0))])
    print("kunci putaran ke-1:", [["%02X" % x for x in r]
                                  for r in state_ke_matriks(_kunci_putaran_16(w, 1))])
    print("kunci putaran ke-10:", [["%02X" % x for x in r]
                                   for r in state_ke_matriks(_kunci_putaran_16(w, 10))])

    garis("6. Jejak putaran vektor uji FIPS PUB 197 Lampiran B")
    key = bytes.fromhex("2B7E151628AED2A6ABF7158809CF4F3C")
    pt = bytes.fromhex("3243F6A8885A308D313198A2E0370734")
    c, jejak = enkripsi(pt, key, jejak=True)
    for i, m in enumerate(jejak[:4]):
        print("state[%2d] :" % i, [["%02X" % x for x in r] for r in m])
    print("   ...")
    for i in (9, 10):
        print("state[%2d] :" % i, [["%02X" % x for x in r] for r in jejak[i]])
    print("ciphertext:", hx(c), " (standar: 3925841D02DC09FBDC118597196A0B32)")

    garis("7. Dekripsi membalikkan enkripsi")
    key = bytes.fromhex("54776F204F6E65204E696E652054776F")
    m = b"Kriptografi AES!"          # tepat 16 byte = satu blok
    c = enkripsi(m, key)
    print("pesan     :", m)
    print("cipherteks:", hx(c))
    print("hasil balik:", dekripsi(c, key))


if __name__ == "__main__":
    main()
