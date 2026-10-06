"""Cipher Caesar: enkripsi, dekripsi, dan pemecahan dengan analisis frekuensi.

Menunjukkan mengapa cipher substitusi monoalfabetik mudah dipecahkan:
distribusi huruf cipherteks masih mencerminkan distribusi bahasa aslinya.

Jalankan: python caesar.py
"""

ABJAD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Urutan kemunculan huruf dalam bahasa Indonesia, dipakai sebagai tebakan awal.
URUTAN_BAHASA = "AENIRSTUDKMLGBOPWYHFCJZVXQ"


def enkripsi(plainteks, k):
    """Geser setiap huruf sejauh k posisi (Caesar cipher)."""
    hasil = []
    for huruf in plainteks.upper():
        if huruf in ABJAD:
            posisi = (ABJAD.index(huruf) + k) % 26
            hasil.append(ABJAD[posisi])
        else:
            hasil.append(huruf)
    return "".join(hasil)


def dekripsi(cipherteks, k):
    """Kebalikan enkripsi: geser balik sejauh k posisi."""
    return enkripsi(cipherteks, -k)


def hitung_frekuensi(teks):
    """Kembalikan pasangan (huruf, jumlah) terurut dari yang paling sering."""
    jumlah = {huruf: 0 for huruf in ABJAD}
    for huruf in teks.upper():
        if huruf in ABJAD:
            jumlah[huruf] += 1
    return sorted(jumlah.items(), key=lambda pasangan: pasangan[1], reverse=True)


def pecahkan(cipherteks):
    """Tebak kunci dengan menyelaraskan huruf tersering ke urutan bahasa.

    Huruf yang paling banyak muncul pada cipherteks dipasangkan dengan huruf
    yang paling banyak muncul pada bahasa, selisihnya menjadi dugaan kunci.
    """
    terurut = [huruf for huruf, jumlah in hitung_frekuensi(cipherteks) if jumlah > 0]
    if not terurut:
        return None, ""

    tebakan_kunci = (ABJAD.index(terurut[0]) - ABJAD.index(URUTAN_BAHASA[0])) % 26
    return tebakan_kunci, dekripsi(cipherteks, tebakan_kunci)


if __name__ == "__main__":
    plainteks = "KRIPTOGRAFI ADALAH ILMU DAN SENI MENJAGA KEAMANAN PESAN"
    kunci = 3

    cipherteks = enkripsi(plainteks, kunci)
    print("Plainteks :", plainteks)
    print("Kunci     :", kunci)
    print("Cipherteks:", cipherteks)
    print("Dekripsi  :", dekripsi(cipherteks, kunci))
    print()

    print("Frekuensi huruf cipherteks (10 teratas):")
    dicetak = 0
    for huruf, jumlah in hitung_frekuensi(cipherteks):
        if jumlah > 0 and dicetak < 10:
            print(f"  {huruf}: {jumlah}")
            dicetak += 1
    print()

    kunci_tebakan, hasil = pecahkan(cipherteks)
    print("Kunci hasil analisis frekuensi:", kunci_tebakan)
    print("Hasil pemecahan              :", hasil)
