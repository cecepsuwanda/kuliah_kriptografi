## Buku Ajar Kriptografi — S1 Matematika FMIPA Universitas Bale Bandung

Repositori ini berisi sumber LaTeX untuk Buku Ajar Mata Kuliah Kriptografi. Buku dibangun menggunakan pendekatan multi-berkas (subfiles) sehingga dapat dikompilasi sebagai satu buku utuh atau per bab secara terpisah. Materi mengikuti RPS (`rps.tex`).

### Struktur Proyek
- `main.tex`: berkas utama buku (mengikutkan seluruh bab). Menggunakan paket `subfiles`, `natbib`, dan `microtype` dengan font `lmodern`.
- `chapters/`: subdirektori berisi bab per-berkas:
  - `ch01.tex` … `ch14.tex`: masing-masing satu bab.
- `references.bib`: daftar referensi (Katz–Lindell, Stallings, Hoffstein–Pipher–Silverman, Menezes dkk., NIST AES/DES, dll.).
- `rps.tex`: ringkasan materi per pertemuan yang menjadi acuan penyusunan bab.
- `figures/`: tempat menyimpan gambar/ilustrasi (opsional).

### Pemetaan Bab ke Pertemuan RPS
- **Bab 1**: Pertemuan 1 — Pengantar, sejarah, definisi, kripto simetris
- **Bab 2**: Pertemuan 2 — Kunci publik vs privat, tanda tangan, hash, sertifikat
- **Bab 3**: Pertemuan 3 — FPB/GCD, kongruensi, \(\mathbb{Z}_n\), Euclid/Extended Euclid
- **Bab 4**: Pertemuan 4 — Sistem kongruensi, CRT, \(\varphi\) Euler, \(\mathbb{Z}_p\), FLT
- **Bab 5**: Pertemuan 5 — Akar primitif, residu kuadratik, simbol Legendre, logaritma diskrit
- **Bab 6**: Pertemuan 6 — Sandi blok vs alir; DES
- **Bab 7**: Pertemuan 7 — Varian DES, AES, IDEA
- **Bab 8**: Pertemuan 8 — LFSR, Vigenère, SEAL, RC4
- (M-9: UTS)
- **Bab 9**: Pertemuan 10 — Konsep kunci publik, FLT/Euler, RSA
- **Bab 10**: Pertemuan 11 — Tanda tangan digital (RSA, Ong–Schnorr–Shamir), verifikasi batch
- **Bab 11**: Pertemuan 12 — Distribusi/manajemen kunci, PKI
- **Bab 12**: Pertemuan 13 — Fungsi hash, MAC, unconditionally secure auth. code
- **Bab 13**: Pertemuan 14 — Kerberos, PGP, sistem pembayaran elektronik
- **Bab 14**: Pertemuan 15 — Analisis sistem kripto sederhana

### Prasyarat
- TeX Live (disarankan paket: `texlive-latex-base`, `texlive-latex-recommended`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-bibtex-extra`, `texlive-lang-other`)
- Font `lmodern` (atau keluarga Latin Modern) untuk kompatibilitas `microtype`
- (Opsional) `latexmk` untuk otomatisasi build

### Cara Kompilasi — Buku Utuh
Jalankan perintah berikut dari direktori proyek utama:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Dengan `latexmk`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

### Cara Kompilasi — Per Bab (Subfiles)
Masuk ke direktori `chapters/` lalu kompilasi berkas bab yang diinginkan:

```bash
cd chapters
pdflatex -interaction=nonstopmode -halt-on-error ch01.tex
```

Output PDF bab akan dihasilkan di direktori `chapters/` dengan nama yang sama (mis. `ch01.pdf`).

### Sitasi dan Daftar Pustaka
Sitasi menggunakan `natbib` dengan sumber pada `references.bib`. Pastikan menjalankan BibTeX (atau `latexmk`) agar referensi terselesaikan.

### Lisensi
Lihat berkas `LICENSE`.

### Kontribusi
- Ajukan isu atau pull request untuk perbaikan materi, kesalahan ketik, atau penambahan contoh/latihan.
