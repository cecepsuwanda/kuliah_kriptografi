# Laporan: Perdalaman Isi Buku Ajar Kriptografi

**Tanggal:** 9 Oktober 2026
**Lingkup:** langkah 6 `perintah.txt` — memperdalam isi materi buku ajar (bukan menambah struktur)
**Rencana acuan:** `C:\Users\cecep\.claude\plans\dynamic-brewing-stream.md`
**Berkas kerja pemetaan:** `buku_ajar/scripts/refactor/gap-map.md`
**Status:** **SELESAI** — seluruh 17 tahap (Tahap 0 + Tahap 1–16) tuntas

---

## 1. Ringkasan

| Tolok ukur | Semula | Sekarang |
|---|---|---|
| Jumlah bab | 16 | 16 (tidak berubah) |
| Total kata | ±24.000 | **152.308** |
| Halaman PDF | 178 | **549** |
| Gerbang kebersihan build | 0 pada 7 pola | **0 pada 7 pola** (tetap) |
| Bab tanpa sitasi | 6 bab | **0** |
| Bab tanpa persamaan bernomor | 16 bab | **2** (Bab 01 & 02, bab konseptual) |
| Bab tanpa environment `example` | 4 bab | **0** |
| Bab tanpa gambar raster | 3 bab | **0** |

Cakupan pekerjaan: **memperdalam substansi**, bukan menambah struktur. Tidak ada bab baru
(Steganografi tidak dibuat meskipun `referensi/19-*` dan `20-*` ada — silabus tidak
mencakupnya), tidak ada section yang dinomori ulang, `referensi/` tidak pernah disentuh,
dan tidak ada `\usepackage` baru di `chapter.tex`.

---

## 2. Cara verifikasi

Seluruh angka pada laporan ini diukur langsung dari repositori, bukan dari catatan:

```bash
# jumlah kata per bab (prosa; blok verbatim, komentar, dan perintah LaTeX dibuang)
cd buku_ajar/scripts/refactor && python -I hitung_kata_bab.py NN

# kompilasi buku penuh — jalur absolut wajib, dan tidak boleh ada build lain berjalan
cmd /c "C:\Matakuliah\kuliah_kriptografi\compile_main.bat < nul"

# gerbang kebersihan: ketujuh pola harus 0 pada output/main_build.log
#   ^! | LaTeX Warning | pdfTeX warning | Package .* Warning
#   Overfull|Underfull | Citation.*undefined | Reference.*undefined

# tanpa penomoran ulang section: bandingkan jumlah section-NN.tex sebelum & sesudah
git ls-tree --name-only 4d5115e -- buku_ajar/chapters/NN/   # sebelum perdalaman
git ls-tree --name-only HEAD    -- buku_ajar/chapters/NN/   # sesudah

# verifikasi visual halaman tertentu
pdftoppm -png -r 100 -f 509 -l 509 output/main.pdf output/_vcheck/p509
```

---

## 3. Tahap dan commit

Satu commit per bab, dikerjakan berurutan 01 → 16. Commit bab tidak pernah menyertakan
`perintah.txt`.

| Bab | Judul | Commit |
|---|---|---|
| 01 | Pengantar dan Urgensi Kriptografi | `05b28b3` |
| 02 | Layanan Keamanan dan Serangan | `a12c181` |
| 03 | Landasan Matematika untuk Kriptografi | `4115eae` |
| 04 | Kriptografi Klasik | `fc61937` |
| 05 | Stream Cipher | `5140104` |
| 06 | Block Cipher: Konsep dan Mode Operasi | `546d10e` |
| 07 | Analisis Algoritma Block Cipher: DES | `fc25eef` |
| 08 | Analisis Algoritma Block Cipher: AES | `32d8f27` |
| 09 | Studi Algoritma Block Cipher Lainnya | `513f47f` |
| 10 | Algoritma RSA | `c2061c6` |
| 11 | Protokol Diffie-Hellman | `c3b4747` |
| 12 | Algoritma ElGamal | `e423c44` |
| 13 | Algoritma Knapsack | `b796f00` |
| 14 | Kriptografi Kurva Eliptik (ECC) | `07f341b` |
| 15 | Fungsi Hash dan MAC | `eebddb0` |
| 16 | Otentikasi dan Tanda Tangan Digital | `fd292db` |

