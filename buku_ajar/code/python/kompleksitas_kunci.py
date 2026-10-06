"""Perhitungan waktu brute force DES, Double DES, dan AES-128.

Sesuai Aktivitas 7.1: membandingkan waktu pencarian kunci secara menyeluruh
(exhaustive key search) untuk panjang kunci yang berbeda.

Jalankan: python kompleksitas_kunci.py
"""

KECEPATAN = 1_000_000_000  # kunci per detik, sesuai Aktivitas 7.1

# Tiap langkah: bagi nilai dengan faktor, lalu satuan berganti ke nama berikut.
LANGKAH = [
    (60.0, "menit"),
    (60.0, "jam"),
    (24.0, "hari"),
    (365.25, "tahun"),
    (1000.0, "ribu tahun"),
    (1000.0, "juta tahun"),
    (1000.0, "miliar tahun"),
]


def ke_satuan_manusiawi(detik):
    """Ubah detik menjadi satuan waktu yang mudah dibaca manusia."""
    nilai, nama = detik, "detik"
    for faktor, nama_berikut in LANGKAH:
        if nilai < faktor:
            return f"{nilai:,.2f} {nama}"
        nilai /= faktor
        nama = nama_berikut
    return f"{nilai:,.2e} {nama}"


def waktu_brute_force(panjang_kunci, kecepatan=KECEPATAN):
    """Waktu terburuk pencarian menyeluruh: seluruh ruang kunci dicoba."""
    return (2 ** panjang_kunci) / kecepatan


if __name__ == "__main__":
    print(f"Asumsi kecepatan penyerang: {KECEPATAN:,} kunci per detik")
    print()

    # (nama, panjang kunci, panjang efektif, ruang kunci efektif)
    # Panjang efektif inilah yang menentukan waktu pencarian: Double DES hanya
    # menyisakan 2^57 karena serangan meet-in-the-middle (Bab 7 bagian 3),
    # sedangkan Triple DES dua kunci menyisakan 2^112.
    percobaan = [
        ("DES", 56, 56, "2^56"),
        ("Double DES", 112, 57, "2^57 efektif"),
        ("Triple DES", 168, 112, "2^112 efektif"),
        ("AES-128", 128, 128, "2^128"),
        ("AES-256", 256, 256, "2^256"),
    ]

    print(f"{'Algoritma':<13}{'Kunci':<8}{'Ruang kunci':<18}{'Waktu'}")
    print("-" * 70)
    for nama, panjang, efektif, ruang in percobaan:
        detik = waktu_brute_force(efektif)
        label_kunci = f"{panjang} bit"
        print(f"{nama:<13}{label_kunci:<8}{ruang:<18}{ke_satuan_manusiawi(detik)}")

    print()
    print("Catatan: Double DES hanya menambah satu bit keamanan efektif "
          "(2^57, bukan 2^112)")
    print("karena serangan meet-in-the-middle. Karena itu, memperpanjang kunci "
          "(AES-128)")
    print("jauh lebih efektif daripada mengulang algoritma yang sama.")
