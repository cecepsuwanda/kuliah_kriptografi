"""Membuat Gambar 16.x: perbandingan ukuran kunci publik dan tanda tangan.

Empat skema dibandingkan pada tingkat keamanan yang setara, yaitu sekitar
128 bit (RSA-3072, DSA-3072, ECDSA P-256, dan Ed25519). Angka yang dipakai
adalah ukuran bahan kriptografis mentah, bukan panjang berkas DER:

    RSA-3072     : modulus 3072 bit = 384 byte, tanda tangan = 384 byte
    DSA-3072/256 : p = 384 byte, tanda tangan = 2 x 32 = 64 byte
    ECDSA P-256  : titik tak terkompresi 65 byte, tanda tangan = 2 x 32 byte
    Ed25519      : titik terkompresi 32 byte, tanda tangan = 64 byte

Keluaran: buku_ajar/chapters/16/figures/ukuran-tanda-tangan.png

Skrip ini hanya memakai pustaka baku Python (zlib, struct), tanpa matplotlib
dan tanpa Pillow, sehingga dapat dijalankan pada lingkungan mana pun.

Jalankan dari mana saja:
    python -I ukuran_tanda_tangan.py
"""

import os
import struct
import zlib

# ---------------------------------------------------------------- data gambar

BARIS = [
    ("RSA-3072", 384, 384),
    ("DSA-3072", 384, 64),
    ("ECDSA P-256", 65, 64),
    ("ED25519", 32, 64),
]

MAKS = 384                        # nilai terbesar pada sumbu byte

KUNCI_RGB = (76, 114, 176)        # biru, sama dengan gambar bab lain
TANDA_RGB = (196, 78, 82)         # merah
GRID_RGB = (221, 221, 221)
TEKS_RGB = (51, 51, 51)
LATAR_RGB = (255, 255, 255)

SKALA_TEKS = 2                    # satu piksel font menjadi 2x2 piksel citra
LEBAR_KAR = 5 * SKALA_TEKS + 2    # 12
TINGGI_KAR = 7 * SKALA_TEKS      # 14

LABEL_W = 140                     # ruang untuk nama algoritma
AREA_W = 420                      # ruang untuk 0..384 byte
SISA_W = 72                       # ruang untuk label nilai di ujung batang
LEBAR = LABEL_W + AREA_W + SISA_W  # 632

BAR_T = 14
BAR_GAP = 4
BARIS_T = 2 * BAR_T + BAR_GAP + 16  # 48
TOP_GRID = 44
TINGGI = TOP_GRID + len(BARIS) * BARIS_T + 38  # 274

# --------------------------------------------------------- font 5x7 (kolom)

FONT = {
    " ": [0x00, 0x00, 0x00, 0x00, 0x00],
    "-": [0x08, 0x08, 0x08, 0x08, 0x08],
    "0": [0x3E, 0x51, 0x49, 0x45, 0x3E],
    "1": [0x00, 0x42, 0x7F, 0x40, 0x00],
    "2": [0x42, 0x61, 0x51, 0x49, 0x46],
    "3": [0x21, 0x41, 0x45, 0x4B, 0x31],
    "4": [0x18, 0x14, 0x12, 0x7F, 0x10],
    "5": [0x27, 0x45, 0x45, 0x45, 0x39],
    "6": [0x3C, 0x4A, 0x49, 0x49, 0x30],
    "7": [0x01, 0x71, 0x09, 0x05, 0x03],
    "8": [0x36, 0x49, 0x49, 0x49, 0x36],
    "9": [0x06, 0x49, 0x49, 0x29, 0x1E],
    "A": [0x7E, 0x11, 0x11, 0x11, 0x7E],
    "B": [0x7F, 0x49, 0x49, 0x49, 0x36],
    "C": [0x3E, 0x41, 0x41, 0x41, 0x22],
    "D": [0x7F, 0x41, 0x41, 0x22, 0x1C],
    "E": [0x7F, 0x49, 0x49, 0x49, 0x41],
    "F": [0x7F, 0x09, 0x09, 0x01, 0x01],
    "G": [0x3E, 0x41, 0x41, 0x51, 0x32],
    "H": [0x7F, 0x08, 0x08, 0x08, 0x7F],
    "I": [0x00, 0x41, 0x7F, 0x41, 0x00],
    "J": [0x20, 0x40, 0x41, 0x3F, 0x01],
    "K": [0x7F, 0x08, 0x14, 0x22, 0x41],
    "L": [0x7F, 0x40, 0x40, 0x40, 0x40],
    "M": [0x7F, 0x02, 0x04, 0x02, 0x7F],
    "N": [0x7F, 0x04, 0x08, 0x10, 0x7F],
    "O": [0x3E, 0x41, 0x41, 0x41, 0x3E],
    "P": [0x7F, 0x09, 0x09, 0x09, 0x06],
    "Q": [0x3E, 0x41, 0x51, 0x21, 0x5E],
    "R": [0x7F, 0x09, 0x19, 0x29, 0x46],
    "S": [0x46, 0x49, 0x49, 0x49, 0x31],
    "T": [0x01, 0x01, 0x7F, 0x01, 0x01],
    "U": [0x3F, 0x40, 0x40, 0x40, 0x3F],
    "V": [0x1F, 0x20, 0x40, 0x20, 0x1F],
    "W": [0x7F, 0x20, 0x18, 0x20, 0x7F],
    "X": [0x63, 0x14, 0x08, 0x14, 0x63],
    "Y": [0x03, 0x04, 0x78, 0x04, 0x03],
    "Z": [0x61, 0x51, 0x49, 0x45, 0x43],
}


