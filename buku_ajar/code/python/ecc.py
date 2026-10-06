"""Penjumlahan dan penggandaan titik pada kurva eliptik.

Sesuai Aktivitas 14.1 dan Contoh Terhitung Bab 14. Kurva ditulis dalam bentuk
umum y^2 = x^3 + a*x + b. Dua medan didukung:

- kurva atas bilangan real (p = None), memakai aritmetika pecahan biasa;
- kurva atas medan berhingga modulo prima p, memakai invers modulo.

Jalankan: python ecc.py
"""


def invers_modulo(nilai, p):
    """Invers perkalian nilai modulo p dengan Algoritma Euclidean diperluas."""
    return pow(nilai % p, p - 2, p)


class Kurva:
    """Kurva eliptik y^2 = x^3 + a*x + b, atas bilangan real atau modulo p."""

    def __init__(self, a, b, p=None):
        self.a = a
        self.b = b
        self.p = p
        # Kurva eliptik harus licin: 4a^3 + 27b^2 tidak boleh nol.
        if 4 * a ** 3 + 27 * b ** 2 == 0:
            raise ValueError("Parameter tidak sah: 4a^3 + 27b^2 = 0")

    def pada_kurva(self, titik):
        """Periksa apakah titik memenuhi persamaan kurva."""
        if titik is None:  # titik di ketakhinggaan
            return True
        x, y = titik
        kiri = y ** 2
        kanan = x ** 3 + self.a * x + self.b
        if self.p is None:
            return abs(kiri - kanan) < 1e-9
        return (kiri - kanan) % self.p == 0

    def _bagi(self, pembilang, penyebut):
        """Bagi dua bilangan pada medan yang dipakai kurva ini."""
        if self.p is None:
            return pembilang / penyebut
        return (pembilang * invers_modulo(penyebut, self.p)) % self.p

    def tambah(self, P, Q):
        """Hitung R = P + Q."""
        if P is None:
            return Q
        if Q is None:
            return P
        x1, y1 = P
        x2, y2 = Q

        if self.p is None:
            sama_x = abs(x1 - x2) < 1e-9
            lawan = abs(y1 + y2) < 1e-9
        else:
            sama_x = (x1 - x2) % self.p == 0
            lawan = (y1 + y2) % self.p == 0

        if sama_x:
            if lawan:  # P dan Q berlawanan: hasilnya titik di ketakhinggaan
                return None
            return self.gandakan(P)  # P == Q, pakai rumus penggandaan

        m = self._bagi(y2 - y1, x2 - x1)
        x3 = m ** 2 - x1 - x2
        y3 = m * (x1 - x3) - y1
        if self.p is not None:
            x3, y3 = x3 % self.p, y3 % self.p
        return (x3, y3)

    def gandakan(self, P):
        """Hitung R = 2P dengan rumus penggandaan titik."""
        if P is None:
            return None
        x1, y1 = P
        if self.p is None:
            nol_y = abs(y1) < 1e-9
        else:
            nol_y = y1 % self.p == 0
        if nol_y:  # garis singgungnya tegak: hasilnya titik di ketakhinggaan
            return None

        m = self._bagi(3 * x1 ** 2 + self.a, 2 * y1)
        x3 = m ** 2 - 2 * x1
        y3 = m * (x1 - x3) - y1
        if self.p is not None:
            x3, y3 = x3 % self.p, y3 % self.p
        return (x3, y3)

    def kali(self, k, P):
        """Hitung k*P dengan metode double-and-add."""
        hasil = None
        penambah = P
        while k > 0:
            if k & 1:
                hasil = self.tambah(hasil, penambah)
            penambah = self.gandakan(penambah)
            k >>= 1
        return hasil


def _angka(nilai, desimal=6):
    """Tampilkan bilangan tanpa nol berekor yang tidak perlu."""
    if not isinstance(nilai, float):
        return str(nilai)
    teks = f"{nilai:.{desimal}f}".rstrip("0").rstrip(".")
    return teks if teks not in ("", "-") else "0"  # menangani 0 dan -0


def format_titik(titik, desimal=6):
    """Ubah titik menjadi teks yang enak dibaca."""
    if titik is None:
        return "O (titik di ketakhinggaan)"
    x, y = titik
    return f"({_angka(x, desimal)}, {_angka(y, desimal)})"


if __name__ == "__main__":
    # --- Kurva atas bilangan real: contoh terhitung bab ---------------------
    kurva_real = Kurva(a=-3, b=3)
    P, Q = (1, 1), (-2, 1)
    print("Kurva y^2 = x^3 - 3x + 3")
    print("  P =", format_titik(P), " P pada kurva:", kurva_real.pada_kurva(P))
    print("  Q =", format_titik(Q), " Q pada kurva:", kurva_real.pada_kurva(Q))
    print("  P + Q =", format_titik(kurva_real.tambah(P, Q)),
          "(buku: (1, -1))")
    print("  2P    =", format_titik(kurva_real.gandakan(P)),
          "(buku: (-2, -1))")
    print()

    # --- Kurva dari Aktivitas 14.1 -----------------------------------------
    kurva_aktivitas = Kurva(a=2, b=4)
    P, Q = (2, 4), (0, 2)
    print("Kurva y^2 = x^3 + 2x + 4 (Aktivitas 14.1)")
    print("  P + Q =", format_titik(kurva_aktivitas.tambah(P, Q)))
    print("  2P    =", format_titik(kurva_aktivitas.gandakan(P)))
    print()

    # --- Kurva modulo prima 23 ---------------------------------------------
    kurva_mod = Kurva(a=1, b=1, p=23)
    P = (3, 10)
    dua_p = kurva_mod.gandakan(P)
    tiga_p = kurva_mod.tambah(dua_p, P)
    print("Kurva y^2 = x^3 + x + 1 (mod 23)")
    print("  P      =", format_titik(P), " P pada kurva:",
          kurva_mod.pada_kurva(P))
    print("  2P     =", format_titik(dua_p), "(buku: (7, 12))")
    print("  3P     =", format_titik(tiga_p), "(buku: (19, 5))")
    print()

    # --- Pertukaran kunci ECDH pada kurva yang sama -------------------------
    B = (3, 10)          # titik basis
    a_privat, b_privat = 2, 3
    PA = kurva_mod.kali(a_privat, B)
    PB = kurva_mod.kali(b_privat, B)
    K_alice = kurva_mod.kali(a_privat, PB)
    K_bob = kurva_mod.kali(b_privat, PA)
    print("Pertukaran kunci ECDH pada kurva yang sama")
    print(f"  Kunci privat Alice a = {a_privat}, publik A = aB =",
          format_titik(PA))
    print(f"  Kunci privat Bob   b = {b_privat}, publik B = bB =",
          format_titik(PB))
    print("  Alice menghitung a * (bB) =", format_titik(K_alice))
    print("  Bob   menghitung b * (aB) =", format_titik(K_bob))
    print("  Kunci bersama sama:", K_alice == K_bob,
          "(buku: (12, 4))")
    print()
    print("Penyerang yang melihat B, PA, dan PB harus menyelesaikan ECDLP")
    print("untuk memperoleh a atau b. Dengan modulus 23 persoalan itu dapat")
    print("diselesaikan dengan mencoba seluruh kemungkinan; pada kurva nyata")
    print("modulusnya berukuran 256 bit atau lebih.")
