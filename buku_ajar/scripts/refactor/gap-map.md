# Peta Celah: Referensi → Buku Ajar

Berkas kerja untuk Tahap 0–16 rencana `dynamic-brewing-stream.md`.
Keadaan awal: buku 178 halaman, 0 error, 0 warning. Tiap bab 1.100–2.200 kata.
Sasaran: ±4.000–6.000 kata/bab (prosa naratif), tabel, contoh terhitung, gambar.

Legenda status: `[ ]` belum · `[~]` sedang dikerjakan · `[x]` selesai.

**Kemajuan:** Tahap 1–7 (Bab 01–07) selesai. Buku 323 halaman, gerbang kebersihan
`output/main_build.log` = 0 pada ketujuh pola. Berikutnya: Tahap 8 (Bab 08).
Panjang bab saat ini di buku penuh: Bab 01 = 23 hal., Bab 02 = 20, Bab 03 = 19,
Bab 04 = 56, Bab 05 = 30, Bab 06 = 23 (149–171), Bab 07 = 29 (172–200).

---

## Bab 01 — Pengantar dan Urgensi Kriptografi  `[x]` SELESAI
Sumber: `referensi/01-Pengantar-Kriptografi-(2026)` (6.585 kata, 27 topik, 198 gambar).
Target: ±4.500 kata. **Hasil: 6.605 kata berkas (dari 1.305), 22 hlm jadi, +5 gambar.**

