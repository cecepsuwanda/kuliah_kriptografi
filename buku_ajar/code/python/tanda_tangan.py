"""Tanda tangan digital RSA: penandatanganan, verifikasi, dan uji pemalsuan.

Melengkapi Aktivitas 16.1. Alur yang dipakai sama seperti pada Bab 16:
pesan di-hash lebih dulu, nilai hash ditandatangani dengan kunci privat
pengirim, dan penerima memverifikasinya dengan kunci publik pengirim.

Pasangan kunci diambil dari Contoh Terhitung Bab 10 (p = 47, q = 71, e = 79,
d = 1019) supaya hasilnya dapat diperiksa dengan angka yang sudah dikenal.

Jalankan: python tanda_tangan.py
"""

import hashlib


def invers_modulo(e, phi):
    """Cari d sehingga e * d = 1 (mod phi)."""
    lama_d, d = 0, 1
    lama_phi, phi_sisa = phi, e
    while phi_sisa:
        hasil_bagi = lama_phi // phi_sisa
        lama_d, d = d, lama_d - hasil_bagi * d
        lama_phi, phi_sisa = phi_sisa, lama_phi - hasil_bagi * phi_sisa
    if lama_phi != 1:
        raise ValueError("e tidak relatif prima terhadap phi(n)")
    return lama_d % phi


def hash_pesan(pesan, n=None):
    """Hash SHA-256 dari pesan sebagai bilangan bulat.

    Bila n diberikan, nilai hash dipangkas modulo n. Pada RSA nyata n
    berukuran 2048 bit atau lebih sehingga digest 256 bit muat tanpa
    pemangkasan; di sini modulusnya kecil, jadi pemangkasan diperlukan.
    """
    nilai = int(hashlib.sha256(pesan.encode("utf-8")).hexdigest(), 16)
    return nilai if n is None else nilai % n


def tanda_tangani(pesan, d, n):
    """Buat tanda tangan: S = hash(pesan)^d mod n, memakai kunci privat."""
    return pow(hash_pesan(pesan, n), d, n)


def verifikasi(pesan, tanda_tangan, e, n):
    """Verifikasi tanda tangan.

    Nilai hash yang dipulihkan dengan kunci publik dibandingkan dengan hash
    pesan yang diterima. Bila sama, tanda tangan sah.
    """
    hash_dipulihkan = pow(tanda_tangan, e, n)
    hash_dihitung = hash_pesan(pesan, n)
    return hash_dipulihkan == hash_dihitung


if __name__ == "__main__":
    # Kunci Bob: publik untuk memverifikasi, privat untuk menandatangani.
    p, q, e = 47, 71, 79
    n = p * q
    d = invers_modulo(e, (p - 1) * (q - 1))

    print(f"Kunci publik  (e, n) = ({e}, {n})")
    print(f"Kunci privat  (d, n) = ({d}, {n})")
    print()

    pesan = "Transfer Rp5.000.000 ke rekening 1234567890"
    tanda_tangan = tanda_tangani(pesan, d, n)

    print("Pesan        :", pesan)
    print("Hash (mod n) :", hash_pesan(pesan, n))
    print("Tanda tangan :", tanda_tangan)
    print()
    print("Verifikasi pesan asli        :",
          verifikasi(pesan, tanda_tangan, e, n))
    print()

    # Penyerang mengubah isi pesan, tetapi tanda tangannya tetap yang lama.
    pesan_palsu = "Transfer Rp5.000.000 ke rekening 9999999999"
    print("Pesan diubah :", pesan_palsu)
    print("Hash (mod n) :", hash_pesan(pesan_palsu, n))
    print("Verifikasi pesan yang diubah :",
          verifikasi(pesan_palsu, tanda_tangan, e, n))
    print()

    print("Tanda tangan tidak lagi cocok karena hash pesan yang diubah berbeda")
    print("dari nilai hash yang dipulihkan dengan kunci publik. Penyerang yang")
    print("ingin memalsukan tanda tangan harus menemukan kolisi SHA-256, yaitu")
    print("dua pesan berbeda dengan hash sama, dan itu tidak praktis. Inilah")
    print("yang memberi sifat nirpenyangkalan (non-repudiation): hanya pemegang")
    print("kunci privat yang dapat membuat tanda tangan yang sah.")
