# ------------------------------------------------------------------
# hash_uji.py -- verifikasi angka Bab 15 (Fungsi Hash dan MAC)
# ------------------------------------------------------------------
# Seluruh nilai yang tercantum pada bab diuji ulang di sini: jejak
# kompresi SHA-256 untuk pesan "abc", aturan padding Merkle-Damgard,
# serangan panjang-ekstensi, vektor uji HMAC-SHA-256 RFC 4231, dan
# batas ulang tahun (birthday bound).
#
# SHA-256 dan HMAC ditulis dari awal supaya setiap putaran dapat
# diperiksa, lalu hasilnya dicocokkan dengan modul hashlib dan hmac
# dari pustaka standar Python.
#
# Jalankan: python hash_uji.py
# ------------------------------------------------------------------

import hashlib
import hmac
import math
import struct


# ------------------------------------------------------------------
# Bagian 1: implementasi SHA-256 dari definisi
# ------------------------------------------------------------------

# Akar pangkat tiga 64 bilangan prima pertama (FIPS 180-4).
KONSTANTA_K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# Bagian pecahan akar kuadrat 8 bilangan prima pertama.
NILAI_AWAL = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
]

MASK32 = 0xFFFFFFFF


def putar_kanan(x, n):
    """Pergeseran berputar ke kanan sebanyak n bit pada kata 32 bit."""
    return ((x >> n) | (x << (32 - n))) & MASK32


def jadwal_pesan(blok):
    """Bangkitkan W[0..63] dari satu blok 512 bit (Persamaan jadwal)."""
    w = list(struct.unpack(">16I", blok))
    for t in range(16, 64):
        s0 = (putar_kanan(w[t - 15], 7) ^ putar_kanan(w[t - 15], 18)
              ^ (w[t - 15] >> 3))
        s1 = (putar_kanan(w[t - 2], 17) ^ putar_kanan(w[t - 2], 19)
              ^ (w[t - 2] >> 10))
        w.append((s1 + w[t - 7] + s0 + w[t - 16]) & MASK32)
    return w


def kompresi(keadaan, w, jejak=None):
    """Jalankan 64 putaran kompresi. Bila jejak diisi dict, catat a dan e."""
    a, b, c, d, e, f, g, h = keadaan
    for t in range(64):
        sigma1 = (putar_kanan(e, 6) ^ putar_kanan(e, 11)
                  ^ putar_kanan(e, 25))
        ch = (e & f) ^ ((~e & MASK32) & g)
        t1 = (h + sigma1 + ch + KONSTANTA_K[t] + w[t]) & MASK32
        sigma0 = (putar_kanan(a, 2) ^ putar_kanan(a, 13)
                  ^ putar_kanan(a, 22))
        maj = (a & b) ^ (a & c) ^ (b & c)
        t2 = (sigma0 + maj) & MASK32
        h, g, f, e = g, f, e, (d + t1) & MASK32
        d, c, b, a = c, b, a, (t1 + t2) & MASK32
        if jejak is not None:
            jejak.setdefault(t + 1, (a, e))
    return [(x + y) & MASK32 for x, y in zip(keadaan,
                                             (a, b, c, d, e, f, g, h))]


def padding(pesan, panjang_bit=None):
    """Aturan padding Merkle-Damgard: 1 bit, lalu 0, lalu panjang 64 bit."""
    if panjang_bit is None:
        panjang_bit = len(pesan) * 8
    hasil = pesan + b"\x80"
    while len(hasil) % 64 != 56:
        hasil += b"\x00"
    return hasil + struct.pack(">Q", panjang_bit)


def sha256(pesan, jejak=None):
    """Digest SHA-256 sebagai daftar 8 kata."""
    blok_penuh = padding(pesan)
    keadaan = list(NILAI_AWAL)
    for offset in range(0, len(blok_penuh), 64):
        w = jadwal_pesan(blok_penuh[offset:offset + 64])
        keadaan = kompresi(keadaan, w, jejak)
    return keadaan


def ke_hex(kata):
    """Ubah daftar kata 32 bit menjadi untai heksadesimal."""
    return "".join(f"{x:08x}" for x in kata)


def lanjutkan_dari_digest(digest_hex, tambahan, panjang_total_byte):
    """Serangan panjang-ekstensi: lanjutkan kompresi dari digest yang sah.

    digest_hex         : keadaan internal yang diketahui penyerang
    tambahan           : pesan yang ingin ditempelkan penyerang
    panjang_total_byte : panjang seluruh pesan palsu, untuk padding-nya
    """
    keadaan = list(struct.unpack(">8I", bytes.fromhex(digest_hex)))
    blok_penuh = padding(tambahan, panjang_total_byte * 8)
    for offset in range(0, len(blok_penuh), 64):
        w = jadwal_pesan(blok_penuh[offset:offset + 64])
        keadaan = kompresi(keadaan, w)
    return ke_hex(keadaan)


# ------------------------------------------------------------------
# Bagian 2: HMAC dari definisi
# ------------------------------------------------------------------

def hmac_sha256(kunci, pesan):
    """HMAC menurut RFC 2104, memakai sha256() di atas."""
    b = 64  # ukuran blok SHA-256 dalam byte
    if len(kunci) > b:
        kunci = bytes.fromhex(ke_hex(sha256(kunci)))
    kunci = kunci + b"\x00" * (b - len(kunci))
    ipad = bytes(x ^ 0x36 for x in kunci)
    opad = bytes(x ^ 0x5C for x in kunci)
    dalam = ke_hex(sha256(ipad + pesan))
    return ke_hex(sha256(opad + bytes.fromhex(dalam)))


