"""Stream cipher sederhana berbasis XOR dan demonstrasi efek bit-flip.

Sesuai Aktivitas 5.1: pesan dan kunci di-XOR bit per bit, lalu ditunjukkan
apa yang terjadi pada plainteks hasil dekripsi bila satu bit cipherteks diubah.

Jalankan: python stream_cipher.py
"""


def ke_biner(teks):
    """Ubah teks menjadi string biner 8 bit per karakter."""
    return "".join(format(ord(karakter), "08b") for karakter in teks)


def dari_biner(biner):
    """Ubah string biner (kelipatan 8 bit) kembali menjadi teks."""
    potongan = [biner[i:i + 8] for i in range(0, len(biner), 8)]
    return "".join(chr(int(potongan[i], 2)) for i in range(len(potongan)))


def xor_biner(biner_a, biner_b):
    """XOR dua string biner dengan panjang sama."""
    return "".join("1" if a != b else "0" for a, b in zip(biner_a, biner_b))


if __name__ == "__main__":
    plainteks = "KRIPTO"
    kunci = "RAHASI"          # panjang kunci harus sama dengan panjang pesan

    if len(kunci) != len(plainteks):
        raise ValueError("Panjang kunci harus sama dengan panjang plainteks")

    biner_plainteks = ke_biner(plainteks)
    biner_kunci = ke_biner(kunci)

    # Enkripsi dan dekripsi adalah operasi yang sama: XOR dengan kunci.
    cipherteks = xor_biner(biner_plainteks, biner_kunci)
    hasil_dekripsi = dari_biner(xor_biner(cipherteks, biner_kunci))

    print("Plainteks      :", plainteks)
    print("Kunci          :", kunci)
    print("Biner plainteks:", biner_plainteks)
    print("Biner kunci    :", biner_kunci)
    print("Biner cipher   :", cipherteks)
    print("Dekripsi       :", hasil_dekripsi)
    print()

    # Ubah bit pertama cipherteks, lalu dekripsi kembali.
    cipherteks_rusak = ("1" if cipherteks[0] == "0" else "0") + cipherteks[1:]
    hasil_rusak = dari_biner(xor_biner(cipherteks_rusak, biner_kunci))
    print("Cipherteks dengan bit pertama dibalik:", cipherteks_rusak)
    print("Hasil dekripsinya                   :", hasil_rusak)
    print()
    print("Perhatikan bahwa satu bit yang berubah hanya merusak satu karakter.")
    print("Pada mode operasi seperti CBC, kesalahan itu menjalar ke blok berikutnya.")
