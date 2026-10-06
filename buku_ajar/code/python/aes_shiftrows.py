"""Simulasi tahap ShiftRows pada matriks state AES.

Sesuai Aktivitas 8.1: blok 16 byte dipetakan ke matriks state 4 x 4, lalu baris
ke-r digeser siklik ke kiri sejauh r byte (baris 0 tetap, baris 1 geser 1 byte,
baris 2 geser 2 byte, baris 3 geser 3 byte).

Jalankan: python aes_shiftrows.py
"""

BLOK = b"Kriptografi-AES!"  # tepat 16 byte, satu blok AES

BARIS = 4
KOLOM = 4


def ke_state(blok):
    """Petakan 16 byte ke state 4 x 4 dengan pengisian kolom demi kolom.

    Byte ke-i masuk ke state[i mod 4][i div 4], sama seperti AES: empat byte
    pertama mengisi kolom pertama, empat byte berikutnya kolom kedua, dan
    seterusnya.
    """
    if len(blok) != BARIS * KOLOM:
        raise ValueError("Blok harus tepat 16 byte")
    return [[blok[KOLOM * kolom + baris] for kolom in range(KOLOM)]
            for baris in range(BARIS)]


def dari_state(state):
    """Kebalikan ke_state: susun kembali 16 byte dari matriks."""
    return bytes(state[baris][kolom]
                 for kolom in range(KOLOM) for baris in range(BARIS))


def shift_rows(state):
    """Geser baris ke-r siklik ke kiri sejauh r byte."""
    return [baris[r:] + baris[:r] for r, baris in enumerate(state)]


def inv_shift_rows(state):
    """Kebalikan ShiftRows: geser baris ke-r siklik ke kanan sejauh r byte."""
    return [baris[-r:] + baris[:-r] for r, baris in enumerate(state)]


def tampilkan(state, judul):
    """Cetak matriks sebagai karakter sekaligus nomor byte aslinya."""
    print(judul)
    for baris in state:
        print("   ", " ".join(f"{byte:>2}" for byte in baris),
              "   ", "".join(chr(byte) for byte in baris))
    print()


if __name__ == "__main__":
    state_awal = ke_state(BLOK)
    state_geser = shift_rows(state_awal)
    state_kembali = inv_shift_rows(state_geser)

    print("Blok plainteks :", BLOK.decode())
    print("Panjang        :", len(BLOK), "byte")
    print()

    # Matriks nomor byte 0..15, supaya perpindahan posisi mudah dilihat.
    posisi = [[KOLOM * kolom + baris for kolom in range(KOLOM)]
              for baris in range(BARIS)]
    print("Nomor byte pada state awal (sebelum ShiftRows):")
    for baris in posisi:
        print("   ", " ".join(f"{n:>2}" for n in baris))
    print()

    tampilkan(state_awal, "State awal (baris, kolom):")
    tampilkan(state_geser, "Setelah ShiftRows:")
    tampilkan(state_kembali, "Setelah InvShiftRows (kembali ke awal):")

    print("Baris 0 tidak bergeser, baris 1 bergeser 1 byte, baris 2 bergeser")
    print("2 byte, dan baris 3 bergeser 3 byte. Akibatnya byte-byte dari satu")
    print("kolom yang sama menyebar ke empat kolom berbeda. Inilah difusi:")
    print("perubahan satu byte cepat memengaruhi seluruh state pada putaran")
    print("berikutnya.")
    print()
    print("InvShiftRows mengembalikan susunan semula:",
          dari_state(state_kembali) == BLOK)