# ------------------------------------------------------------------
# Bagian 3: pengujian
# ------------------------------------------------------------------

def garis(judul):
    print()
    print(judul)
    print("-" * len(judul))


def uji_panjang_padding(pesan, panjang_bit):
    """Hitung berapa blok yang terbentuk menurut aturan padding."""
    k = (-(panjang_bit + 1 + 64)) % 512
    total = panjang_bit + 1 + k + 64
    print(f"  panjang {panjang_bit:>5} bit -> k = {k:>3} nol, "
          f"total {total:>5} bit = {total // 512} blok")


def main():
    garis("1. Jejak kompresi SHA-256 untuk pesan 'abc'")
    jejak = {}
    kata = sha256(b"abc", jejak)
    for putaran in (1, 2, 16, 32, 48, 64):
        a, e = jejak[putaran]
        print(f"  putaran {putaran:>2}: a = {a:08x}  e = {e:08x}")
    print(f"  digest      : {ke_hex(kata)}")
    print(f"  hashlib     : {hashlib.sha256(b'abc').hexdigest()}")
    cocok = ke_hex(kata) == hashlib.sha256(b"abc").hexdigest()
    print(f"  cocok       : {cocok}")

    garis("2. Aturan padding Merkle-Damgard")
    uji_panjang_padding(b"abc", 24)
    uji_panjang_padding("A" * 125, 1000)
    uji_panjang_padding("A" * 56, 448)

    garis("3. Serangan panjang-ekstensi pada SHA-256")
    kunci = b"kunci"
    pesan = b"pesan"
    tambahan = b"&penerima=Budi"

    tag_asli = hashlib.sha256(kunci + pesan).hexdigest()
    print(f"  K                : {kunci!r} (penyerang tidak tahu isinya)")
    print(f"  m                : {pesan!r}")
    print(f"  H(K||m)          : {tag_asli}")

    blok_palsu = padding(kunci + pesan)
    pesan_palsu = blok_palsu + tambahan
    print(f"  panjang pesan palsu: {len(pesan_palsu)} byte "
          f"({len(blok_palsu)} + {len(tambahan)})")

    tag_palsu = lanjutkan_dari_digest(tag_asli, tambahan, len(pesan_palsu))
    print(f"  tag palsu (dihitung): {tag_palsu}")
    print(f"  H(pesan palsu)      : "
          f"{hashlib.sha256(pesan_palsu).hexdigest()}")
    print(f"  cocok               : "
          f"{tag_palsu == hashlib.sha256(pesan_palsu).hexdigest()}")
    print("  Penyerang tidak pernah mengetahui satu byte pun dari kunci.")

    garis("4. HMAC-SHA-256: vektor uji RFC 4231")
    pesan_panjang = b"Test Using Larger Than Block-Size Key - Hash Key First"
    vektor = [
        (1, b"\x0b" * 20, b"Hi There"),
        (2, b"Jefe", b"what do ya want for nothing?"),
        (3, b"\xaa" * 20, b"\xdd" * 50),
        (4, bytes(range(1, 26)), b"\xcd" * 50),
        (6, b"\xaa" * 131, pesan_panjang),
    ]
    semua_cocok = True
    for nomor, kunci_uji, pesan_uji in vektor:
        milik_kita = hmac_sha256(kunci_uji, pesan_uji)
        rujukan = hmac.new(kunci_uji, pesan_uji,
                           hashlib.sha256).hexdigest()
        cocok = milik_kita == rujukan
        semua_cocok = semua_cocok and cocok
        print(f"  TC{nomor}: {milik_kita}")
        print(f"       cocok dengan hmac.new: {cocok}")
    print(f"  semua vektor cocok: {semua_cocok}")
    print("  TC6 memakai kunci 131 byte, melebihi blok 64 byte, sehingga")
    print("  cabang H(K) pada aturan panjang kunci ikut teruji.")

    garis("5. Batas ulang tahun (birthday bound)")
    for n in (128, 160, 256, 512):
        akar = 2.0 ** (n / 2)
        k50 = math.sqrt(2 * math.log(2)) * akar
        print(f"  n = {n:>3}: 2^(n/2) = {akar:.6g}  "
              f"k(50%) = {k50:.6g}")
    print("  Faktor sqrt(2 ln 2) = "
          f"{math.sqrt(2 * math.log(2)):.6f}")
    print("  Peluang pada k = 2^(n/2) adalah 1 - exp(-1/2) = "
          f"{1 - math.exp(-0.5):.4f}")

    garis("6. Perbandingan tag secara waktu-konstan")
    tag_a = bytes.fromhex(hmac_sha256(b"kunci", b"pesan"))
    tag_b = bytearray(tag_a)
    tag_b[-1] ^= 0x01  # satu byte terakhir diubah

    def naif(x, y):
        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True

    def waktu_konstan(x, y):
        beda = 0
        for i in range(len(x)):
            beda |= x[i] ^ y[i]
        return beda == 0

    print(f"  tag sah     : {tag_a.hex()}")
    print(f"  tag diubah  : {bytes(tag_b).hex()}")
    print(f"  cara naif   : {naif(tag_a, bytes(tag_b))}")
    print(f"  waktu-konstan: {waktu_konstan(tag_a, bytes(tag_b))}")
    print("  Keduanya menolak, tetapi cara naif berhenti pada byte pertama")
    print("  yang berbeda, sehingga lama pemeriksaan membocorkan berapa")
    print("  byte awal tag yang sudah benar.")


if __name__ == "__main__":
    main()
