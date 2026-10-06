"""Demonstrasi kebocoran pola pada mode ECB dibandingkan mode CBC.

Sesuai Aktivitas 6.1: blok plainteks yang identik menghasilkan blok cipherteks
yang identik pada ECB, sedangkan pada CBC hasilnya berbeda karena tiap blok
di-XOR lebih dulu dengan cipherteks blok sebelumnya.

Untuk kejelasan, block cipher-nya diganti dengan permutasi sederhana
(block cipher mainan). Tujuannya menunjukkan perilaku mode, bukan kekuatan
algoritmanya.

Jalankan: python mode_operasi.py
"""

BLOCK = 4  # ukuran blok dalam karakter


def kunci_putaran(blok, kunci):
    """Block cipher mainan: XOR dengan kunci yang bergeser tiap posisi, lalu putar.

    Kunci bergeser per posisi (kunci + indeks) supaya tiap posisi dalam blok
    mendapat nilai berbeda. Penyandian tetap dapat dibalik, sehingga hasilnya
    sah sebagai block cipher walau sengaja dibuat lemah.
    """
    tergeser = "".join(
        chr((ord(karakter) ^ (kunci + posisi)) & 0x7F)
        for posisi, karakter in enumerate(blok)
    )
    return tergeser[1:] + tergeser[0]


def bagi_blok(teks):
    """Potong teks menjadi blok berukuran tetap, tambah padding bila perlu."""
    padding = (-len(teks)) % BLOCK
    teks += " " * padding
    return [teks[i:i + BLOCK] for i in range(0, len(teks), BLOCK)]


def tambah_xor(blok_a, blok_b):
    """XOR dua blok karakter per karakter."""
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(blok_a, blok_b))


def enkripsi_ecb(plainteks, kunci):
    """Setiap blok dienkripsi sendiri-sendiri, tanpa kaitan antar blok."""
    return [kunci_putaran(blok, kunci) for blok in bagi_blok(plainteks)]


def enkripsi_cbc(plainteks, kunci, iv):
    """Setiap blok di-XOR dengan cipherteks sebelumnya sebelum dienkripsi."""
    hasil = []
    sebelumnya = iv
    for blok in bagi_blok(plainteks):
        blok_cipher = kunci_putaran(tambah_xor(blok, sebelumnya), kunci)
        hasil.append(blok_cipher)
        sebelumnya = blok_cipher
    return hasil


if __name__ == "__main__":
    # Pola berulang yang mencolok, seperti area warna rata pada sebuah gambar.
    plainteks = "AAAAAAAABBBBBBBBAAAAAAAA"
    kunci = 0x5A
    iv = "INIT"

    blok_ecb = enkripsi_ecb(plainteks, kunci)
    blok_cbc = enkripsi_cbc(plainteks, kunci, iv)

    def tampilkan_hex(blok):
        """Tampilkan blok sebagai heksadesimal agar tiap byte terbaca jelas."""
        return " ".join(f"{ord(karakter):02X}" for karakter in blok)

    print("Plainteks   :", plainteks)
    print("Blok        :", " | ".join(bagi_blok(plainteks)))
    print()
    print("ECB (blok identik -> cipher identik):")
    for blok in blok_ecb:
        print("  ", tampilkan_hex(blok))
    print()
    print("CBC (blok identik -> cipher berbeda):")
    for blok in blok_cbc:
        print("  ", tampilkan_hex(blok))
    print()
    print("Pada ECB, blok 1 dan 2 (AAAA) menghasilkan cipherteks yang sama,")
    print("demikian pula blok 3 dan 4 (BBBB), sehingga pola data asli terbaca.")
    print("Pada CBC, setiap blok terkait dengan blok sebelumnya, sehingga")
    print("blok yang sama menghasilkan cipherteks yang berbeda.")