---

## 4. Statistik per bab

| Bab | Kata | Tabel | Gambar | Persamaan | Contoh | Sitasi |
|---|---:|---:|---:|---:|---:|---:|
| 01 | 5.538 | 2 | 10 | 0 | 4 | 5 |
| 02 | 4.657 | 2 | 9 | 0 | 5 | 13 |
| 03 | 6.181 | 1 | 4 | 6 | 5 | 9 |
| 04 | 12.164 | 13 | 35 | 10 | 6 | 38 |
| 05 | 9.684 | 12 | 12 | 7 | 4 | 13 |
| 06 | 7.207 | 4 | 5 | 16 | 4 | 7 |
| 07 | 10.077 | 9 | 3 | 8 | 7 | 6 |
| 08 | 12.803 | 10 | 7 | 19 | 6 | 8 |
| 09 | 9.284 | 10 | 7 | 7 | 4 | 18 |
| 10 | 9.033 | 8 | 3 | 15 | 6 | 11 |
| 11 | 9.048 | 5 | 7 | 3 | 6 | 7 |
| 12 | 8.722 | 4 | 4 | 8 | 6 | 9 |
| 13 | 8.118 | 9 | 4 | 8 | 6 | 6 |
| 14 | 16.712 | 12 | 7 | 20 | 6 | 10 |
| 15 | 12.415 | 8 | 5 | 16 | 7 | 38 |
| 16 | 10.665 | 5 | 5 | 10 | 6 | 31 |
| **Total** | **152.308** | **114** | **127** | **153** | **88** | **229** |

Jumlah "Gambar" mencakup gambar raster (`figures/*.png`) dan diagram TikZ
(`figures/*.tex`). Setiap bab memiliki paling sedikit satu gambar raster.

---

## 5. Verifikasi enam cacat lintas bab

Rencana mencatat enam cacat yang harus diperbaiki sambil memperdalam. Status terukur:

| # | Cacat | Status |
|---|---|---|
| 1 | **Bab 09 menyesatkan soal keamanan GOST** — buku menyiratkan GOST lebih aman, padahal kompleksitas serangan turun ke 2¹⁷⁸ | **Selesai.** Subbagian *Kriptanalisis GOST dan Batas Rekeying*, tabel kompleksitas serangan, batas rekeying 2³² blok, kotak `\important`; `praktikum.tex` butir 2 diganti dan butir 9.5 ditambah |
| 2 | **Nol environment `equation` ber-nomor** | **Selesai untuk 14 dari 16 bab** (153 persamaan bernomor). Bab 01 dan 02 memang tidak memuat penurunan rumus, jadi penomoran tidak diperlukan |
| 3 | **`contoh.tex` tidak konsisten memakai `example`** | **Selesai.** 16/16 bab memakai `example`; terendah 4, tertinggi 7 (total 88) |
| 4 | **Bab 03, 15, 16 tanpa gambar raster** | **Selesai.** Ketiganya kini punya `.png`; seluruh 16 bab punya gambar raster |
| 5 | **Bab tanpa sitasi: 02, 03, 05, 06, 07, 14** | **Selesai.** 16/16 bab bersitasi; terendah Bab 01 = 5, tertinggi Bab 04 & 15 = 38 |
| 6 | **`code/pascal/` kosong** | **Tidak dikerjakan — sesuai rencana.** Rencana menandainya opsional karena `praktikum.tex` hanya menjanjikan padanan C++ dan MATLAB. Isi direktori masih `.gitkeep` saja |

**Tidak ada penomoran ulang section.** Jumlah `section-NN.tex` per bab identik antara commit
`4d5115e` (sebelum perdalaman dimulai) dan `HEAD`, sehingga `frontmatter/syllabus_map.tex`
tetap sahih. Hal ini juga tercermin pada build: 0 `Reference undefined`.

---

## 6. Butir gap bernilai tertinggi dari rencana

Kelima belas butir pada tabel prioritas rencana diuji keberadaannya di berkas bab:

