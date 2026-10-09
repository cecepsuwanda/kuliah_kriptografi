"""Menghitung jumlah kata pada berkas-berkas satu bab.

Dipakai untuk memeriksa target kedalaman per bab (lihat
scripts/refactor/gap-map.md). Perintah LaTeX dan isi blok verbatim dibuang
lebih dahulu supaya angkanya mencerminkan prosa yang benar-benar dibaca.

Jalankan: python -I hitung_kata_bab.py 16
"""

import os
import re
import sys

BERKAS = ["chapter.tex", "section-01.tex", "section-02.tex", "section-03.tex",
          "section-04.tex", "contoh.tex", "praktikum.tex", "latihan.tex",
          "rangkuman.tex", "evaluasi.tex"]

POLA_VERBATIM = re.compile(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", re.S)
POLA_KOMENTAR = re.compile(r"%.*")
POLA_PERINTAH = re.compile(r"\\[a-zA-Z]+\*?")
POLA_SIMBOL = re.compile(r"[{}$\\&_^~]")


def bersihkan(teks):
    teks = POLA_VERBATIM.sub(" ", teks)
    teks = POLA_KOMENTAR.sub(" ", teks)
    teks = POLA_PERINTAH.sub(" ", teks)
    teks = POLA_SIMBOL.sub(" ", teks)
    return teks


def hitung(path):
    return len(bersihkan(open(path, encoding="utf-8").read()).split())


def main():
    if len(sys.argv) < 2:
        print("Pakai: python -I hitung_kata_bab.py NN")
        return 1
    direktori = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "chapters",
        sys.argv[1]))

    total = 0
    for nama in BERKAS:
        path = os.path.join(direktori, nama)
        if not os.path.exists(path):
            continue
        n = hitung(path)
        total += n
        print("%-16s %6d kata" % (nama, n))
    print("%-16s %6d kata" % ("TOTAL", total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
