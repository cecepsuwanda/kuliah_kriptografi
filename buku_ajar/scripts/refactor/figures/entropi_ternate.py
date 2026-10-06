"""Membuat Gambar 3.x: sebaran frekuensi huruf plainteks vs cipherteks.

Sumber teks: referensi/02-Landasan-Matematika-Kriptografi-(2026), halaman 9
(contoh berita Kota Ternate beserta cipherteksnya).

Keluaran: buku_ajar/chapters/03/figures/frekuensi-huruf-ternate.png

Jalankan dari mana saja:
    python -I entropi_ternate.py
"""

import collections
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(
    os.path.join(HERE, "..", "..", "..", "chapters", "03", "figures",
                 "frekuensi-huruf-ternate.png")
)

PLAINTEXT = (
    "Dinas Pendidikan Kota Ternate meminta kepada pihak sekolah dan orang tua "
    "siswa untuk jenjang pendidikan SD dan SMP se-Kota Ternate untuk melarang "
    "para siswa membawa permainan lato-lato yang sedang tren itu ke sekolah, "
    "karena akan mengganggu kegiatan belajar mengajar yang dinilai berbahaya "
    "sehingga mengantisipasi kecelakaan bagi anak di daerah itu."
)

CIPHERTEXT = (
    "HAWFHZDOHAHANGOMKLGFCVWFLBOCPRKFGHNOFNINSPGNLHMPFVBEFWMVFWTBWRHSFZRWK"
    "FQMVHPAFWIKDOHAHANGPFEWNFPFNKLHMPFGLBAMGFCXKFQMOCFVAVKANIAVHSFZRNCODG"
    "AFOHYUVGWGFOFGXEGFMLFWITHEFWTBVCPAYQOBLHMPFVBPVADOVGNWFGNOVCARKVA"
    "RQOBRGGFWHCVFGVYYUDORVGVYCFWABAPVSVGCHGCIDRFIFHBAPVQRVOC KAFWSGSHSNIH"
    "SOBDHFVNGFWDGRGRFWGNHANFCVIDGSWZ"
)


def letters_only(text):
    return "".join(ch for ch in text.upper() if "A" <= ch <= "Z")


def frequencies(text):
    letters = letters_only(text)
    counts = collections.Counter(letters)
    total = len(letters)
    return {c: 100.0 * counts.get(c, 0) / total for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}


def entropy(text):
    letters = letters_only(text)
    counts = collections.Counter(letters)
    total = len(letters)
    return -sum((n / total) * math.log2(n / total) for n in counts.values())


def main():
    fp = frequencies(PLAINTEXT)
    fc = frequencies(CIPHERTEXT)
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    x = range(len(alphabet))

    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["DejaVu Serif"],
        "mathtext.fontset": "dejavuserif",
        "font.size": 9,
    })

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.0), sharey=True)

    axes[0].bar(x, [fp[c] for c in alphabet], color="#4C72B0", width=0.72)
    axes[0].set_title(
        r"Plainteks: $H(P)=3{,}8988$ bit/karakter", fontsize=9.5
    )

    axes[1].bar(x, [fc[c] for c in alphabet], color="#C44E52", width=0.72)
    axes[1].set_title(
        r"Cipherteks: $H(C)=4{,}3035$ bit/karakter", fontsize=9.5
    )

    for ax in axes:
        ax.set_xticks(list(x))
        ax.set_xticklabels(alphabet, fontsize=7)
        ax.set_ylim(0, 22)
        ax.grid(axis="y", linestyle=":", linewidth=0.5, alpha=0.6)
        ax.set_axisbelow(True)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)

    axes[0].set_ylabel("Frekuensi relatif (%)")
    fig.tight_layout()
    fig.savefig(OUT, dpi=220)
    print("Ditulis:", OUT)
    print("H(P) hitung = %.4f  H(C) hitung = %.4f" % (
        entropy(PLAINTEXT), entropy(CIPHERTEXT)))


if __name__ == "__main__":
    main()
