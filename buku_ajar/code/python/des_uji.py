"""Verifikasi tabel DES: vektor uji resmi, putaran pertama, dan kunci lemah.

Bab 7. Program ini memuat seluruh tabel bit DES yang dicetak di buku
(IP, IP^-1, E, P, PC-1, PC-2, S1-S8, dan jadwal pergeseran) sehingga
pembaca dapat memeriksa bahwa hasil kerjanya di atas kertas sama dengan
hasil program.

Jalankan: python des_uji.py
"""

# ---------------------------------------------------------------- tabel bit
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

IP_INV = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2,
       59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6,
       61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

GESER = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

S = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
]

# ------------------------------------------------------------------ bantuan
def ke_bit(nilai, panjang):
    """Ubah bilangan bulat menjadi senarai bit, bit paling kiri paling berarti."""
    return [int(c) for c in format(nilai, "0%db" % panjang)]


def ke_hex(bit):
    """Ubah senarai bit menjadi senarai karakter heksadesimal besar."""
    return "%0*X" % (len(bit) // 4, int("".join(map(str, bit)), 2))


def ke_teks(bit):
    return "".join(map(str, bit))


def permutasi(bit, tabel):
    """Tabel 1-basis: bit keluaran ke-i diambil dari bit masukan tabel[i]."""
    return [bit[i - 1] for i in tabel]


def geser_kiri(bit, n):
    return bit[n:] + bit[:n]


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


# ----------------------------------------------------------------- DES inti
def kunci_putaran(kunci):
    """Hasilkan 16 subkunci 48 bit dari kunci eksternal 64 bit."""
    k = permutasi(ke_bit(kunci, 64), PC1)
    C, D = k[:28], k[28:]
    hasil = []
    for i in range(16):
        C = geser_kiri(C, GESER[i])
        D = geser_kiri(D, GESER[i])
        hasil.append(permutasi(C + D, PC2))
    return hasil


def fungsi_f(R, K):
    """Fungsi f DES: ekspansi, XOR subkunci, delapan S-box, lalu permutasi P."""
    x = xor(permutasi(R, E), K)
    keluaran = []
    for j in range(8):
        grup = x[j * 6:j * 6 + 6]
        baris = grup[0] * 2 + grup[5]
        kolom = int("".join(map(str, grup[1:5])), 2)
        keluaran += ke_bit(S[j][baris][kolom], 4)
    return permutasi(keluaran, P)


def daftar_putaran(plainteks, kunci):
    """Kembalikan senarai (L_i, R_i) untuk i = 0 sampai 16."""
    K = kunci_putaran(kunci)
    p = permutasi(ke_bit(plainteks, 64), IP)
    L, R = p[:32], p[32:]
    jejak = [(L[:], R[:])]
    for i in range(16):
        L, R = R, xor(L, fungsi_f(R, K[i]))
        jejak.append((L[:], R[:]))
    return jejak


def enkripsi(plainteks, kunci):
    L, R = daftar_putaran(plainteks, kunci)[-1]
    return permutasi(R + L, IP_INV)


def dekripsi(cipherteks, kunci):
    """Dekripsi memakai putaran yang sama dengan subkunci berurutan terbalik."""
    K = kunci_putaran(kunci)[::-1]
    p = permutasi(ke_bit(cipherteks, 64), IP)
    L, R = p[:32], p[32:]
    for i in range(16):
        L, R = R, xor(L, fungsi_f(R, K[i]))
    return permutasi(R + L, IP_INV)


# -------------------------------------------------------------------- utama
if __name__ == "__main__":
    P_uji = 0x0123456789ABCDEF
    K_uji = 0x133457799BBCDFF1

    print("1. Vektor uji resmi FIPS PUB 46-3")
    C = enkripsi(P_uji, K_uji)
    print("   C = E(%016X, %016X) = %s   (resmi: 85E813540F0AB405)"
          % (P_uji, K_uji, ke_hex(C)))
    kembali = dekripsi(int(ke_hex(C), 16), K_uji)
    print("   P = D(C, K)          = %s   (harus sama dengan plainteks)" % ke_hex(kembali))

    print()
    print("2. Subkunci pertama")
    K = kunci_putaran(K_uji)
    print("   K1 = %s" % ke_hex(K[0]))
    print("   K2 = %s" % ke_hex(K[1]))

    print()
    print("3. Jejak putaran (L_i, R_i)")
    for i, (L, R) in enumerate(daftar_putaran(P_uji, K_uji)):
        print("   %2d | %s | %s" % (i, ke_hex(L), ke_hex(R)))

    print()
    print("4. Putaran pertama, langkah demi langkah")
    L0, R0 = daftar_putaran(P_uji, K_uji)[0]
    print("   L0    = %s" % ke_hex(L0))
    print("   R0    = %s" % ke_hex(R0))
    print("   E(R0) = %s" % ke_hex(permutasi(R0, E)))
    print("   E^K1  = %s" % ke_hex(xor(permutasi(R0, E), K[0])))
    x = xor(permutasi(R0, E), K[0])
    keluaran = []
    for j in range(8):
        grup = x[j * 6:j * 6 + 6]
        baris = grup[0] * 2 + grup[5]
        kolom = int("".join(map(str, grup[1:5])), 2)
        nilai = S[j][baris][kolom]
        keluaran += ke_bit(nilai, 4)
        print("   S%d(%s) -> baris %d kolom %2d -> %2d = %s"
              % (j + 1, ke_teks(grup), baris, kolom, nilai, ke_teks(ke_bit(nilai, 4))))
    print("   S-out = %s" % ke_hex(keluaran))
    print("   P(S)  = %s" % ke_hex(permutasi(keluaran, P)))

    print()
    print("5. Kunci lemah: semua subkunci harus sama")
    daftar_lemah = [0x0101010101010101, 0x1F1F1F1F0E0E0E0E,
                    0xE0E0E0E0F1F1F1F1, 0xFEFEFEFEFEFEFEFE]
    for wk in daftar_lemah:
        kk = kunci_putaran(wk)
        sama = len(set(ke_hex(v) for v in kk)) == 1
        print("   %016X -> subkunci identik: %s (K1 = %s)"
              % (wk, "ya" if sama else "tidak", ke_hex(kk[0])))

    print()
    print("6. Kunci semi-lemah: subkunci kedua kunci harus terbalik")
    pasangan = [(0x01FE01FE01FE01FE, 0xFE01FE01FE01FE01),
                (0x1FE01FE00EF10EF1, 0xE01FE01FF10EF10E),
                (0x01E001E001F101F1, 0xE001E001F101F101),
                (0x1FFE1FFE0EFE0EFE, 0xFE1FFE1FFE0EFE0E),
                (0x011F011F010E010E, 0x1F011F010E010E01),
                (0xE0FEE0FEF1FEF1FE, 0xFEE0FEE0FEF1FEF1)]
    for a, b in pasangan:
        ka = [ke_hex(v) for v in kunci_putaran(a)]
        kb = [ke_hex(v) for v in kunci_putaran(b)]
        print("   %016X / %016X -> terbalik: %s"
              % (a, b, "ya" if kb == ka[::-1] else "tidak"))

    print()
    print("7. Efek longsoran: satu bit plainteks dibalik")
    dasar = enkripsi(P_uji, K_uji)
    ubah = enkripsi(P_uji ^ (1 << 63), K_uji)
    beda = sum(1 for a, b in zip(dasar, ubah) if a != b)
    print("   C        = %s" % ke_hex(dasar))
    print("   C'       = %s" % ke_hex(ubah))
    print("   bit berbeda = %d dari 64" % beda)