| Bab | Butir rencana | Status |
|---|---|---|
| 07 | Tabel bit DES (IP, IP⁻¹, E, S-box, P, PC-1, PC-2) + nilai kunci lemah | ada |
| 08 | Dekripsi AES (InvSubBytes/InvShiftRows/InvMixColumns) + Rcon + konstruksi S-box | ada |
| 09 | Koreksi kriptanalisis GOST + batas rekeying | ada |
| 10 | Contoh multi-blok "HELLO ALICE" + penurunan dari Teorema Euler | ada |
| 04 | Kasiski + indeks kebetulan + tabel bigram/trigram | ada |
| 12 | Contoh multi-blok "HALO" dengan dua kunci sesaat berbeda | ada |
| 13 | Greedy superincreasing {2,3,6,13,27,52} + knapsack dasar | ada |
| 14 | ECEG + encoding Koblitz mod 751 + aritmetika GF(2^m) | ada |
| 15 | SHA-3 sponge + CMAC/Poly1305/GMAC/AEAD | ada |
| 01 | Tiga keluarga algoritma + studi kasus kebocoran data Indonesia | ada |
| 02 | Tabel kategori serangan + saluran samping | ada |
| 03 | Entropi teks nyata + totient/Euler/akar primitif | ada |
| 05 | A5/1, Trivium, Salsa20/ChaCha20, RC4 | ada |
| 06 | Lima mode operasi + CFB-8 + tabel perbandingan | ada |
| 11 | MITM + protokol tiga pihak + Logjam | ada |

---

## 7. Gerbang kebersihan kompilasi

Kompilasi terakhir (`cmd /c "C:\Matakuliah\kuliah_kriptografi\compile_main.bat < nul"`):

```
Output written on output/main_build.pdf (549 pages, 16.084.107 bytes)
```

| Pola pada `output/main_build.log` | Jumlah |
|---|---:|
| `^!` | 0 |
| `LaTeX Warning` | 0 |
| `pdfTeX warning` | 0 |
| `Package .* Warning` | 0 |
| `Overfull\|Underfull` | 0 |
| `Citation.*undefined` | 0 |
| `Reference.*undefined` | 0 |

Verifikasi visual (render `pdftoppm`) atas halaman-halaman kunci Bab 16 — gambar raster,
diagram TLS 1.2/1.3 berdampingan, tabel perbandingan — menunjukkan gambar tampil utuh,
tabel tidak meluber, dan penomoran persamaan (16.1)–(16.10) ter-render serta dirujuk benar.

---

## 8. Penyimpangan dari angka target

Ini bukan kekurangan, tetapi perlu dicatat karena jauh melampaui target yang tertulis di
rencana:

| | Target rencana | Aktual |
|---|---|---|
| Total kata | ±74.000 | **152.308** (2,1×) |
| Halaman | ±400–450 | **549** |
| Kata per bab | ±4.000–6.000 | 4.657 – **16.712** (Bab 14) |

Bab yang paling jauh melampaui target per-bab: **14** (16.712), **08** (12.803),
**15** (12.415), **04** (12.164). Bab yang paling dekat ke target: **02** (4.657),
**01** (5.538), **03** (6.181).

---

## 9. Catatan dan sisa pekerjaan

- **Tidak ada butir rencana yang tertinggal**, kecuali `code/pascal/` yang memang
  ditandai opsional oleh rencana sendiri.
- **Jika total ingin didekatkan ke ±74.000 kata**, bab yang perlu diramping adalah
  14, 08, 15, dan 04. Namun itu berarti memangkas prosa naratif yang sudah lolos
  gerbang kebersihan, sehingga belum ditempuh tanpa persetujuan.
- `perintah.txt` tetap dalam keadaan termodifikasi di working tree dan **tidak** ikut
  di-commit pada keenam belas commit bab, konsisten dengan tahap-tahap sebelumnya.
- Berkas baru yang dihasilkan selama pengerjaan:
  - `buku_ajar/scripts/refactor/hitung_kata_bab.py` — penghitung kata per bab
  - `buku_ajar/scripts/refactor/gap-map.md` — pemetaan gap per bab (semua bertanda selesai)
  - `buku_ajar/scripts/refactor/figures/ukuran_tanda_tangan.py` + gambar raster Bab 16
  - `buku_ajar/code/cpp/tanda_tangan.cpp`, `buku_ajar/code/matlab/tanda_tangan.m`
- **Referensi:** `referensi/` tidak pernah diubah. Gambar hanya disalin keluar.