- [x] Tiga jenis algoritma kriptografi (simetri, nir-simetri, fungsi hash) sebagai kategori utuh
- [x] Studi kasus kebocoran data Indonesia (BPJS, Tokopedia, KPU, Kemenhan, BSI) sebagai motivasi urgensi
- [x] Lembaga terkait kriptografi di Indonesia (BSSN, PSSN, Museum Sandi)
- [x] Tantangan masa depan: komputasi kuantum, IoT/*lightweight*, AI, *selective encryption*
- [x] Tabel miskonsepsi vs fakta (`tab:miskonsepsi`)
- [x] Terminologi diperluas menjadi 8 item + Prinsip Kerckhoffs
- [x] Sejarah: Mesir Kuno, Yunani/Romawi, Al-Kindi & ad-Durayhim, Renaisans, PD II (Enigma), era modern
- [x] Gambar baru: `enigma-pd2.png`, `kriptografi-simetri.png`, `kriptografi-nirsimetri.png`,
      `encoding-hashing-encryption.png`, `lightweight-cryptography-iot.png`
- [x] Tabel baru: `tab:empat-masalah`, `tab:miskonsepsi`
- [x] Contoh baru: *encoding* ≠ enkripsi (Base64); jumlah kunci simetri vs nir-simetri

## Bab 02 — Layanan Keamanan dan Serangan  `[x]` SELESAI
Sumber: `referensi/06-Serangan-pada-kriptografi-(2026)` (4.241 kata, 21 topik, 63 gambar).
Target: ±4.000 kata. **Hasil: 5.529 kata berkas (dari 1.415), 20 hlm jadi bab mandiri,
+5 gambar, +3 tabel, +3 contoh, 7 sitasi (sebelumnya 0).**

- [x] Definisi formal tiap tipe serangan (Diberikan/Dideduksi) + contoh kerja per tipe
      (Caesar `KHOORZRUOG`, Vigenère `AAAAA`→`SCRAM`, adaptive A→F lalu B→G, chosen-ciphertext `A`→`X`)
- [x] Tujuan serangan: key-recovery, plaintext-recovery, distinguishing, forgery, replay
      beserta ukuran keberhasilan masing-masing + `fig:serangan-replay`
- [x] Tabel 7 kategori serangan Stallings + contoh nyata (`tab:kategori-serangan`)
- [x] Serangan pasif vs aktif: intersepsi, analisis lalu lintas, interupsi, fabrikasi,
      modifikasi, pemutaran ulang, MITM
- [x] *Side-channel* konkret: penyadapan kabel, elektromagnetik ($r<2$ m, SDR), akustik
      (vibrometri), Wireshark; `tab:side-channel` (jenis / kebocoran / penangkal)
- [x] Keamanan komputasi (3 syarat) vs keamanan tanpa syarat ($H(P\mid C)=H(P)$, OTP)
- [x] Kasus ATM (chosen-plaintext), pemalsuan MAC, dan pengulangan pesan dengan nomor urut
- [x] Gambar baru: `serangan-analisis-lalu-lintas.png`, `wireshark-plaintext.png`,
      `penyadapan-elektromagnetik.png`, `penyadapan-akustik.png`, `serangan-replay.png`
- [x] Contoh baru: CPA pada Vigenère (`C = K`), *timing attack* ($26^n$ → $26n$),
      *replay* + nomor urut
- [x] Sitasi: `stallings2017`, `menezes1996`, `katz2020`, `schneier1996`

## Bab 03 — Landasan Matematika untuk Kriptografi  `[x]` SELESAI
Sumber: `referensi/02-*` (**hanya 1.071 kata, 2 topik — paling tipis**); lengkapi dari
`referensi/materi_buku.tex` + `menezes1996` (HAC Bab 2). Target: ±3.500 kata.
**Hasil: 6.066 kata berkas (dari 1.109), 19 hlm jadi bab mandiri, +1 gambar TikZ,
+1 gambar raster (dibuat sendiri), +1 tabel, +3 contoh, 5 sitasi (sebelumnya 0).**

- [x] Tabel peta topik matematika untuk kriptografi + tempat pembahasannya (`tab:peta-matematika`)
- [x] Teori bilangan: sifat pembagian (Pers. `eq:pembagian`), aritmetika modulo + modulo
      negatif, kekongruenan + sifat & batas pencoretan, PBB, Algoritma Euclidean,
      kombinasi lanjar (Identitas Bézout), invers modulo, bilangan prima,
      fungsi totient Euler, Teorema Euler & Fermat Kecil, akar primitif, logaritma diskrit
- [x] Nomor persamaan: `eq:pembagian`, `eq:mod-tambah`, `eq:mod-kali`, `eq:invers`,
      `eq:euler`, `eq:entropi` — bab pertama yang memakai `equation` bernomor
- [x] Kuantisasi informasi (1 bit jenis kelamin, 3 bit hari, 4 bit angka), laju bahasa
      dan redundansi (~75\% untuk bahasa Inggris)
- [x] Contoh entropi teks nyata (berita Kota Ternate: 3,8988 vs 4,3035 bit);
      **angka $H(P)$ diverifikasi ulang dari teksnya dan cocok persis (296 huruf, 21 huruf berbeda)**
- [x] $H_{\max}$ 26 huruf = 4,7004 bit; 256 ASCII = 8 bit
- [x] Latihan modulo negatif, invers modulo, totient, Teorema Euler, akar primitif
- [x] Gambar baru: `figures/rentang-entropi.tex` (TikZ) dan
      `figures/frekuensi-huruf-ternate.png` (raster, dibuat oleh
      `scripts/refactor/figures/entropi_ternate.py`)
- [x] Sitasi: `menezes1996`, `stinson2018`, `katz2020`, `stallings2017`

## Bab 04 — Kriptografi Klasik  `[x]` SELESAI
Sumber: `referensi/03-*` (3.455) + `04-*` (11.746) + `05-*` (2.565). Target: ±6.000 kata.
**Hasil: 15.594 kata berkas (dari 1.941), 55 hlm jadi bab mandiri, 25 gambar,
7 tabel baru, 3 contoh baru, 3 sitasi baru (`shannon1949`, `vernam1919`, `kasiski1863`);
buku penuh 178 → 220 hlm.**

- [x] Transposisi: kolom dengan kata kunci, pagar rel (\textit{Rail Fence}) $k=3$/$k=4$,
      transposisi blok; tabel + 3 gambar
- [x] Super-enkripsi (Caesar+transposisi), ROT13, dan kaitannya ke cipher modern
- [x] Analisis frekuensi: tabel frekuensi Inggris & Indonesia, bigram, trigram,
      indeks kebetulan (`eq:indeks-kebetulan`, `tab:ic-stalling`), studi kasus Stallings
      $CI = 916/(120\cdot119) = 0{,}0641$
- [x] Kasiski dengan contoh nyata (jarak 15/15/15/10/10 → panjang kunci 5 → SCRAM)
- [x] Hill: matriks 2×2 dan 3×3, determinan/invers, kriptanalisis *known-plaintext*
- [x] Affine: rumusan + syarat $\gcd(m,26)=1$, contoh \code{kripto} → \code{CZOLNE},
      kriptanalisis dua kongruensi simultan, ruang kunci 300, varian blok 4 huruf
- [x] Vigenère varian: Full Vigenère, Auto-Key, Running-Key (`tab:varian-vigenere`)
- [x] Playfair: sejarah Wheatstone, alasan \code{J} dihapus, 3 aturan + contoh bigram
- [x] Enigma: Scherbius, rotor/plugboard/reflektor, periode $26^3$/$26^4$,
      contoh huruf demi huruf (\code{PESAWATMENDARAT}), Bombe Turing
- [x] OTP: syarat formal $|K| = |P|$, Vernam 1919, kerahasiaan sempurna Shannon 1949
      (`eq:perfect-secrecy`), \code{onetimepad} + \code{tbfrgfarhm} → \code{HOJKOREGHP},
      alasan tak cocok untuk WhatsApp/HTTPS/VPN/cloud/IoT + telusur sejarah (hotline Moskow)
- [x] Perbaikan cacat: `fig:cakram-caesar` dirujuk tetapi belum pernah didefinisikan →
      blok `figure` disisipkan di `section-01.tex`; gambar duplikat
      `columnar-tombak.png` dihapus (identik byte-per-byte dengan `transposisi-kolom.png`)

### Koreksi terhadap sumber (wajib dicatat)
- **Super-enkripsi**: `KROHZGORZOUZ` (dek mencetak `KROHZGZOUZ` — kurang satu huruf).
- **Playfair**: cacah bigram = **676** (dek mencetak 677).
- **Affine varian blok**: invers dari $m = 21\,035\,433$ modulo $25\,252\,525$ adalah
  **$11\,837\,547$** (dek mencetak $5\,174\,971$; sudah diverifikasi \textit{round-trip}
  $P=10\,170\,815 \rightarrow C=22\,837\,395 \rightarrow P=10\,170\,815$).
- **OTP Contoh 1**: dek mencetak cipherteks `HOJKOREGHP` dan kunci `tbfrgfarfm` yang
  saling tidak konsisten. Bukti silang: dengan membaca cipherteks sebagai `HOJKOREGHP`
  (huruf ke-9 kunci = `h`), kunci Contoh 3 dek (`LMCCAWAAZD`, `ZDVUZOEYEO`) tereproduksi
  **10/10**; dengan pembacaan sebaliknya hanya 9/10. Karena itu dipakai
  \code{onetimepad} + \code{tbfrgfarhm} → \code{HOJKOREGHP}.
- **OTP Contoh 3**: kunci dek (`LMCCAWAAZD`/`ZDVUZOEYEO`) adalah kunci Konvensi cermin
  (Beaufort, $K = P - C$). Buku memakai negatifnya modulo 26,
  \code{POYYAEAABX} → \code{SALMONEGGS} dan \code{BXFGBMWCWM} → \code{GREENFIELD},
  sesuai aturan yang dinyatakan buku ($P = (C-K) \bmod 26$).
- **OTP Contoh 2 tidak dipakai**: plainteks 41 huruf, kunci 41 huruf, tetapi cipherteks
  yang dicetak dek hanya 40 huruf dan menyimpang sejak posisi 10; contoh itu tidak dapat
  direproduksi sehingga dihilangkan dari buku.
- **Ruang kunci Affine**: kepala tulisan memakai **300** ($12 \times 25$) mengikuti dek dan
  rencana; secara ketat $b \in 0..25$ memberi 312, dan hal itu dijelaskan dalam teks.

## Bab 05 — Stream Cipher  `[x]` SELESAI
Sumber: `referensi/07-Kripto-modern-dan-stream-cipher-2026` (9.039 kata, 35 topik, 94 gambar).
Target: ±4.500 kata. **Hasil: 9.625 kata berkas (dari 1.628), 29 hlm jadi bab mandiri,
12 gambar (9 baru), 7 tabel baru (total 12), 4 contoh (3 baru), 10 sitasi baru
(sebelumnya 0).**

- [x] Tabel konversi bit/byte/heksadesimal (`tab:konversi-biner-hex`) + tabel kebenaran XOR (`tab:kebenaran-xor`)
- [x] Subbagian baru *Bit, Byte, dan Kode Heksadesimal* (1 byte = 8 bit, 1 digit hex = 4 bit,
      `9D6A`, `Halo`, `Indonesia emas 2045`) + `fig:kriptografi-modern-blok`
- [x] Subbagian baru *Operasi XOR dan Bitwise* (4 sifat, `eq:xor-enkripsi`, `eq:xor-dekripsi`,
      `10011⊕11001=01010`, `fig:xor-bitwise`, `65₁₆⊕35₁₆=50₁₆='P'`)
- [x] Subbagian baru *Cipher XOR Sederhana dan Kelemahannya* (contoh 29 bit, pelacakan periode
      ala Kasiski, `c₁⊕c₂ = p₁⊕p₂`)
- [x] `tab:klasik-vs-modern` diperluas (2 baris baru) + `tab:stream-vs-block`
- [x] Subbagian baru *Keystream Generator dan Umpan* (acak semu vs acak sejati, periode,
      ketidakterulangan umpan, nonce) + `eq:stream-enkripsi`/`eq:stream-dekripsi`
- [x] Subbagian baru *Umpan Balik dan LFSR* (`fig:fsr-blok`, `fig:lfsr` dipindah dari
      section-03, `tab:lfsr-4bit` 15 baris terverifikasi, periode $2^n-1$, kelemahan linier
      + Berlekamp--Massey)
- [x] Subbagian baru *Penyebaran Galat dan Aplikasi Cipher Alir* (`tab:galat-cipher-alir`,
      serangan *flip-bit*, akses acak berbasis pencacah)
- [x] Subbagian baru *Peta Cipher Alir* (`tab:daftar-cipher-alir` 17 cipher + tahun,
      `tab:estream` portofolio 2008)
- [x] **RC4**: pseudokode KSA + PRGA (`lst:rc4-pseudocode`), `fig:ron-rivest`, `fig:alur-rc4`,
      `fig:rc4-prga`, keamanan (korelasi byte awal, buang 256--512 byte, FMS/WEP, *flip-bit*,
      RFC 7465, varian Spritz/RC4A/VMPC/RC4+)
- [x] **A5/1**: frame 228 bit/4,6 ms, kunci sesi 64 bit, tiga LFSR 19/22/23,
      `tab:a51-register` (memisahkan bit kendali dan titik sadap umpan balik),
      `fig:a51-lfsr`, `eq:a51-luaran`, kaidah mayoritas (peluang 3/4), pola inisialisasi
      64 + 22 + 100 + 228, A5/2, A5 di Indonesia *disabled*, serangan Anderson 1994
- [x] **Trivium**: De Cannière--Preneel, eSTREAM, NLFSR 93/84/111, `tab:trivium-tap`,
      `fig:trivium-sirkuit`, `eq:trivium-luaran`, inisialisasi 80-bit IV + 80-bit kunci +
      $4\times288=1152$ detak pemanasan, keunggulan *lightweight* (288 sel, 3 AND, 7 XOR)
- [x] **Salsa20/ChaCha20**: `fig:daniel-bernstein`, blok 512 bit, `fig:salsa20-state`,
      konstanta `expand 32-byte k`, AXR, QR Salsa20 (rotasi 7/9/13/18), `eq:salsa-final`,
      ChaCha20 (rotasi 16/12/8/7), `tab:chacha-round` (indeks kolom/diagonal), nonce 96 bit
      versi IETF, TLS 1.3/RFC 8439, keunggulan ARX + keystream paralel
- [x] Subbagian *Perbandingan Cipher Alir* (`tab:perbandingan-cipher-alir`) + penutup
      analitis: panjang kunci bukan penentu utama keamanan cipher alir
- [x] Contoh baru: keystream LFSR 4 bit untuk pesan `Aku` (periode terlihat), RC4 mainan
      $N=8$ kunci `AB` (jejak KSA lengkap + byte keystream 7,4,0 + `Halo`→`4F656C`),
      satu QR ChaCha20 atas $(1,2,3,4)$
- [x] Aktivitas baru: 5.2 (membangkitkan keystream LFSR & mengukur periode) dan
      5.3 (demonstrasi bahaya pemakaian ulang keystream)
- [x] Latihan 5.1 diperluas 3 → 8 butir + Latihan 5.2 baru (7 butir hitungan/analisis);
      rangkuman 7 → 12 butir; kuis 3 → 7 butir; checklist 5 → 14 baris
- [x] Sitasi: `estream2008`, `canniere2006trivium`, `bernstein2005salsa20`,
      `bernstein2008chacha`, `anderson1994`, `briceno1999`, `fluhrer2001`, `rfc7465`,
      `rfc8439`, `massey1969` (10 entri baru di `references.bib`, 13 → 23)

### Koreksi terhadap sumber (wajib dicatat)
- **Keystream pada contoh P/K/C**: dek menulis keystream `111101011001001000111101011`
  yang panjangnya **27 bit**, bukan 24 bit, dan hasil XOR-nya tidak konsisten dengan
  $C$ yang dicetak dek sendiri. Keystream 24 bit yang benar adalah `111101011001000111101011`
  $=\code{F591EB}$, yaitu 15 bit keluaran LFSR diulang 9 bit awalnya; dengan itu
  $P=\code{571964}$ menghasilkan $C=\code{A2888F}$, persis seperti yang ditulis dek.
- **LFSR 4 bit**: tabel pada `contoh.tex` lama salah pada baris ke-7 (mencetak `1 0 1 1`;
  keadaan yang benar adalah `0011`). Seluruh 15 baris dihitung ulang dengan Python dan
  sekarang disajikan di `tab:lfsr-4bit`.
- **Titik sadap A5/1**: dek mencampur istilah *bit kendali* (*clocking*) dengan *titik sadap
  umpan balik* ("Bit ke-8 pada register 1. Bit-bit detak pada bit 13, 16, 17, dan 18").
  Buku memisahkan keduanya ke dalam dua kolom `tab:a51-register` agar dapat diikuti.
- **Aplikasi cipher alir**: dek menampilkan aplikasi sebelum daftar cipher; bab ini
  memindahkan urutannya (daftar cipher lebih dulu) dan menambahkan portofolio eSTREAM yang
  tidak ada di dek.
- **Bahan di luar lingkup**: dek 07 memuat makalah *BPCS-Steganography* (halaman 18--20)
  yang tidak berhubungan dengan stream cipher dan **tidak dipakai**, sesuai batas silabus.

## Bab 06 — Block Cipher: Konsep dan Mode Operasi  `[x]` SELESAI
Sumber: `referensi/08-*` (6.812 kata, 21 topik, 92 gambar). Target: ±4.000 kata.

Hasil: 4.872 kata pada empat section (6.709 kata berkas mentah), 23 halaman
mandiri, 1 tabel + 1 gambar baru (`mode-cfb-ofb`), 2 contoh terhitung baru,
sitasi baru (`shannon1949`, `stallings2017`, `menezes1996`).

- [x] Tabel perbandingan lima mode operasi (ECB/CBC/CFB/OFB/CTR) — `tab:perbandingan-mode`
- [x] Contoh padding ECB (`10001101 00101001 10110[000]`) di section-01
- [x] CFB s-bit (CFB-8): shift register, IV, rumus $\mathrm{MSB}_s$/$\mathrm{LSB}_{b-s}$, kasus $s=b$
- [x] OFB: tanpa propagasi galat, umpan balik dari keluaran $E_K$
- [x] Contoh konkret confusion/diffusion (S-box $S_1$ DES dan S-box AES)
- [x] Contoh cipher mainan 4 bit ($E_K(P)=(P\oplus K)\ll 1$) — sudah ada, diperdalam
- [x] Cipher blok sebagai permutasi bijektif ($2^n!$ permutasi vs $2^m$ kunci)
- [x] Tabel ukuran blok/kunci/putaran tujuh cipher (`tab:ukuran-blok-kunci`)
- [x] Tabel Feistel vs SPN (`tab:feistel-vs-spn`) dan tabel confusion vs diffusion
- [x] Manipulasi blok ECB (kasus "Uang ditransfer lima satu juta rupiah")
- [x] Contoh Feistel dua putaran dan bahaya pengulangan counter CTR (contoh.tex)
- [x] Aktivitas 6.2 (penjalaran galat) dan 6.3 (pengulangan counter) di `praktikum.tex`
- [x] Latihan 6.1 diperluas 3→8 butir, ditambah Latihan 6.2 (7 butir)
- [x] `rangkuman.tex` 7→14 butir; `evaluasi.tex` kuis 3→8, checklist 5→13 baris

### Koreksi terhadap sumber (wajib dicatat)

1. **Hasil CBC pada dek `08-*` salah.** Dek menyatakan cipherteks CBC
   `\text{A23A9}` adalah **27FBF**; perhitungan ulang memberi **27FDF**
   ($C = 0010\ 0111\ 1111\ 1101\ 1111$). Buku sudah memakai nilai yang benar.
2. **Contoh S-box DES pada dek tidak konsisten.** Dek memberi masukan
   $\code{110100}$ dan menyebut entrinya bernilai 4. Menurut aturan baku
   (baris = bit ke-1 dan ke-6 $=10_2=2$; kolom = bit ke-2…5 $=1010_2=10$),
   $S_1$ baris 2 kolom 10 bernilai **9** ($\code{1001}$). Nilai 4 adalah entri
   $S_6$ pada posisi yang sama. Buku memakai $S_1 \to \code{1001}$ dan
   menampilkan baris $S_1$ yang dipakai agar pembaca dapat memverifikasi.
3. **Contoh diffusion pada dek berukuran tidak konsisten.** Plainteks 16 bit
   dipetakan ke cipherteks 17 bit (`01101100000101001`). Buku memakai panjang
   16 bit agar sesuai dengan syarat panjang keluaran = panjang masukan.
4. **Rumus CFB pada dek memakai indeks campur** ($C_i$ di dalam pembaruan
   register yang seharusnya $C_j$). Buku memakai $C_j$ secara konsisten.

## Bab 07 — Analisis Algoritma Block Cipher: DES  `[x]` SELESAI
Sumber: `referensi/09-*` (5.218 kata, 16 topik, 74 gambar). Target: ±5.000 kata.
**Prioritas #1.** **Belum punya sitasi → kini menyitasi `fips46`, `biham1991`,
`matsui1994`, `eff1998`, `stallings2017`, `menezes1996`.**

Hasil: 10.473 kata berkas mentah (7.392 kata prosa pada tiga section; sisanya
tabel dan daftar butir), 29 halaman mandiri, 8 tabel baru, 4 contoh terhitung
baru, 1 program verifikasi baru (`code/python/des_uji.py`). Seluruh tabel bit dan
seluruh konstanta DES **diverifikasi ulang dengan implementasi Python** yang
mereproduksi vektor uji resmi FIPS PUB 46-3 secara persis.

- [x] **Tabel bit resmi DES**: IP, IP⁻¹ (`tab:ip-des`), E dan P (`tab:ep-des`),
  S1–S8 (`tab:sbox-des`), PC-1 dan PC-2 (`tab:pc-des`), jadwal pergeseran
  (`tab:jadwal-geser-des`)
- [x] Nilai kunci lemah (4 nilai heksadesimal) dan 6 pasangan kunci semi-lemah
  (`tab:kunci-semi-lemah-des`) — semua diverifikasi program
- [x] Sejarah DES: NBS 1972, Lucifer/Feistel (128 bit), pemangkasan NSA, NBS 1976,
  FIPS PUB 46 (1977), FIPS 46-1/2/3, penarikan 2005; pengungkapan Coppersmith 1994
- [x] Brute force terukur ($2^{56} = 72.057.594.037.927.936$; tabel laju vs waktu
  `tab:brute-force-des`) + kronologi DESCHALL 1997 / distributed.net / EFF Deep
  Crack / 22 jam 15 menit 1999 (`tab:kronologi-des`)
- [x] Contoh DES putaran demi putaran: subkunci pertama, putaran pertama lengkap
  (tujuh langkah), dan tabel jejak $(L_i, R_i)$ 17 baris sampai cipherteks resmi
  `85E813540F0AB405`
- [x] Meet-in-the-middle $X=E_{K_1}(P)=D_{K_2}(C)$ (`eq:des-mitm`) + tabel
  varian 3DES (`tab:perbandingan-double-des`) + contoh biaya memori 576 petabita
- [x] Mode DES (ECB/CBC/CFB/OFB/CTR), catatan kecepatan implementasi, dan
  misteri S-box NSA
- [x] Kriptanalisis diferensial (Biham–Shamir, $2^{47{,}2}$ pada 15 putaran →
  $2^{58}$ pada 16) dan linier (Matsui, $2^{43}$ plainteks dikenal)
- [x] 3DES: EDE, opsi dua kunci 112 bit dan tiga kunci 168 bit, alasan
  kompatibilitas (`eq:des-3des-kompatibel`), batas rekeying $2^{32}$ blok
- [x] `praktikum.tex`: Aktivitas 7.2 (satu putaran di atas kertas) dan 7.3
  (verifikasi tabel dan kunci lemah dengan program)
- [x] `latihan.tex` 3→16 butir (dua blok: konsep dan hitungan dengan tabel)
- [x] `rangkuman.tex` 7→17 butir; `evaluasi.tex` kuis 3→8, checklist 5→13 baris

### Koreksi terhadap sumber (wajib dicatat)

1. **Daftar kunci lemah pada dek `09-*` salah.** Dek menyebut empat nilai:
   `0000000000000000`, `0000000FFFFFFFF`, `FFFFFFF00000000`,
   `FFFFFFFFFFFFFFFF`. Dua di antaranya bukan bilangan heksadesimal 16 digit
   yang sah (15 digit), dan perhitungan ulang menunjukkan hanya kunci nol dan
   kunci semua-satu dari daftar itu yang benar-benar lemah. Empat kunci lemah
   yang benar adalah `0101010101010101`, `1F1F1F1F0E0E0E0E`,
   `E0E0E0E0F1F1F1F1`, `FEFEFEFEFEFEFEFE`. Buku memakai daftar yang benar.
2. **Nilai antara S-box pada literatur yang beredar sering salah kutip.** Untuk
   vektor uji resmi, keluaran tahap S-box putaran pertama adalah `5C82B597`;
   nilai `5C82B5A5` yang banyak dikutip (beserta `P = 2148ADBB`) tidak konsisten
   dengan tabel $P$ resmi. Buku memakai `5C82B597` dengan `P(S) = 234AA9BB` dan
   $R_1 = \code{EF4A6544}$, sesuai perhitungan program.
3. **Klaim "kunci lemah membuat $E_K(E_K(x)) = x$" pada buku lama hanya
   separuh benar.** Sifat itu berlaku untuk empat kunci lemah; untuk dua belas
   kunci semi-lemah yang berlaku adalah $E_{K'}(E_K(x)) = x$ dengan $K'$ adalah
   pasangannya, bukan kunci yang sama. Buku kini membedakan keduanya.

## Bab 08 — Analisis Algoritma Block Cipher: AES  `[x]` SELESAI
Sumber: `referensi/10-*` (5.580 kata, 21 topik, 55 gambar). Target: ±5.500 kata.
**Menyitasi `fips197`, `daemen2002`, `eff1998`** (dua entri `.bib` baru: `fips197`,
`daemen2002`).

Hasil: 12.968 kata berkas mentah (9.500 kata prosa pada empat section: §1 1.377,
§2 4.313, §3 1.706, §4 2.104), 36 halaman mandiri, 10 tabel, 6 contoh terhitung,
19 persamaan bernomor, 3 diagram TikZ, 2 gambar raster baru, dan satu program
verifikasi baru (`code/python/aes_uji.py`, ~342 baris). Bab semula hanya ±1.142
kata tanpa satu pun tabel bernomor, persamaan bernomor, atau contoh terhitung.
Seluruh angka pada contoh, tabel, dan latihan **dihitung ulang dengan program**
yang membangun S-box dari nol dan mencocokkan hasilnya dengan vektor uji resmi
FIPS PUB 197 untuk AES-128/192/256, pada enkripsi **dan** dekripsi.

- [x] **Dekripsi AES lengkap**: InvSubBytes (`eq:aes-invsubbytes`), InvShiftRows
  (`eq:aes-inv-shiftrows`), InvMixColumns dengan matriks `0E 0B 0D 09`
  (`eq:aes-inv-mixcolumns`), tabel S-box invers (`tab:inv-sbox-aes`), dan urutan
  dekripsi (`eq:aes-dekripsi-putaran`, `eq:aes-dekripsi`) — semula absen total
- [x] Penjelasan mengapa urutan dekripsi **bukan** cermin naif enkripsi (state
  "setengah jadi" yang diwarisi antariterasi) + dua susunan yang setara:
  *straightforward* dan *equivalent inverse cipher* dengan
  $\tilde{K}_i = \text{InvMixColumns}(K_i)$ (`eq:aes-equiv-kunci`)
- [x] Konstruksi S-box lima langkah: inisialisasi menaik, inversi $\text{GF}(2^8)$
  (`eq:aes-invers-pangkat`), vektor bit, affine $8\times8$ (`eq:aes-sbox-affine`,
  `eq:aes-sbox-rumus`), konstanta `63`; diagram TikZ `figures/konstruksi-sbox`
  + satu entri dikerjakan tangan ($\text{S-box}(\code{53}) = \code{ED}$)
- [x] Tabel S-box penuh 16×16 (`tab:sbox-aes`) dan inversnya
- [x] Key Expansion: larik $w[0..43]$, `temp`, fungsi $g$, `RC[1..10]`
  (`tab:rcon-aes`), tabel per varian (`tab:key-expansion-varian`), diagram TikZ
  `figures/key-expansion-aes`, contoh satu putaran `rk[1]` dari kunci
  ``Two One Nine Two''
- [x] AES-256: 14 putaran, aturan ganda ($g$ pada $i \bmod 8 = 0$, `SubWord` saja
  pada $i \bmod 8 = 4$) dengan contoh $w[8]$ dan $w[12]$ dari kunci FIPS A.3
- [x] Aritmetika $\text{GF}(2^8)$: penjumlahan XOR, perkalian polinomial modulo
  $x^8+x^4+x^3+x+1$ = `11B` (`eq:aes-polinom-pereduksi`), inversi
  $a^{-1} = a^{254}$; perkalian `02·26 = 4C`, `03·7B = 8D`
- [x] Tabel lima finalis AES (`tab:finalis-aes`) dan tabel parameter Rijndael
  (`tab:parameter-aes`) + perbandingan DES–AES (`tab:perbandingan-des-aes`)
- [x] Tabel transformasi per jenis putaran (`tab:transformasi-putaran-aes`)
- [x] Contoh terhitung `contoh.tex` ditulis ulang total: konvensi state kolom demi
  kolom, MixColumns + InvMixColumns, AddRoundKey involutif, jejak satu putaran,
  tabel jejak 10 putaran AES-128 (`tab:jejak-aes128`), tabel jejak dekripsi
  (`tab:jejak-dekripsi`), dan pembangkitan kunci AES-256
- [x] `praktikum.tex`: Aktivitas 8.1 (ShiftRows/InvShiftRows + konvensi kolom),
  8.2 (membangkitkan kunci putaran dengan tangan), 8.3 (memeriksa implementasi
  terhadap vektor uji resmi); dua penggalan `aes_uji.py` sebagai listing
- [x] `latihan.tex` 3→14 butir (tiga kelompok); `rangkuman.tex` 7→15 butir;
  `evaluasi.tex` kuis 3→7, checklist 5→10 baris
- [x] Justifikasi keamanan terukur: $2^{128} = 3{,}4\times10^{38}$ kunci, difusi
  penuh jauh lebih cepat daripada DES, dan alasan AES-256 lebih tahan Grover
- [x] Gambar raster baru: `perancang-aes.png` (dua perancang Rijndael) dan
  `invshiftrows-aes.png`; gambar lama `alur-enkripsi-aes.png`,
  `shiftrows-aes.png`, dan `figures/subbytes-aes` tetap dipakai

### Koreksi terhadap sumber (wajib dicatat)

1. **Angka jadwal kunci ``Two One Nine Two'' pada dek `10-*` salah.** Dek
   menuliskan RotWord$(w[3]) = (54, 77, \code{6E}, 20)$ dan
   $\text{SubWord} = (20, F5, \code{9F}, B7)$, sehingga
   $w[4] = (75, 82, \code{F0}, 97)$ dan seterusnya. Byte terakhir $w[3]$ adalah
   `6F`, bukan `6E`, sehingga RotWord yang benar adalah $(54,77,\code{6F},20)$,
   $\text{SubWord} = (20, F5, \code{A8}, B7)$, dan $w[4] = \code{7582C797}$.
   Rantai dek juga tidak konsisten dengan dirinya sendiri: dari
   $w[4] = (75,82,F0,97)$ seharusnya $w[5] = \code{3AEC95B7}$, tetapi dek
   menuliskan `3AEC96B7`. Nilai yang benar, sesuai tabel S-box resmi FIPS PUB 197:
   $w[4] = \code{7582C797}$, $w[5] = \code{3AECA2B7}$, $w[6] = \code{7485CCD2}$,
   $w[7] = \code{54D1BBBD}$. Buku memakai nilai yang benar dan menambahkan kotak
   *Catatan koreksi* pada Sub-bab KeyExpansion (§3).
2. **Catatan yang benar tentang AES-256.** Dek menyebut aturan ganda AES-256
   (baris $i \bmod 8 = 0$ dan $i \bmod 8 = 4$) dengan tepat; buku hanya
   memperjelas *mengapa* `SubWord` tambahan itu perlu, yaitu mencegah sebagian
   kunci putaran menjadi fungsi linier dari kunci pengguna.
3. **Contoh aritmetika $\text{GF}(2^8)$ pada dek sudah benar**
   ($\code{0D}+\code{06}=\code{0B}$, $\code{57}+\code{83}=\code{D4}$,
   $\code{57}\cdot\code{83}=\code{C1}$, matriks InvMixColumns `0E 0B 0D 09`).
   Tidak ada koreksi; angka itu tetap dipakai sebagai bahan §4.

## Bab 09 — Studi Algoritma Block Cipher Lainnya  `[x]` SELESAI
Sumber: `referensi/11-*` (3.352 kata, 11 topik, 19 gambar). Target: ±4.500 kata.
**Menyitasi 13 kunci** (13 entri `.bib` baru: `rfc5830`, `rfc4357`, `rfc7801`,
`rfc8891`, `rivest1994rc5`, `rivest1998rc6`, `schneier1994blowfish`,
`schneier1998twofish`, `anderson1998serpent`, `burwick1998mars`,
`courtois2011gost`, `isobe2011gost`, `dinur2012gost`).

Hasil: 9.135 kata pada delapan berkas (tiga section 5.844, contoh 1.735,
praktikum 722, rangkuman 414, evaluasi 219, latihan 201), **29 halaman mandiri**,
10 tabel bernomor, 4 contoh terhitung, 7 persamaan bernomor, 5 diagram TikZ baru,
dan satu program verifikasi baru (`code/python/rc5_gost_uji.py`, 326 baris). Bab
semula hanya ±1.400 kata tanpa satu pun persamaan bernomor maupun contoh
terhitung. Seluruh angka pada contoh, tabel, dan latihan **dihitung ulang dengan
program**: implementasi RC5 umum ($w$, $r$, $b$) dicocokkan terhadap **17 vektor
uji resmi RFC 2040** dan implementasi fungsi putaran GOST dicocokkan terhadap
Contoh~\ref{ex:gost-round}.

- [x] **Koreksi keamanan GOST** (Temuan #1) — Sub-bab *Kriptanalisis GOST dan Batas
  Rekeying* (`subsec:kriptanalisis-gost`) dengan
  Tabel~\ref{tab:kompleksitas-serangan-gost} ($2^{256} \to 2^{228} \to 2^{178}$,
  data $2^{64}$, memori $2^{70}$; Dinur dkk.\ $2^{224}$/$2^{192}$), penurunan batas
  rekeying $2^{64/2} = 2^{32}$ blok $= 2^{35}$ byte $\approx 32$ GiB, dan kotak
  `\important` yang melarang kesimpulan "GOST lebih aman daripada DES".
  Nada di `praktikum.tex` diperbaiki: butir lama "jumlah putaran lebih banyak
  cenderung lebih aman" diganti menjadi perbandingan GOST versus Serpent yang
  sama-sama 32 putaran tetapi bercatatan keamanan berbeda
- [x] Identitas standar GOST 28147-89 → Magma (GOST R 34.12-2015) → Kuznyechik:
  Sub-bab *Riwayat dan Identitas Standar* + Tabel~\ref{tab:parameter-gost},
  termasuk penjelasan mengapa Kuznyechik bukan "GOST 28147-89 versi baru"
- [x] Jadwal kunci RC5 lengkap: larik $L$ dengan urutan *little-endian*
  (termasuk aturan pengisian nol), $S[0]=P_w$, $S[i]=S[i-1]+Q_w$, pencampuran
  $n = 3\cdot\max(t,c)$ langkah — Persamaan~\eqref{eq:jadwal-kunci-rc5};
  penurunan $P_w$ dan $Q_w$ dari $e$ dan $\phi$
  (Persamaan~\eqref{eq:pw-qw}, Tabel~\ref{tab:konstanta-pw-qw}) beserta alasan
  *nothing up my sleeve*
- [x] Algoritma enkripsi dan dekripsi RC5
  (Persamaan~\eqref{eq:rc5-putaran}), penjelasan rotasi bergantung data dan
  mengapa dekripsi harus menempuh putaran dalam urutan terbalik; RC6
  (Persamaan~\eqref{eq:rc6-putaran}) dengan penjelasan mengapa $x(2x+1)$
  merupakan pemetaan satu-ke-satu modulo $2^w$
- [x] Tabel jadwal kunci putaran GOST 32 putaran (`tab:jadwal-kunci-gost`, 17 kolom,
  `\footnotesize` + `\tabcolsep=4pt`), tabel Kotak-S lengkap
  (`tab:kotak-s-gost`), dan contoh pemecahan kunci
  ``abcdefghijklmnopqrstuvwxyz123456'' → $K_1=\text{abcd}$ … $K_8=\text{3456}$;
  fungsi putaran dalam Persamaan~\eqref{eq:putaran-gost} dan
  \eqref{eq:fungsi-f-gost} + diagram `figures/putaran-gost`
- [x] Kedalaman keempat cipher lain, masing-masing satu diagram TikZ baru:
  Blowfish (fungsi $F$, `figures/fungsi-f-blowfish`,
  Persamaan~\eqref{eq:fungsi-f-blowfish}, prosedur 1042 kata / 521 enkripsi dari
  digit $\pi$), Twofish (`figures/fungsi-g-twofish`, matriks MDS + PHT),
  Serpent (`figures/putaran-serpent`), dan MARS (`figures/mars-mixing`,
  tiga fase 8+16+8)
- [x] Gambar raster tabel perbandingan cipher simetris **dihapus** dan diganti
  tabel `booktabs`/`tabularx` sungguhan (`tab:perbandingan-cipher-simetris`,
  sembilan algoritma); berkas `figures/perbandingan-block-cipher.png`
  (140 KB) dihapus karena sudah tidak dirujuk
- [x] `contoh.tex` ditulis ulang total menjadi empat `example` bernomor:
  (1) `ex:rc5-jadwal` — enam langkah jadwal kunci RC5-32/0/1 dengan kunci
  satu byte, tabel jejak `tab:jejak-jadwal-kunci-rc5`, hasil
  $S[0]=\code{4DBA7B7A}$, $S[1]=\code{1E1D1179}$;
  (2) `ex:rc5-kecil` — enkripsi penuh RC5-16/2/2 langkah demi langkah, dengan
  catatan eksplisit bahwa keenam nilai $S[i]$ dipilih untuk ilustrasi;
  (3) `ex:rc5-vektor` — larik $S$ 18 kata RC5-32/8/1, penyaringan CBC
  ($A_0=\code{44332211}$, $B_0=\code{88776655}$), tabel jejak delapan putaran
  `tab:jejak-putaran-rc5`, dan pemeriksaan terhadap vektor RFC 2040
  `9646fb77638f9ca8`;
  (4) `ex:gost-round` — satu putaran GOST dengan tabel substitusi
  `tab:jejak-substitusi-gost` ($\code{7396B9DC} \to \code{416DCF77} \to
  \code{6E7BBA0B} \to R_i = \code{6F79B90F}$)
- [x] `praktikum.tex`: Aktivitas 9.1 (perbandingan struktur, butir menyesatkan
  diperbaiki) tetap, ditambah 9.2 (jadwal kunci RC5 dengan tangan), 9.3
  (memeriksa terhadap vektor RFC 2040), 9.4 (fungsi putaran GOST dengan tangan
  + uji avalanche satu bit), 9.5 (menghitung batas rekeying dan menilai
  kriptanalisis GOST); tiga penggalan `rc5_gost_uji.py` sebagai listing
- [x] `latihan.tex` 3 → 8 butir (dua kelompok `obereflection`); butir lama 2
  dipersempit agar hanya membahas pencarian kunci menyeluruh;
  `rangkuman.tex` 7 → 11 butir; `evaluasi.tex` kuis 3 → 6, checklist 5 → 7 baris
- [x] Program verifikasi baru `code/python/rc5_gost_uji.py` (326 baris, ASCII + LF):
  RC5 umum ($w$, $r$, $b$) + CBC, GOST RFC 4357/5830, dan empat blok pengujian
  mandiri. Ketujuh belas vektor RFC 2040 adalah kutipan langsung dari §9.2–9.3
  RFC; seluruhnya **lulus** ketika dijalankan

### Koreksi terhadap sumber (wajib dicatat)

1. **Klaim keamanan GOST pada dek `11-*` menyesatkan** dan telah tersebar ke
   buku versi lama. Dek hanya menyebut "kunci 256 bit … lebih tahan terhadap
   *brute force*" tanpa menyebut satu pun hasil kriptanalisis, padahal dek itu
   sendiri memuat bagian *Cryptanalysis of GOST* yang menyatakan kompleksitas
   serangan turun dari $2^{256}$ ke $2^{178}$ dan Courtois menyebut GOST
   "a deeply flawed cipher". Buku kini memuat kedua sisi itu sekaligus dan
   menambahkan batas rekeying $2^{32}$ blok yang tidak ada di dek.
2. **Tabel perbandingan cipher simetris pada dek salah dua angka.** Panjang
   kunci Blowfish tertulis "1 sampai 448 bit" (spesifikasi resminya menetapkan
   paling sedikit 32 bit), dan panjang kunci RC5 tertulis "128 sampai 256 bit"
   (RC5 justru dapat dipilih dari 0 sampai 2040 bit; 128–256 bit itu panjang
   kunci Rijndael). Keduanya diperbaiki pada
   Tabel~\ref{tab:perbandingan-cipher-simetris} dan didokumentasikan di paragraf
   penutup Sub-bab *Perbandingan Cipher Simetris*.
3. **Twofish disebut memiliki lima kotak-S.** Yang benar adalah empat kotak-S
   $8 \times 8$ yang bergantung pada kunci, masing-masing disusun dari permutasi
   tetap $q_0$ dan $q_1$. Koreksi ini dicatat langsung di dalam §3, karena sifat
   *bergantung kunci* itulah yang menjadi ciri khas sekaligus kelemahan
   keluarga Blowfish–Twofish di perangkat keras.
4. **MARS disebut melakukan substitusi–permutasi pada setiap putaran.** MARS
   sebenarnya adalah Feistel tak seimbang (*unbalanced Feistel*) dengan tiga fase
   yang berbeda sifatnya. Koreksi ini disertai penguraian 8 putaran *forward
   mixing* + 16 putaran inti + 8 putaran *backward mixing*
   (`figures/mars-mixing`).
5. **Kotak-S GOST nomor 6 pada dek berakhir `14 14`.** Kedelapan kotak-S GOST
   harus merupakan permutasi dari 0 sampai 15, sehingga `14 14` jelas salah dan
   yang benar adalah `14 15`. Kesalahan ini diverifikasi dengan program: buku
   memakai `14 15`, dan `rc5_gost_uji.py` memeriksa sifat permutasi itu pada
   setiap kali dijalankan.
6. **Kode semu jadwal kunci RC5 pada dek mengandung dua salah tulis**:
   $n = 3\cdot\max(r, c)$ seharusnya $n = 3\cdot\max(t, c)$ (dengan $t = 2r+2$,
   bukan $r$), dan pada baris pembaruan tertulis $i \leftarrow (l+1) \bmod t$
   dengan huruf $l$, bukan $i$. Keduanya diperbaiki pada
   Persamaan~\eqref{eq:jadwal-kunci-rc5}, dan urutan pembaruan $X$/$Y$ yang
   benar ditegaskan secara eksplisit karena menukarnya menghasilkan larik $S$
   yang tidak kompatibel dengan vektor uji resmi.
7. **Vektor uji yang dipakai buku diverifikasi ulang dari sumber primer.**
   Penurunan jadwal kunci RC5 pertama kali dilakukan dengan menerka urutan
   pembaruan; nilai yang diperoleh dari ingatan/hasil pencarian tidak cocok
   dengan implementasi mana pun. Setelah program diuji terhadap keenam belas
   vektor pada §9.3 RFC 2040, urutan yang benar ditemukan dan seluruh vektor
   lulus. Angka pada `contoh.tex` berasal dari sumber primer itu, bukan dari
   dek.

## Bab 10 — Algoritma RSA  `[x]` SELESAI
Sumber: `referensi/13-*` (6.603 kata, 20 topik, 17 gambar). Target: ±5.000 kata.
**Menyitasi 7 kunci baru** (`atkins1995rsa129`, `boneh1999`, `shor1997`,
`bellare1994oaep`, `bleichenbacher1998`, `rfc8017`, `fips203`); dua sitasi lama
(`rsa1978`, `diffie1976`) tetap dipakai. `references.bib` 49 entri.

Hasil: 8.869 kata pada sembilan berkas (empat section 5.630, contoh 1.393,
praktikum 743, rangkuman 493, latihan 333, evaluasi 277), **29 halaman mandiri**,
8 tabel bernomor, 6 contoh terhitung, 15 persamaan bernomor, 12 subbagian baru
(8 → 20), 1 diagram TikZ baru + 1 gambar raster yang disisipkan kembali, dan satu
program verifikasi baru (`code/python/rsa_uji.py`, 331 baris, sembilan blok
pengujian yang seluruhnya **lulus**). Bab semula 1.360 kata tanpa satu pun
persamaan bernomor, tanpa contoh terhitung, dan tanpa program pengujian.

- [x] **Penurunan rumus RSA dari Teorema Euler** — Sub-bab *Penurunan Rumus
  Enkripsi dan Dekripsi* (`sec:landasan-rsa`) dengan lingkungan `definition`
  (fungsi totient Euler) dan `theorem` (Teorema Euler), lalu rantai bernomor
  Persamaan~\eqref{eq:totient-prima} → \eqref{eq:totient-rsa} (dengan
  justifikasi kombinatorial) → \eqref{eq:ed-kongruen} →
  \eqref{eq:ed-kelipatan} → \eqref{eq:rsa-pangkat} → \eqref{eq:rsa-bukti} →
  \eqref{eq:rsa-rumus}. Ditutup dengan argumen CRT yang membuktikan dekripsi
  benar untuk **semua** $0 \le m < n$, bukan hanya $m$ yang relatif prima
  terhadap $n$ — kasus yang tidak dibahas dek sama sekali
- [x] Contoh totient $\varphi(20) = 8$ beserta kedelapan residu koprima $1, 3, 7,
  9, 11, 13, 17, 19$ dan contoh Teorema Euler $a = 3$, $n = 10$, $3^4 = 81
  \equiv 1 \pmod{10}$
- [x] **Contoh multi-blok ``HELLO ALICE''** lengkap (Contoh~\ref{ex:rsa-hello-alice}):
  $m = 07041111140011080204$ → blok $0704, 1111, 1400, 1108, 0204$ →
  $C = 0328, 0301, 2653, 2986, 1164$ → dekripsi dengan $d = 1019$.
  Meliputi Tabel~\ref{tab:pengodean-hello} (pengodean per huruf),
  blok `aligned` lima enkripsi, dan Tabel~\ref{tab:jejak-hello-alice} (jejak
  huruf → angka → cipherteks → huruf kembali). Ditambah paragraf yang menerangkan
  mengapa $c_2 = 0301$ **wajib** ditulis empat digit dan mengapa
  $c_1 = 0704$ harus dipecah dengan $k = 4$ meskipun rumus panjang blok hanya
  menjamin $k \le 3$ (kode dua huruf terbesar, 2525, masih di bawah $n = 3337$)
- [x] **Algoritma Euclidean diperluas menggantikan coba-coba pada $k$** —
  Sub-bab *Menghitung Kunci Privat dengan Algoritma Euclidean Diperluas*:
  identitas Bézout \eqref{eq:bezout}, Tabel~\ref{tab:euclid-dipertluas} rekursi
  $r_i, s_i, t_i$ lengkap, dan Contoh~\ref{ex:euclid-rsa} yang memperoleh
  $d = 1019$ dalam **lima pembagian** alih-alih 25 percobaan $k$. Ini
  memperbaiki cara pengajaran dek yang hanya memakai coba-coba
- [x] Dua tabel baru: **parameter dan kerahasiaannya** (Tabel~\ref{tab:properti-rsa}:
  $p, q, n, \varphi(n), e, d, m, c$) dan **ukuran kunci versus rekor pemfaktoran**
  (Tabel~\ref{tab:ukuran-kunci-rsa}: 256 sampai 3072 bit) yang diletakkan
  berdampingan dengan kronologi RSA-129 (1994) → RSA-250 (829 bit, 2020)
- [x] **Ancaman komputasi kuantum** (Algoritma Shor) dalam Sub-bab *Ancaman
  Komputasi Kuantum*: mengapa Grover hanya kuadratik sehingga AES-256 cukup
  sedangkan RSA tidak punya penangkal, pola *harvest now, decrypt later*, dan
  migrasi ke kriptografi pasca-kuantum (NIST FIPS 203, Agustus 2024)
- [x] Sub-bab baru **Kriptografi Hibrida** (empat langkah eksplisit
  \eqref{eq:...} + diagram `figures/kriptografi-hibrida`) menjelaskan mengapa RSA
  jarang dipakai langsung untuk pesan dan bagaimana kunci sesi AES-256 dibungkus
  dengan RSA — jembatan menuju Bab 11
- [x] Sub-bab baru **Padding OAEP dan Keamanan Semantik** (`subsec:padding-oaep`):
  determinisme, serangan kamus (Tabel~\ref{tab:kamus-rsa} 26 huruf dibangkitkan
  hanya dari kunci publik), kerapuhan perkalian
  $c' = c \cdot s^e \bmod n = (m \cdot s)^e \bmod n$ \eqref{eq:kerapuhan-rsa},
  struktur blok PKCS \#1 v1.5, Bleichenbacher 1998, dan OAEP
  (Bellare–Rogaway 1994, RFC 8017)
- [x] **Tabel ringkasan 7 keluarga serangan RSA** (Tabel~\ref{tab:serangan-rsa}:
  serangan/prinsip/penangkalan), termasuk serangan Man-in-the-Middle yang
  diuraikan sebagai narasi Carol, dan batas 245 byte pesan untuk RSA-2048
  dengan PKCS \#1 v1.5
- [x] **Himpunan parameter kedua** $p = 7$, $q = 11 \Rightarrow n = 77$,
  $\varphi = 60$, $d = 43$, $8^7 \bmod 77 = 57$; ditambah parameter latihan
  ketiga $e = 17$ pada modulus yang sama ($d = 2273$) di `latihan.tex`
- [x] **Contoh terhitung** 4 → 6 (`contoh.tex`, seluruhnya memakai
  $p=47, q=71, e=79$): pembangkitan kunci, satu blok, HELLO ALICE, dan
  kerapuhan RSA telanjang (determinisme blok $0203$ menghasilkan $1488$ dua
  kali, plus perubahan $c = 1493 \to c' = 2304$ yang didekripsi menjadi
  $48 = 16 \times 3$)
- [x] Program verifikasi `code/python/rsa_uji.py` (331 baris, ASCII + LF):
  `pbb`, `euclid_diperluas` (dengan jejak per langkah), `invers_modulo`,
  pembangkitan kunci, enkripsi/dekripsi, pengodean–pemecahan–penyambungan blok
  dengan penjagaan nol di depan, kamus huruf & serangan kamus, peragaan
  kerapuhan, dan perkiraan pemfaktoran berdasarkan panjang modulus. Sembilan
  blok pengujian memeriksa ulang setiap angka pada contoh, tabel, dan latihan;
  keluaran akhir `Seluruh pengujian LULUS`
- [x] `latihan.tex` 3 → 9 butir (dua kelompok `obereflection`, termasuk butir
  Fermat $p=1000003, q=1000033$ dengan pemeriksaan $\lceil\sqrt{n}\rceil^2 - n$
  sebagai kuadrat sempurna, estimasi $2^{512} \approx 1{,}34 \times 10^{154}$,
  dan pertanyaan pasca-kuantum); `rangkuman.tex` → 15 butir;
  `evaluasi.tex` kuis 3 → 6, checklist 6 → 11 baris; `praktikum.tex` 1 → 5
  aktivitas dengan empat kutipan listing dari `rsa_uji.py`

### Koreksi terhadap sumber (wajib dicatat)

1. **$\varphi(n)$ pada dek salah hitung.** Dek menulis
   $\varphi(n) = (p-1)(q-1) = 46 \times 60 = 3220$ untuk $p = 47$, $q = 71$.
   Faktor keduanya seharusnya $q - 1 = 70$, bukan 60: $46 \times 60 = 2760$
   jelas tidak sama dengan 3220. Produk yang benar tetap 3220, sehingga
   $d = 1019$ pada dek kebetulan tidak terpengaruh — tetapi baris itu
   mengajarkan langkah yang salah dan sudah diperbaiki menjadi
   $46 \times 70 = 3220$ di `contoh.tex` dan `section-02.tex`.
2. **Deretan kode ``HELLO ALICE'' pada dek berlebih satu blok.** Dek menulis
   $m = 070411111140011080204$ (21 digit), yang tidak habis dibagi empat
   sehingga terpecah menjadi enam blok alih-alih lima. Deretan yang benar adalah
   $07041111140011080204$ (20 digit) — dek menyisipkan satu ``11'' berlebih.
   Kesalahan ini diperbaiki dan diverifikasi program
   (`rsa_uji.py`, UJI 4 memeriksa `len(kode) == 20`).
3. **Label blok kelima pada dek tertukar.** Dek menulis $m_1 = 204 \to c_5$
   untuk blok terakhir; seharusnya $m_5 = 0204 \to c_5 = 1164$. Notasi pada dek
   mencampur indeks 1 dan 5 dalam satu baris. Diperbaiki menjadi berindeks lima
   yang konsisten, dan nol di depan ditulis eksplisit karena itulah justru inti
   pelajarannya.
4. **Cara menghitung $d$ pada dek tidak dapat dipakai untuk modulus nyata.**
   Dek hanya menyebut ``dicoba nilai $k$ sampai pembilang habis dibagi''.
   Untuk $n = 3337$ cara itu masih dapat dikerjakan dengan tangan, tetapi
   untuk modulus 617 digit (RSA-2048) tidak ada nilai $k$ yang dapat ditemukan
   dengan cara itu. Buku menambahkan Algoritma Euclidean diperluas sebagai
   cara yang benar dan menunjukkan bahwa ia memerlukan lima pembagian untuk
   parameter yang sama. Ini bukan kesalahan angka, melainkan kesalahan metode.
5. **Klaim ketahanan RSA-129 pada dek terbalik arahnya.** Dek menyebut
   tantangan RSA-129 (1977) dan pemecahannya pada 1994, tetapi menyajikannya
   sebagai bukti keunggulan RSA. Buku menambahkan pembacaan yang jujur: Rivest
   memperkirakan $4 \times 10^{16}$ tahun sedangkan kenyataannya delapan bulan,
   dan kemajuan pemfaktoran selalu lebih cepat daripada perkiraan — itulah
   alasan RSA-1024 kini dianggap terlalu tipis meskipun belum dipecahkan.
6. **Dek tidak menyebut OAEP maupun Bleichenbacher.** Bagian *padding* pada dek
   berhenti pada PKCS \#1 v1.5 tanpa menyebut bahwa skema itu sendiri dapat
   diserang. Buku menambahkan Sub-bab~\ref{subsec:padding-oaep} lengkap dengan
   serangan Bleichenbacher 1998 dan OAEP, karena tanpa keduanya pembaca akan
   menyimpulkan bahwa memakai padding sudah cukup untuk mengamankan RSA.

## Bab 11 — Protokol Diffie-Hellman  `[x]` SELESAI
Sumber: `referensi/15-*` (2.457 kata, 8 topik, 11 gambar). Target: ±4.000 kata.
**Menyitasi 5 kunci baru** (`hellman2002`, `diffie1992`, `rfc7919`, `rfc8446`,
`adrian2015logjam`); dua sitasi lama (`diffie1976`, `stallings2017`) tetap
dipakai. Bab ini semula **tanpa satu pun sitasi**. `references.bib` 54 entri.

Hasil: 8.623 kata pada sembilan berkas (empat section 5.377, contoh 1.341,
praktikum 662, rangkuman 510, latihan 432, evaluasi 301), **30 halaman mandiri**,
5 tabel bernomor, 6 contoh terhitung, 5 persamaan bernomor, 13 subbagian baru
(5 → 18), 3 diagram TikZ baru + 3 gambar raster (2 disisipkan kembali, 1 baru
disalin dari referensi), dan satu program verifikasi baru
(`code/python/dh_uji.py`, 357 baris, sepuluh blok pengujian yang seluruhnya
**lulus**). Bab semula 1.415 kata tanpa subbagian bernama, tanpa persamaan
bernomor, tanpa contoh terhitung, dan tanpa program pengujian.

- [x] **Kriptografi hibrida dengan persamaan eksplisit + diagram** — Subbagian
  *Kriptografi Hibrida secara Terperinci* (`subsec:hibrida-eksplisit`) memuat
  enam langkah bernomor dengan rumus $E_{\text{RSA},\text{PK}_{\text{Bob}}}(K) = C_K$,
  $E_{\text{AES},K}(M) = C_M$, $D_{\text{RSA},\text{SK}_{\text{Bob}}}(C_K) = K$,
  dan $D_{\text{AES},K}(C_M) = M$, ditutup diagram baru
  Gambar~\ref{fig:hibrida-pesan-dh} (TikZ) dan paragraf yang menerangkan mengapa
  urutan pemulihan langkah 5 dan 6 tidak dapat ditukar
- [x] **Serangan MITM dengan dua kunci bersama eksplisit** — Subbagian
  *Serangan Man-in-the-Middle* (`subsec:mitm-dh`) dengan
  Tabel~\ref{tab:alur-mitm} (alur empat pesan), lingkungan `align` bernomor
  Persamaan~\eqref{eq:mitm-k1} dan \eqref{eq:mitm-k2}, diagram baru
  Gambar~\ref{fig:mitm-dh}, dan Contoh~\ref{ex:dh-mitm} yang menghitung
  $M = 3^{101} \bmod 353 = 63$, $K_1 = 257$, dan $K_2 = 249$ secara numerik.
  Ditambah Subbagian *Mengapa Serangan Itu Berhasil dan Bagaimana Menangkalnya*
  dengan empat penangkal, termasuk *Station-to-Station* (`diffie1992`)
- [x] **Protokol tiga pihak lengkap (12 langkah)** — Subbagian *Pertukaran Kunci
  Tiga Pihak* memuat seluruh dua belas langkah dek (versi lama buku memangkas
  dua leg), diagram melingkar baru Gambar~\ref{fig:dh-tiga-pihak}, dan catatan
  bahwa jumlah pengiriman tumbuh secepat $n(n-1)$ sehingga hanya praktis untuk
  kelompok kecil
- [x] **Catatan sejarah "Diffie–Hellman–Merkle"** — Subbagian *Sejarah Singkat
  dan Penamaan* dengan potret
  Gambar~\ref{fig:pionir-dh} (raster baru disalin dari referensi), kutipan
  Hellman (`hellman2002`) bahwa nama yang adil adalah *Diffie--Hellman--Merkle*,
  dan catatan Penghargaan Turing 2015
- [x] **Contoh numerik kedua ($G = 1601$, $N = 4789$)** — Contoh~\ref{ex:dh-1601}
  dengan $x = 20 \Rightarrow A = 2716$, $y = 4 \Rightarrow B = 1302$, dan
  $K = 4257$ dari kedua sisi, beserta pembahasan mengapa $y = 4$ yang sangat
  kecil tidak berbahaya selama $A$ tidak ikut tersadap
- [x] **Lima tabel bernomor** — Tabel~\ref{tab:hibrida-vs-dh} (hibrida versus
  pertukaran kunci), Tabel~\ref{tab:akar-primitif} (pangkat $g = 7$ dan $g = 3$
  modulo 11), Tabel~\ref{tab:alur-mitm}, Tabel~\ref{tab:ukuran-dh} (panjang
  modulus versus tingkat keamanan), dan Tabel~\ref{tab:serangan-dh} (empat
  serangan khusus beserta penangkalnya)
- [x] **Pemilihan parameter yang tidak dibahas dek sama sekali** — Subbagian
  *Pemilihan Parameter dan Ukuran yang Memadai* (`subsec:parameter-dh`): panjang
  modulus minimum, *safe prime* $p = 2q+1$ dan subgrup berorde prima, kisah
  pembangkit acak lemah Debian OpenSSL 2008, dan grup bernama RFC 7919
  (`rfc7919`)
- [x] **Analisis lengkap masalah logaritma diskret** — Subbagian *Masalah
  Logaritma Diskret* (`subsec:dlog-dh`) dengan Persamaan~\eqref{eq:dlp} dan
  \eqref{eq:dlp-index-calculus}, penjelasan *index calculus*, serta algoritma
  **langkah raksasa-bayi** yang tidak ada di dek: untuk $p = 353$ diperoleh
  $m = \lceil\sqrt{352}\rceil = 19$ dan $a = 97$ ditemukan dalam **24 perkalian**
  alih-alih 97 langkah pencarian menyeluruh
- [x] **Serangan Logjam sebagai serangan penurunan parameter** — Subbagian
  *Serangan Khusus terhadap Diffie--Hellman* menegaskan bahwa Logjam 2015
  (`adrian2015logjam`) tidak menyerang matematikanya, melainkan menurunkan
  negosiasi ke modulus ekspor 512 bit yang sudah dipecahkan
- [x] **Forward secrecy dan TLS 1.3** — Subbagian *Kunci Sesaat dan Forward
  Secrecy* (`subsec:forward-secrecy`): DHE, mengapa kunci jangka panjang yang
  bocor tidak membuka rekaman lama, dan mengapa TLS 1.3 (`rfc8446`) mewajibkan
  pertukaran kunci sesaat
- [x] **Program verifikasi** `code/python/dh_uji.py` — 357 baris, ASCII + LF,
      sepuluh banner komentar tepat 68 karakter. Memuat `pbb`, `prima`,
      `faktorisasi`, `siklus_pangkat`, `orde`, `akar_primitif`,
      `kunci_publik`, `kunci_bersama`, `pertukaran`, `tiga_pihak`,
      `langkah_raksasa_bayi`, `serang_mitm`, dan `perkirakan_keamanan`, lalu
      sepuluh blok `uji_*` yang **seluruhnya lulus** (baris terakhir:
      `Seluruh pengujian LULUS`). Empat blok disisipkan ke `praktikum.tex`
      sebagai Listing~\ref{lst:dh-parameter}, \ref{lst:dh-serangan}, dan
      \ref{lst:dh-keamanan}
- [x] **Pertumbuhan komponen OBE** — `praktikum.tex` 4 → 5 `obeactivity`,
      `latihan.tex` 1 → 2 `obereflection` (13 butir), `rangkuman.tex` 12 butir,
      `evaluasi.tex` 6 butir kuis dan **`competencychecklist` 5 → 12 baris**

### Koreksi terhadap sumber (wajib dicatat)

**Berbeda dari seluruh dek yang sudah diproses, dek `15-*` tidak memuat satu pun
angka yang salah.** Seluruh nilai yang dipakai buku telah diperiksa ulang dengan
`code/python/dh_uji.py` sebelum ditata huruf:

| Klaim dek | Verifikasi |
|---|---|
| $p = 353$, $g = 3$, $a = 97 \Rightarrow A = 40$ | lulus (UJI 4) |
| $p = 353$, $b = 233 \Rightarrow B = 248$, $K = 160$ | lulus (UJI 4) |
| $G = 1601$, $N = 4789$, $x = 20 \Rightarrow A = 2716$ | lulus (UJI 6) |
| $y = 4 \Rightarrow B = 1302$ | lulus (UJI 6) |
| $\varphi(352) = 160$ akar primitif $p = 353$ | $352 \times \tfrac{1}{2} \times \tfrac{10}{11} = 160$ |
| akar primitif $g = 3$ modulo 11 berode 5 | lulus (UJI 2) |
| $p = 23$ *safe prime* ($23 = 2 \times 11 + 1$) | $q = 11$ prima |

Dua koreksi berikut menyangkut **buku**, bukan dek:

1. **`latihan.tex` semula menyebut "19 langkah langkah raksasa-bayi"** untuk
   menemukan $a = 97$. Angka 19 adalah $m = \lceil\sqrt{p-1}\rceil$, yaitu ukuran
   tabel langkah bayi, **bukan** jumlah perkalian. Yang benar adalah **24
   perkalian** (`m + i` dengan $i = 5$, sebab $97 = 5 \cdot 19 + 2$), sesuai
   keluaran program. Sekaligus membetulkan kata berulang "langkah langkah".
2. **Dua gambar raster lama hilang saat penulisan ulang** dan harus disisipkan
   kembali: `figures/analogi-cat-dh.png` (analogi pencampuran cat) dan
   `figures/contoh-numerik-dh.png` (contoh $p = 11$, $g = 7$ lengkap dengan kolom
   penyadap). Keduanya masih dirujuk `\ref` dari `section-01.tex` sehingga tanpa
   penyisipan kembali keduanya menjadi rujukan menggantung. Gambar pertama
   diletakkan di Subbagian *Analogi Pencampuran Cat*, gambar kedua di
   `contoh.tex` setelah Contoh~\ref{ex:dh-kecil} — tempat keduanya paling
   berguna bagi pembaca.

## Bab 12 — Algoritma ElGamal
Sumber: `referensi/14-*` (2.160 kata, 5 topik). Target: ±4.000 kata.

- [ ] **Contoh multi-blok "HALO"** dengan dua kunci sesaat ($k=1463$, $k=2001$)
- [ ] Contoh akar primitif + logaritma diskret
- [ ] Bukti identitas dekripsi $b/a^x \equiv m$ (environment `equation`)
- [ ] Contoh lengkap kedua dengan $p=2357$

## Bab 13 — Algoritma Knapsack
Sumber: `referensi/16-*` (2.499 kata, 7 topik, 3 gambar). Target: ±4.000 kata.

- [ ] Contoh knapsack dasar (non-superincreasing)
- [ ] Contoh greedy superincreasing $\{2,3,6,13,27,52\}$
- [ ] Himpunan parameter Merkle–Hellman alternatif
- [ ] Parameter penerapan + estimasi brute force + serangan Shamir
- [ ] `contoh.tex` → environment `example`

## Bab 14 — Kriptografi Kurva Eliptik
Sumber: `referensi/17-*` (2.883) + `18-*` (5.706). Target: ±5.500 kata.
**Belum punya sitasi.**

- [ ] ECEG lengkap + tabel perbandingan ElGamal vs EC-ElGamal
- [ ] Metode Koblitz *encoding* pada $y^2\equiv x^3-x+188 \pmod{751}$
- [ ] Aritmetika $GF(2^m)$
- [ ] Kedalaman aljabar abstrak (grup/medan, $F_{23}$)
- [ ] Geometri kurva + penurunan analitik rumus $P+Q$ dan $2P$
- [ ] Enumerasi penuh EC atas $GF(11)$
- [ ] `contoh.tex` → `example`; tambah sitasi

## Bab 15 — Fungsi Hash dan MAC (tanpa sumber referensi)
Sumber: `menezes1996` (HAC Bab 9), `stallings2017`, `katz2020`, FIPS 180-4, FIPS 202,
SP 800-107, SP 800-38B, RFC 4231. Target: ±5.000 kata.

- [ ] Mekanisme internal kompresi MD5/SHA-1/SHA-2 + gambar alur
- [ ] Vektor uji nyata (RFC 4231 / jejak kompresi SHA-256)
- [ ] Serangan tabrakan nyata: Wang 2004, SHAttered
- [ ] SHA-3/Keccak: rate/capacity, Keccak-f[1600], padding
- [ ] MAC selain HMAC: CBC-MAC, CMAC, GMAC/Poly1305, UMAC; AEAD
- [ ] Notasi formal PRF/PRP, EUF-CMA, batas ulang tahun
- [ ] Gambar + entri `.bib`

## Bab 16 — Otentikasi dan Tanda Tangan Digital (tanpa sumber referensi)
Sumber: `stallings2017`, `menezes1996`, `rsa1978`, `katz2020`, FIPS 186-5, RFC 5280,
RFC 8032, RFC 8446. Target: ±5.000 kata.

- [ ] X.509 v3 penuh (ASN.1) + contoh sertifikat nyata
- [ ] TLS 1.2 vs 1.3: urutan pesan handshake + key schedule
- [ ] Validasi sertifikat: jalur, name constraints, CRL vs OCSP
- [ ] Schnorr, EdDSA/Ed25519, RSA-PSS + tabel perbandingan DSA/ECDSA/EdDSA
- [ ] Permukaan serangan padding: PKCS#1 v1.5 vs PSS, Bleichenbacher, ROCA
- [ ] Vektor uji nyata (RFC 8032 / NIST CAVP)
- [ ] Otentikasi timbal balik, signcryption, certificate transparency
- [ ] Gambar + entri `.bib`

---

## Cacat lintas bab yang harus diperbaiki sambil jalan

- [x] **Bab 09 menyesatkan soal keamanan GOST** — buku menyiratkan GOST "lebih aman";
  referensi `11-*` menyatakan sebaliknya (2²⁵⁶ → 2¹⁷⁸). Perbaiki + imbangi di `praktikum.tex`.
  **Selesai:** Sub-bab *Kriptanalisis GOST dan Batas Rekeying*
  (`subsec:kriptanalisis-gost`) + `tab:kompleksitas-serangan-gost` + batas rekeying
  2³² blok + kotak `\important`; `praktikum.tex` butir 2 diganti, butir baru 9.5
  ditambahkan; `rangkuman.tex` butir keunggulan GOST dipersempit dan dua butir
  koreksi ditambahkan.
- [~] **Environment `equation`/`align` ber-nomor** mulai dipakai sejak Bab 03
  (`eq:pembagian`, `eq:mod-tambah`, `eq:mod-kali`, `eq:invers`, `eq:euler`,
  `eq:entropi`); Bab 04 menambah 8 persamaan bernomor (`eq:caesar`,
  `eq:indeks-kebetulan`, `eq:hill`, `eq:affine-enkripsi`, `eq:affine-dekripsi`,
  `eq:affine-simultan-1/2`, `eq:otp-enkripsi`, `eq:otp-dekripsi`, `eq:two-time-pad`,
  `eq:perfect-secrecy`); Bab 05 menambah 7 (`eq:xor-enkripsi`, `eq:xor-dekripsi`,
  `eq:stream-enkripsi`, `eq:stream-dekripsi`, `eq:a51-luaran`, `eq:trivium-luaran`,
  `eq:salsa-final`); Bab 06 menambah 17 (`eq:blok-plainteks`, `eq:blok-cipherteks`,
  `eq:block-encrypt-decrypt`, `eq:mainan-enkripsi`, `eq:mainan-dekripsi`, `eq:ecb`,
  `eq:cbc-enkripsi`, `eq:cbc-dekripsi`, `eq:cfb-enkripsi`, `eq:cfb-dekripsi`, `eq:ofb`,
  `eq:ctr-enkripsi`, `eq:iterated-cipher`, `eq:whitening`, `eq:feistel-enkripsi`,
  `eq:feistel-dekripsi`, `eq:feistel-reversible`); Bab 07 menambah 8
  (`eq:des-putaran`, `eq:des-f`, `eq:des-subkunci`, `eq:des-ruang-kunci`,
  `eq:des-double`, `eq:des-mitm`, `eq:des-3des-ede`, `eq:des-3des-kompatibel`);
  Bab 08 menambah 19 (`eq:aes-state`, `eq:aes-subbytes`, `eq:aes-shiftrows`,
  `eq:aes-mixcolumns`, `eq:aes-mixcolumns-komponen`, `eq:aes-mixcolumns-polinom`,
  `eq:aes-addroundkey`, `eq:aes-invsubbytes`, `eq:aes-inv-shiftrows`,
  `eq:aes-inv-mixcolumns`, `eq:aes-inv-mixcolumns-komponen`, `eq:aes-enkripsi`,
  `eq:aes-dekripsi-putaran`, `eq:aes-dekripsi`, `eq:aes-equiv-kunci`,
  `eq:aes-polinom-pereduksi`, `eq:aes-invers-pangkat`, `eq:aes-sbox-affine`,
  `eq:aes-sbox-rumus`); Bab 09 menambah 7 (`eq:jadwal-kunci-rc5`, `eq:pw-qw`,
  `eq:rc5-enkripsi`, `eq:gost-putaran`, `eq:gost-jadwal-kunci`, `eq:gost-cbc`,
  `eq:batas-rekeying`); Bab 10 menambah 15 (`eq:totient-prima`, `eq:totient-rsa`,
  `eq:ed-kongruen`, `eq:ed-kelipatan`, `eq:rsa-pangkat`, `eq:rsa-bukti`,
  `eq:rsa-rumus`, `eq:bezout`, `eq:serang-d`, `eq:gnfs`, `eq:syarat-blok`,
  `eq:enkripsi-blok`, `eq:panjang-blok`, `eq:dekripsi-blok`, `eq:kerapuhan-rsa`);
  Bab 11 menambah 5 (`eq:dh-bukti`, `eq:dlp`, `eq:dlp-index-calculus`,
  `eq:mitm-k1`, `eq:mitm-k2`).
  Lanjutkan untuk ElGamal, ECDLP, hash.
- [ ] **`contoh.tex` tidak konsisten** — bab 13–16 nol `\begin{example}`.
- [ ] **Bab 15 dan 16 tanpa gambar raster.** (Bab 03 dan 04 sudah punya.)
  Skrip pembuat gambar raster: `scripts/refactor/figures/entropi_ternate.py`.
- [ ] **Bab tanpa sitasi: 14.** (02, 03, 04, 05, 06, dan 07 sudah selesai; Bab 06
  kini menyitasi `shannon1949`, `stallings2017`, dan `menezes1996`, sedangkan
  Bab 07 menyitasi `fips46`, `biham1991`, `matsui1994`, `eff1998`,
  `stallings2017`, dan `menezes1996`.)

## Catatan lintas bab: tabel lebar & panjang baris

Bab 04 sempat menghasilkan 6 cacat tipografis (`Overfull`/`Underfull`) yang sudah
diperbaiki; polanya akan terulang di bab-bab berikut, jadi perhatikan sejak awal:

- **Rangkaian huruf panjang di dalam paragraf** (cipherteks tanpa spasi, nilai heksadesimal
  panjang) tidak bisa dipotong TeX → taruh di `center` tersendiri, bukan inline.
- **Bilangan panjang di dalam matematika inline** ($25! = 15.511.\ldots$) → jadikan
  tampilan `\[ ... \]`.
- **`tabularx` tanpa kolom `X`** → pakai `tabular` biasa (tab:affine-enkripsi sempat
  `Underfull ... in alignment` karena ini).
- **Kolom `X` harus diberi `>{\raggedright\arraybackslash}`**; `X` yang rata kanan-kiri
  mudah `Underfull` (`badness 10000`).
- **Tabel 8 kolom dengan `@{\hspace{16pt}}`** bisa melebihi `\linewidth` → turunkan
  jarak antar kelompok kolom.
- **Blok `quote` berisi satu string `\texttt` panjang** → tambahkan `\raggedright`
  agar baris terakhir tidak dipaksa rata kanan.
- **Baris kepala tabel sempit** (`tabular` dengan kolom `l`/`c` saja) dapat melebihi
  `\linewidth` walau isinya pendek, karena TeX tidak bisa memenggal sel. Bab 05 sempat
  `Overfull 4,75pt` pada `tab:trivium-tap` → perpendek judul kolomnya ("Masukan gerbang
  AND" → "Masukan AND"). Bab 06 mengulang pola yang sama pada `tab:perbandingan-mode`
  (kepala kolom "Ketergantungan") → lebarkan `p{2.9cm}` menjadi `p{3.1cm}` dan rampingkan
  kolom tetangganya. **Periksa kepala kolom `p{}` sejak awal**, jangan hanya isinya.
- **Persamaan tampilan panjang yang memuat banyak tanda `\oplus`** mudah melewati
  `\linewidth` (Bab 06 `contoh.tex`: 50,8pt pada contoh pengulangan counter, dan 0,1pt pada
  contoh Feistel) → pecah ke dua `\[ ... \]` atau ganti `\qquad` menjadi `\quad`.
- **Tanda pisah `---` diikuti kata panjang pada akhir baris** memindahkan titik potong ke
  tempat yang salah dan menghasilkan `Overfull` beberapa pt (Bab 05, paragraf penutup
  section-03) → ganti dengan titik dua atau ubah susunan kalimatnya.
- **Rangkaian `\texttt` berisi biner/heksadesimal di dalam `array`** aman selama tiap baris
  di bawah ~68 karakter; bila lebih, pecah menjadi dua tampilan atau pindahkan ke `tabular`.
- **Baris komentar `# -----…-----` (banner) di dalam berkas Python yang di-`lstinputlisting`
  TIDAK dapat dipotong.** `breaklines=true` hanya memenggal pada spasi, sedangkan banner
  sama sekali tidak mengandung spasi, sehingga baris itu meluber utuh. Bab 10 mengalaminya:
  banner 77 karakter → `Overfull 51,49pt`; dipendekkan ke 72 → masih `19,99pt`; baru 68
  karakter yang muat. **Ukuran yang benar-benar muat adalah <= 68 karakter** (dari
  pengukuran: ~6,3pt per karakter terhadap `\linewidth` 442,8pt). Berkas
  `rc5_gost_uji.py` dan `aes_uji.py` memakai banner 72 karakter dan kebetulan tidak
  bermasalah karena baris banner itu tidak pernah masuk ke rentang `firstline`/`lastline`
  listing mana pun — jadi 72 **tidak** boleh dianggap aman. **Aturan: berkas
  `code/python/*.py` baru dibuat dengan banner 68 karakter**, dan begitulah
  `rsa_uji.py` disetel; berkas lama yang bannernya tidak pernah masuk rentang listing
  dibiarkan apa adanya (72) agar commit per bab tetap bersih. Kesalahan ini juga sulit
  dilacak karena LaTeX melaporkan nomor baris berkas induk (`praktikum.tex`), bukan
  nomor baris berkas listing; cara isolasinya adalah mempersempit
  `firstline`/`lastline` berulang kali.
- **Isi kotak OBE (`obeassessment`, `obeactivity`, dll.) lebih sempit daripada `\linewidth`**
  karena padding tcolorbox. Rangkaian `\code{...}` 32 byte yang aman di badan teks justru
  menghasilkan `Overfull` **dan** `Underfull badness 10000` di dalam kotak (Bab 08
  `evaluasi.tex`). Solusi: taruh rangkaian itu pada tampilan `\[ ... \]` tersendiri, atau
  pecah menjadi beberapa `\code{}` pendek dalam satu baris. Ingat juga bahwa **satu kotak
  OBE yang tidak ditutup** (`\end{obeassessment}` hilang) menyeret seluruh berkas
  berikutnya ke dalam kotak itu dan memunculkan galat
  `\begin{tcb@savebox} ... ended by \end{document}` — periksa pasangan
  `\begin`/`\end` tiap kotak sebelum menyalahkan tipografi.
- **Label persamaan bersifat global** — sebelum menambah `eq:...` baru, periksa dulu
  dengan `grep -rho "label{eq:nama}" chapters/ | wc -l` agar tidak menimpa label bab lain.
- **Judul `\subsection` yang memuat matematika** ($f$, $S_1$, dst.) memicu
  `Package hyperref Warning: Token not allowed in a PDF string` karena teks itu masuk ke
  penanda PDF. Bunyi peringatan persisnya "removing `math shift'" (Bab 07,
  `\subsection{Struktur Putaran dan Fungsi $f$}`) → bungkus dengan
  `\texorpdfstring{$f$}{f}`.
- **`\code{...}` (yaitu `\texttt`) di dalam `\textbf{...}` di dalam environment
  `example`** meminta bentuk huruf `T1/lmtt/bx/it` yang tidak ada, karena badan
  `example` dimiringkan otomatis oleh `\newtheorem` gaya *plain* (Bab 07,
  `\textbf{Mengapa \code{0101010101010101} kunci lemah}`) → keluarkan `\code` dari
  `\textbf`, atau tulis angkanya sebagai teks biasa.
- **Dua tabel berdampingan dengan `\hspace{...}`** mudah melebihi `\linewidth` bila tiap
  tabel punya banyak kolom (Bab 07, tabel IP/IP⁻¹ 8 kolom dan tabel PC-1/PC-2) →
  tambahkan `\setlength{\tabcolsep}{4pt}` per tabel.
- **Menghitung jumlah kolom pada preamble `*{n}{c}`** — tabel jadwal pergeseran Bab 07
  memuat satu kolom label ditambah 16 kolom nilai, sehingga preamble harus
  `@{}l*{16}{c}@{}`, bukan `@{}*{16}{c}@{}`; kekeliruan ini memicu
  `! Extra alignment tab has been changed to \cr`.
- **Tampilan biner/heksadesimal panjang di mode matematika** (`\[ ... \]` berisi 64 bit
  atau empat nilai heksadesimal 16 digit) melewati `\linewidth` meski terlihat pendek →
  taruh dalam `center` dengan `\texttt` (baris tidak dirata-kan sehingga tidak
  `Underfull`), atau pecah dua baris dengan `aligned`.
- **Paragraf yang memuat beberapa nilai heksadesimal 16 digit berurutan** sulit dipatahkan
  TeX dan menghasilkan `Underfull` (Bab 07, butir rangkuman kunci lemah) → pindahkan
  nilai-nilainya ke `center` tersendiri.
- **Node TikZ tanpa `text width` tidak pernah membungkus teks.** Keterangan gambar yang
  ditulis berbaris-baris di dalam sumber `figures/*.tex` tetap keluar sebagai **satu baris
  raksasa**, karena TikZ mengabaikan perpindahan baris di dalam node. Bab 09 sempat
  menghasilkan enam `Overfull` sampai **293pt** (≈10cm) dari lima diagram baru; penyebabnya
  bukan koordinat, melainkan dua node keterangan tanpa `text width`. Solusi: beri setiap
  node keterangan gaya `catatan/.style={font=\footnotesize, align=left, text width=...}`
  lalu pilih lebarnya agar ujungnya masih di dalam rentang node gambar. Ukur juga lebar
  kata terpanjang di dalam kotak: Bab 09 sempat `Overfull 8,5pt` karena kata
  "transformasi" (≈54pt) tidak muat di `text width=1.75cm`; menaikkannya ke `2.2cm`
  cukup, dan kotak di sekitarnya perlu dijarakkan ulang agar panah tetap punya ruang.
  **Cara memastikan siapa pelakunya:** `Overfull` pada log muncul *sebelum* penanda
  `(figures/nama.tex`, jadi pasangkan dengan penanda berkas terakhir sebelum baris itu.
