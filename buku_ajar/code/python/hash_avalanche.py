"""Efek longsoran (avalanche effect) pada fungsi hash SHA-256.

Sesuai Aktivitas 15.1: dua kalimat yang berbeda satu karakter di-hash, lalu
jumlah bit keluaran yang berbeda dihitung. Fungsi hash di sini memakai modul
hashlib dari pustaka standar Python, bukan implementasi sendiri, karena SHA-256
dirancang untuk dipakai apa adanya.

Jalankan: python hash_avalanche.py
"""

import hashlib


def hash_sha256(teks):
    """Kembalikan digest SHA-256 sebagai string heksadesimal 64 karakter."""
    return hashlib.sha256(teks.encode("utf-8")).hexdigest()


def selisih_bit(heks_a, heks_b):
    """Hitung jumlah bit yang berbeda antara dua digest heksadesimal."""
    bit_a = bin(int(heks_a, 16))[2:].zfill(4 * len(heks_a))
    bit_b = bin(int(heks_b, 16))[2:].zfill(4 * len(heks_b))
    return sum(bit_x != bit_y for bit_x, bit_y in zip(bit_a, bit_b))


if __name__ == "__main__":
    pesan_a = "Kriptografi itu Menyenangkan"
    pesan_b = "Kriptografi itu menyenangkan"  # hanya satu karakter berbeda

    hash_a = hash_sha256(pesan_a)
    hash_b = hash_sha256(pesan_b)

    jumlah_bit = 4 * len(hash_a)  # 256 bit untuk SHA-256
    beda = selisih_bit(hash_a, hash_b)

    print("Pesan A :", pesan_a)
    print("Hash A  :", hash_a)
    print()
    print("Pesan B :", pesan_b)
    print("Hash B  :", hash_b)
    print()
    print(f"Ukuran digest        : {jumlah_bit} bit")
    print(f"Bit yang berbeda     : {beda} bit")
    print(f"Persentase perbedaan : {beda / jumlah_bit * 100:.1f}%")
    print()

    # Perubahan kecil lain, sebagai pembanding bahwa sifat ini konsisten.
    print("Perbandingan tambahan (satu karakter diubah pada tiap baris):")
    acuan = hash_sha256("Kriptografi")
    for varian in ["kriptografi", "Kriptografj", "Kriptografi ", "Kriptograf"]:
        uji = hash_sha256(varian)
        print(f"  {'Kriptografi':<14} vs {varian!r:<16}"
              f" -> {selisih_bit(acuan, uji):>3} bit berbeda")
    print()

    print("Jika keluaran hash bersifat acak, sekitar separuh bitnya (128 dari")
    print("256) diharapkan berbeda. Perubahan satu karakter saja sudah")
    print("mengubah sekitar separuh digest. Sifat inilah yang membuat hash")
    print("berguna untuk pemeriksaan keutuhan: perubahan sekecil apa pun pada")
    print("pesan langsung terdeteksi, dan penyerang tidak dapat menyusun pesan")
    print("lain dengan hash yang sama tanpa memecahkan sifat tahan-kolisi.")