def gambar_teks(piksel, x, y, teks, warna):
    """Menuliskan teks dengan font 5x7 pada kanvas piksel."""
    for huruf in teks.upper():
        kolom = FONT.get(huruf, FONT[" "])
        for cx, bit_kolom in enumerate(kolom):
            for cy in range(7):
                if bit_kolom >> cy & 1:
                    for dy in range(SKALA_TEKS):
                        for dx in range(SKALA_TEKS):
                            py = y + cy * SKALA_TEKS + dy
                            px = x + cx * SKALA_TEKS + dx
                            if 0 <= py < TINGGI and 0 <= px < LEBAR:
                                piksel[py][px] = warna
        x += LEBAR_KAR
    return x


def kotak(piksel, x0, y0, x1, y1, warna):
    """Mengisi persegi panjang."""
    for y in range(max(0, y0), min(TINGGI, y1)):
        for x in range(max(0, x0), min(LEBAR, x1)):
            piksel[y][x] = warna


def panjang_batang(nilai):
    """Panjang batang dalam piksel; batang sekecil apa pun tetap terlihat."""
    return max(2, int(round(nilai * AREA_W / MAKS)))


def tulis_png(path, lebar, tinggi, piksel):
    mentah = b"".join(
        b"\x00" + bytes(v for px in baris for v in px) for baris in piksel
    )

    def chunk(tipe, data):
        return (struct.pack(">I", len(data)) + tipe + data
                + struct.pack(">I", zlib.crc32(tipe + data) & 0xFFFFFFFF))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", lebar, tinggi,
                                        8, 2, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(mentah, 9))
           + chunk(b"IEND", b""))
    with open(path, "wb") as berkas:
        berkas.write(png)


def main():
    piksel = [[LATAR_RGB] * LEBAR for _ in range(TINGGI)]

    # --- legenda di bagian atas ---
    kotak(piksel, LABEL_W, 16, LABEL_W + 22, 16 + 14, KUNCI_RGB)
    gambar_teks(piksel, LABEL_W + 28, 16, "KUNCI PUBLIK", TEKS_RGB)
    kotak(piksel, LABEL_W + 184, 16, LABEL_W + 206, 16 + 14, TANDA_RGB)
    gambar_teks(piksel, LABEL_W + 212, 16, "TANDA TANGAN", TEKS_RGB)

    # --- garis bantu sumbu byte ---
    for nilai in (0, 128, 256, 384):
        x = LABEL_W + int(round(nilai * AREA_W / MAKS))
        kotak(piksel, x, TOP_GRID - 6, x + 1, TOP_GRID + len(BARIS) * BARIS_T - 16,
              GRID_RGB)

    # --- batang dan label tiap algoritma ---
    for i, (nama, kunci, tanda) in enumerate(BARIS):
        atas = TOP_GRID + i * BARIS_T
        gambar_teks(piksel, 6, atas + 14, nama, TEKS_RGB)

        y1 = atas + BAR_T
        y2 = atas + BAR_T + BAR_GAP
        x1 = LABEL_W + panjang_batang(kunci)
        x2 = LABEL_W + panjang_batang(tanda)

        kotak(piksel, LABEL_W, atas, x1, y1, KUNCI_RGB)
        kotak(piksel, LABEL_W, y2, x2, y2 + BAR_T, TANDA_RGB)

        gambar_teks(piksel, x1 + 6, atas + 4, "%d B" % kunci, TEKS_RGB)
        gambar_teks(piksel, x2 + 6, y2 + 4, "%d B" % tanda, TEKS_RGB)

    # --- sumbu byte di bawah ---
    y_axis = TOP_GRID + len(BARIS) * BARIS_T - 16
    kotak(piksel, LABEL_W, y_axis, LABEL_W + AREA_W, y_axis + 1, TEKS_RGB)
    for nilai in (0, 128, 256, 384):
        x = LABEL_W + int(round(nilai * AREA_W / MAKS))
        kotak(piksel, x, y_axis, x + 1, y_axis + 5, TEKS_RGB)
        teks = str(nilai)
        gambar_teks(piksel, x - len(teks) * LEBAR_KAR // 2, y_axis + 8,
                    teks, TEKS_RGB)

    keluar = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..", "..", "chapters", "16", "figures",
        "ukuran-tanda-tangan.png"))
    tulis_png(keluar, LEBAR, TINGGI, piksel)
    print("Ditulis:", keluar, "(%dx%d)" % (LEBAR, TINGGI))
    for nama, kunci, tanda in BARIS:
        print("  %-12s kunci %3d B   tanda tangan %3d B" % (nama, kunci, tanda))


if __name__ == "__main__":
    main()
