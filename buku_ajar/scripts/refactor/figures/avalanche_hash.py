"""Membuat gambar efek longsoran (avalanche effect) SHA-256.

Menampilkan digest 256 bit dari dua pesan yang berbeda satu huruf sebagai
petak 16 x 16; petak ketiga menyorot bit yang berubah di antara keduanya.

Angka yang dipakai (dihitung ulang setiap kali skrip dijalankan):
    digest("Kriptografi itu Menyenangkan") = ...
    digest("Kriptografi itu menyenangkan") = ...
Bit yang berbeda dicetak ke layar agar dapat dicocokkan dengan teks bab.

Keluaran: buku_ajar/chapters/15/figures/longsoran-sha256.png

Skrip ini hanya memakai pustaka standar (hashlib, zlib, struct), sehingga
dapat dijalankan tanpa matplotlib. Gambar dilukis piksel demi piksel.

Jalankan dari mana saja:
    python -I avalanche_hash.py
"""

import hashlib
import os
import struct
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(
    os.path.join(HERE, "..", "..", "..", "chapters", "15", "figures",
                 "longsoran-sha256.png")
)

PESAN_ASLI = "Kriptografi itu Menyenangkan"
PESAN_UBAH = "Kriptografi itu menyenangkan"

# --- tata letak (piksel) -----------------------------------------------------
BARIS = KOLOM = 16          # digest 256 bit = 16 x 16 petak
PETAK = 13                   # ukuran satu bit
PITCH = 14                   # jarak antar titik awal petak (1 px celah)
PANEL = KOLOM * PITCH - 1    # 223
JARAK = 34                   # celah antar panel
MARGIN = 24
BAR_T = 10                   # tebal batang penanda di atas tiap panel
BAR_Y = 20
Y0 = BAR_Y + BAR_T + 10      # awal petak

LEBAR = 2 * MARGIN + 3 * PANEL + 2 * JARAK
TINGGI = Y0 + PANEL + 25

# --- warna -------------------------------------------------------------------
LATAR = (255, 255, 255)
BIT_NOL = (235, 240, 248)
BIT_SATU = (31, 71, 136)
SAMA = (226, 226, 226)
BEDA = (196, 30, 30)
BAR_ABU = (76, 114, 176)
BAR_MERAH = (196, 78, 82)
GARIS = (140, 150, 165)


def tulis_png(path, lebar, tinggi, piksel):
    """Menulis gambar RGB 8 bit tanpa pustaka luar selain zlib."""
    mentah = b"".join(
        b"\x00" + bytes(v for px in baris for v in px) for baris in piksel
    )

    def chunk(tipe, data):
        return (struct.pack(">I", len(data)) + tipe + data
                + struct.pack(">I", zlib.crc32(tipe + data) & 0xFFFFFFFF))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", lebar, tinggi, 8, 2, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(mentah, 9))
           + chunk(b"IEND", b""))
    with open(path, "wb") as f:
        f.write(png)


def bits(digest):
    """256 bit, bit paling berarti lebih dahulu, urut baris demi baris."""
    return [(byte >> (7 - i)) & 1 for byte in digest for i in range(8)]


def isi(piksel, x, y, w, h, warna):
    for baris in range(y, y + h):
        for kolom in range(x, x + w):
            piksel[baris][kolom] = warna


def gambar_panel(piksel, x0, data, warna_satu, warna_nol):
    for nomor, bit in enumerate(data):
        r, c = divmod(nomor, KOLOM)
        isi(piksel, x0 + c * PITCH, Y0 + r * PITCH, PETAK, PETAK,
            warna_satu if bit else warna_nol)
    # bingkai tipis mengelilingi panel
    for x in range(x0 - 1, x0 + PANEL + 1):
        piksel[Y0 - 1][x] = GARIS
        piksel[Y0 + PANEL][x] = GARIS
    for y in range(Y0 - 1, Y0 + PANEL + 1):
        piksel[y][x0 - 1] = GARIS
        piksel[y][x0 + PANEL] = GARIS


def main():
    digest_a = hashlib.sha256(PESAN_ASLI.encode("utf-8")).digest()
    digest_b = hashlib.sha256(PESAN_UBAH.encode("utf-8")).digest()
    bit_a, bit_b = bits(digest_a), bits(digest_b)
    bit_d = [1 if p != q else 0 for p, q in zip(bit_a, bit_b)]

    jumlah = sum(bit_d)
    print("H(pesan asli) =", digest_a.hex())
    print("H(pesan ubah) =", digest_b.hex())
    print("bit berbeda   = %d dari 256 (%.2f%%)" % (jumlah, 100 * jumlah / 256))
    print("byte berbeda  = %d dari 32"
          % sum(1 for p, q in zip(digest_a, digest_b) if p != q))

    piksel = [[LATAR] * LEBAR for _ in range(TINGGI)]

    x0 = MARGIN
    x1 = x0 + PANEL + JARAK
    x2 = x1 + PANEL + JARAK

    for x, warna in ((x0, BAR_ABU), (x1, BAR_ABU), (x2, BAR_MERAH)):
        isi(piksel, x, BAR_Y, PANEL, BAR_T, warna)

    gambar_panel(piksel, x0, bit_a, BIT_SATU, BIT_NOL)
    gambar_panel(piksel, x1, bit_b, BIT_SATU, BIT_NOL)
    gambar_panel(piksel, x2, bit_d, BEDA, SAMA)

    tulis_png(OUT, LEBAR, TINGGI, piksel)
    print("Ditulis:", OUT)
    print("Ukuran : %d x %d piksel" % (LEBAR, TINGGI))


if __name__ == "__main__":
    main()
