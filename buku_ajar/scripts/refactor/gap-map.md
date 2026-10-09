# Peta Celah: Referensi → Buku Ajar

Berkas kerja untuk Tahap 0–16 rencana `dynamic-brewing-stream.md`.
Keadaan awal: buku 178 halaman, 0 error, 0 warning. Tiap bab 1.100–2.200 kata.
Sasaran: ±4.000–6.000 kata/bab (prosa naratif), tabel, contoh terhitung, gambar.

Legenda status: `[ ]` belum · `[~]` sedang dikerjakan · `[x]` selesai.

**Kemajuan:** Tahap 1–14 (Bab 01–14) selesai. Buku **494 halaman**, gerbang
kebersihan `output/main_build.log` = 0 pada ketujuh pola. Berikutnya: Tahap 15
(Bab 15 — Fungsi Hash dan MAC).

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

## Bab 12 — Algoritma ElGamal  `[x]` SELESAI
Sumber: `referensi/14-*` (2.160 kata, 5 topik, 3 gambar di `images/llm/`).
Target: ±4.000 kata.
**Menyitasi 5 entri baru** (`defeo2021elgamal`, `rfc4880`, `rfc9580`,
`fips1865`, `fail0verflow2010`) dan **memperkaya satu entri lama**
(`elgamal1985` kini lengkap: volume 31, nomor 4, halaman 469–472, DOI
10.1109/TIT.1985.1057074). `references.bib` 54 → **59 entri**.

Hasil: **8.223 kata** pada sembilan berkas (empat section 4.866, contoh 1.555,
praktikum 671, latihan 431, rangkuman 420, evaluasi 280), **27 halaman
mandiri**, 4 tabel bernomor, 6 contoh terhitung, **10 persamaan bernomor**,
**19 subbagian baru (0 → 19)**, 1 diagram TikZ + 3 gambar raster (1 di antaranya
baru disalin dari referensi), dan satu program verifikasi baru
(`code/python/elgamal_uji.py`, 306 baris, sepuluh blok pengujian yang seluruhnya
**lulus**). Bab semula 1.148 kata, **tanpa satu pun subbagian bernama** (hanya
empat `\section`), tanpa persamaan bernomor, dan tanpa program pengujian.

- [x] **Contoh multi-blok "HALO" dengan dua kunci efemeral berbeda** — 
  Contoh~\ref{ex:elgamal-halo}: pengodean $A = 00$ (Tabel~\ref{tab:pengodean-halo}),
  $m = 07001114$ dipecah menjadi $m_{1} = 0700$ dan $m_{2} = 1114$, dienkripsi
  dengan $k = 1463$ dan $k = 2001$ menjadi $(1439, 74)$ dan $(1220, 1682)$,
  lalu dipulihkan kembali. Gap terbesar bab ini.
- [x] **Contoh akar primitif dan logaritma diskret** — Contoh~\ref{ex:elgamal-akar}
  membandingkan siklus $a = 3$ ($3, 2, 6, 4, 5, 1$) dengan $a = 2$
  ($2, 4, 1, \dots$) modulo 7 pada Tabel~\ref{tab:akar-primitif-7}, menghitung
  $7^{3} \equiv 15 \pmod{41}$, serta $\varphi(6) = 2$ dan $\varphi(40) = 16$
- [x] **Bukti identitas dekripsi $b/a^{x} \equiv m \pmod p$** —
  Subbagian~\ref{subsec:bukti-elgamal} dengan Persamaan~\eqref{eq:elgamal-bukti}
  (`split` di dalam `equation`), menunjukkan faktor $g^{xk}$ saling meniadakan.
  Bukti ini **sama sekali tidak ada di buku lama** maupun di ringkasan dek.
- [x] **Contoh lengkap kedua dengan $p = 2357$** — Contoh~\ref{ex:elgamal-2357}:
  $g = 2$, $x = 1751 \Rightarrow y = 1185$, $m = 2035$, $k = 1520 \Rightarrow
  (a, b) = (1430, 697)$, dekripsi dengan eksponen $605 = p - 1 - x$ memberi $872$
- [x] **Pembongkaran pesan karena $k$ dipakai ulang** — Contoh~\ref{ex:elgamal-k-ulang}
  dengan angka lengkap: $a_{1} = a_{2} = 1439$, $b_{1} = 74$, $b_{2} = 988$,
  $\frac{b_{1}}{b_{2}} \equiv 474 \equiv \frac{m_{1}}{m_{2}}$, pemulihan
  $m_{2} = m_{1} b_{2} b_{1}^{-1} \equiv 1114$, dan kebocoran
  $y^{k} = b_{1} m_{1}^{-1} \equiv 1825$. Derivasinya pada
  Persamaan~\eqref{eq:elgamal-k-ulang} dan~\eqref{eq:elgamal-k-ulang-m2}
- [x] **Empat tabel bernomor** — Tabel~\ref{tab:elgamal-vs-rsa} (ElGamal versus
  RSA, kini bergaya `booktabs` dengan tujuh baris, semula lima baris bergaris
  penuh), Tabel~\ref{tab:akar-primitif-7}, Tabel~\ref{tab:parameter-elgamal}
  (kerahasiaan $p, g, x, y, m, k, a, b$), dan Tabel~\ref{tab:pengodean-halo}
- [x] **Status kerahasiaan yang semula tidak pernah ditabulasikan** —
  Subbagian *Properti dan Kerahasiaan Parameter*: tabel menegaskan bahwa $k$
  **harus dirahasiakan sama ketatnya dengan $x$**, sesuatu yang hanya disinggung
  sekilas pada buku lama
- [x] **Sepuluh persamaan bernomor** — \eqref{eq:elgamal-kunci},
  \eqref{eq:elgamal-a}, \eqref{eq:elgamal-b}, \eqref{eq:elgamal-invers},
  \eqref{eq:elgamal-dekripsi}, \eqref{eq:elgamal-bukti},
  \eqref{eq:elgamal-homomorfik}, \eqref{eq:elgamal-k-ulang},
  \eqref{eq:elgamal-k-ulang-m2}, \eqref{eq:dlp-elgamal}. Semula **nol**.
- [x] **Analisis kelemahan secara berimbang** — Subbagian *Sifat Homomorfik
  Multiplikatif* (dengan catatan jujur bahwa hasil kalinya berlaku modulo $p$:
  $700 \times 1114 \bmod 2273 = 161$, bukan $779.800$), *Enkripsi Probabilistik*,
  *Bahaya Penggunaan Ulang Kunci Efemeral* (termasuk kisah Sony PS3 2010,
  `fail0verflow2010`), dan *Ekspansi Cipherteks*
- [x] **Sejarah dan penamaan** — Subbagian~\ref{subsec:sejarah-elgamal}: makalah
  IEEE Trans. Inf. Theory 31(4):469–472 (1985) dan versi awalnya di CRYPTO '84,
  riwayat Taher Elgamal (HP Labs → *Chief Scientist* Netscape → SSL → Securify
  1998 → RSA Conference Lifetime Achievement Award 2009 → Marconi Prize 2019),
  serta catatan ejaan ``Elgamal'' versus ``ElGamal''. Gambar raster baru
  Gambar~\ref{fig:penghargaan-elgamal} (`penghargaan-elgamal-2009.png`, disalin
  dari `referensi/14-*/images/llm/page_002_img_02.png`)
- [x] **Catatan penerapan OpenPGP** — Subbagian *Catatan Penerapan: ElGamal di
  Dunia Nyata*: ElGamal sebagai algoritma kunci publik nomor 16 dengan tanda
  ``(Encrypt-Only)'' pada RFC~4880, pelarangannya oleh RFC~9580 (2024), dan
  serangan De Feo--Poettering--Sorniotti (CCS 2021) berupa **ambiguitas
  parameter** — pemulihan kunci privat 2048 bit dalam ±2,5 jam pada satu inti,
  ±2.000 kunci rentan, CVE-2021-33560 (Libgcrypt) dan CVE-2021-40530 (Crypto++)
- [x] **Program verifikasi** `code/python/elgamal_uji.py` — 306 baris, ASCII + LF,
      empat banner komentar tepat 68 karakter. Memuat `prima`, `siklus_pangkat`,
      `orde`, `akar_primitif`, `phi`, `pbb`, `invers_fermat`,
      `bangkitkan_kunci`, `enkripsi`, `dekripsi`, `dari_kode`, `ke_kode`, lalu
      sepuluh blok `uji_*` yang **seluruhnya lulus** (baris terakhir:
      `Seluruh pengujian LULUS`). Empat blok disisipkan ke `praktikum.tex`
      sebagai Listing~\ref{lst:elgamal-parameter}, \ref{lst:elgamal-prosedur},
      \ref{lst:elgamal-blok}, dan \ref{lst:elgamal-serangan}
- [x] **Pertumbuhan komponen OBE** — `praktikum.tex` 1 → 5 `obeactivity`,
      `latihan.tex` 1 → 2 `obereflection` (3 → 13 butir), `rangkuman.tex`
      7 → 15 butir, `evaluasi.tex` 3 → 6 butir kuis dan
      **`competencychecklist` 5 → 12 baris**

### Koreksi terhadap sumber (wajib dicatat)

Dek `14-*` hampir bersih: **seluruh angkanya benar kecuali satu salah cetak
modulus.** Semua nilai telah diperiksa ulang dengan `code/python/elgamal_uji.py`
sebelum ditata huruf:

| Klaim dek | Verifikasi |
|---|---|
| $\operatorname{ord}(3, 2273) = 2272$ (akar primitif) | lulus (UJI 2) |
| $p = 2273$, $g = 3$, $x = 243 \Rightarrow y = 461$ | lulus (UJI 2) |
| $m = 700$, $k = 1463 \Rightarrow (a, b) = (1439, 74)$ | lulus (UJI 3) |
| $1439^{2029} \bmod 2273 = 1791$, lalu $74 \times 1791 = 700$ | lulus (UJI 3) |
| $3^{(p-1)/2} \bmod 2273$ untuk uji akar primitif | lulus (UJI 1) |
| $\operatorname{ord}(2, 2357) = 2356$ (akar primitif) | lulus (UJI 9) |
| $p = 2357$, $g = 2$, $x = 1751 \Rightarrow y = 1185$ | lulus (UJI 9) |
| $m = 2035$, $k = 1520 \Rightarrow (a, b) = (1430, 697)$ | lulus (UJI 9) |
| $1430^{605} \bmod 2357 = 872$, lalu $697 \times 872 = 2035$ | lulus (UJI 9) |

1. **Salah cetak modulus pada dek.** Dek menuliskan
   $2^{1751} \pmod{2353} = 1185$. Modulus yang benar adalah **2357**, sesuai $p$
   yang telah ditetapkan pada dek yang sama; dengan modulus $2353$ hasilnya
   justru $1008 \ne 1185$. Nilai $1185$ sendiri benar. Buku menuliskan nilai
   yang benar dan **mencatat kekeliruan itu secara terbuka** di
   Contoh~\ref{ex:elgamal-2357} supaya mahasiswa yang membandingkan dengan dek
   tidak mengira buku yang keliru.
2. **Kalimat DSA pada buku lama keliru.** `section-04.tex` semula menyatakan DSA
   ``dibakukan oleh NIST pada tahun 1991''. Yang benar: DSA **diusulkan** pada
   1991 dan **dibakukan sebagai FIPS 186 pada 1994**; lebih jauh, FIPS 186-5
   (2023) sudah **tidak lagi mengizinkan pembangkitan kunci DSA yang baru**.
   Sejak Bab 12 fakta ini muncul utuh di Subbagian~\ref{subsec:sejarah-elgamal}
   dan dirujuk ulang (bukan diulang) di `section-04.tex`.
3. **Bukti dekripsi absen total.** Baik buku lama maupun dek tidak pernah
   membuktikan mengapa $m = b \cdot (a^{x})^{-1} \bmod p$ mengembalikan
   plainteks semula; keduanya hanya menyatakan rumusnya. Bukti itu kini ada
   (`subsec:bukti-elgamal`).
4. **Kunci efemeral $k$ tidak pernah digolongkan sebagai rahasia.** Buku lama
   menyebut $k$ hanya sebagai ``bilangan acak''. Tabel~\ref{tab:parameter-elgamal}
   menegaskan statusnya, dan seluruh Subbagian~\ref{subsec:k-ulang} menjelaskan
   akibat kelalaiannya.

## Bab 13 — Algoritma Knapsack  `[x]` SELESAI
Sumber: `referensi/16-*` (2.499 kata, 7 topik, 3 gambar). Target: ±4.000 kata.
**Menyitasi 3 entri baru** (`merkle1978`, `lagarias1985subset`,
`coster1991subset`) dan **memperkaya satu entri lama** (`shamir1982` kini
lengkap: `@inproceedings`, halaman 145–152, DOI 10.1109/SFCS.1982.5, plus
catatan versi jurnal IEEE Trans. Inf. Theory 30(5):699–704, 1984).
`references.bib` 59 → **62 entri**.

Hasil: **7.774 kata** pada sembilan berkas (empat section 3.925, contoh 1.978,
praktikum 562, latihan 374, rangkuman 460, evaluasi 373), **25 halaman
mandiri**, 9 tabel bernomor, 6 contoh terhitung, **8 persamaan bernomor**,
**18 subbagian baru (0 → 18)**, 1 diagram TikZ + 3 gambar raster (1 di antaranya
baru disalin dari referensi), dan satu program verifikasi baru
(`code/python/knapsack_uji.py`, 347 baris, sepuluh blok pengujian yang
seluruhnya **lulus**). Bab semula 1.367 kata dan **tanpa satu pun subbagian
bernama**, tanpa persamaan bernomor, tanpa tabel apa pun di `contoh.tex`, dan
tanpa program pengujian.

- [x] **Contoh knapsack dasar non-superincreasing** — Contoh~\ref{ex:knapsack-dasar}:
  $W = \{1, 5, 6, 11, 14, 20\}$ dengan kriptogram $(32, 30, 0, 11)$ pada
  Tabel~\ref{tab:knapsack-dasar}, sekaligus menunjukkan bahwa $M = 32$
  sesungguhnya punya **tiga** solusi berbeda sehingga \textit{greedy} justru
  memilih yang salah
- [x] **Contoh \textit{greedy} superincreasing** — Contoh~\ref{ex:greedy-superincreasing}
  dan Tabel~\ref{tab:greedy-70}: barisan $\{2,3,6,13,27,52\}$ dengan $M = 70$
  menghasilkan \code{110101} langkah demi langkah
- [x] **Himpunan parameter Merkle--Hellman alternatif** —
  Contoh~\ref{ex:mh-kunci-105} (pembangkitan kunci: $m = 105$, $n = 31$,
  Tabel~\ref{tab:mh-kunci-105}) dan Contoh~\ref{ex:mh-105} (enkripsi dan
  dekripsi tiga blok: \code{011000110101101110} $\to (174, 280, 333) \to$
  pulih, Tabel~\ref{tab:mh-105-dekripsi})
- [x] **Contoh prosedur lengkap dari ujung ke ujung** — Contoh~\ref{ex:mh-lengkap}:
  $W_{priv} = \{1,2,4,9,18,36,72,144\}$, $m = 293$, $n = 37$, $n^{-1} = 198$,
  blok \code{10110010} dan \code{01101001} menjadi $252$ dan $356$
- [x] **\textbf{Bukti dekripsi yang semula absen total}** — baru, dan justru
  inilah kekuatan bab ini. Subbagian~\ref{subsec:bukti-knapsack} menurunkan
  Persamaan~\eqref{eq:mh-bukti} ($n^{-1} n \equiv 1$ menghapus faktor pengali)
  lalu **menaikkan kesamaan modulo menjadi kesamaan eksak** lewat
  $0 \le \sum_i b_i w_i \le \sum_i w_i < m$ pada
  Persamaan~\eqref{eq:mh-bukti-eksak}. Baik buku lama maupun dek tidak pernah
  menjelaskan mengapa syarat $m > \sum_i w_i$ menjamin \textit{greedy} menerima
  sisa yang benar
- [x] **Koreksi rumus enkripsi yang bertentangan dengan contohnya sendiri** —
  `section-03.tex` lama menulis $C = \sum_i b_i w'_i \pmod m$, padahal
  `contoh.tex` yang lama menghitung $C_2 = 74 + 148 + 80 + 54 = 356 > m = 105$.
  Rumus kini ditulis **tanpa** modulus (Persamaan~\eqref{eq:mh-enkripsi})
  disertai catatan bahwa pengurangan modulo $m$ di sisi pengirim bersifat
  opsional, sebab dekripsi hanya memakai $C \bmod m$
- [x] **\textbf{Analisis kerapatan yang sama sekali baru}** —
  Persamaan~\eqref{eq:densitas-knapsack} dan Tabel~\ref{tab:kerapatan-knapsack}:
  barisan contoh buku ini $d = 0{,}8992$ (di atas ambang, relatif aman),
  sedangkan parameter Merkle--Hellman praktis $d \approx 0{,}3344$ (jauh di
  bawah ambang). Ambang Lagarias--Odlyzko $d < 0{,}645$ dan perbaikan
  Coster--LaMacchia--Odlyzko--Schnorr menjadi $d < 0{,}9408$
- [x] **Parameter anjuran sumber dibongkar ketidakcocokannya** —
  Subbagian *Parameter yang Dianjurkan dan Kelemahannya*: sumber menganjurkan
  $\ge 250$ elemen bernilai 200–400 bit **dan** modulus hanya 100–200 bit;
  keduanya mustahil berdampingan. Diturunkan angka yang self-konsisten: 100
  elemen dimulai dari $2^{200}$ memberi jumlah $\approx 2^{300}$, sehingga $m$
  perlu **sekitar 300 bit atau lebih**
- [x] **Angka \textit{brute force} $10^{46}$ tahun dinilai ulang** —
  $2^{250}$ vektor pada $10^6$ percobaan/detik sesungguhnya memerlukan
  $5{,}7 \times 10^{61}$ tahun; angka $10^{46}$ tahun yang beredar sepadan
  dengan hanya $2^{198}$ percobaan, yaitu barisan $\pm 200$ elemen. Lebih
  penting lagi, angka itu **mengukur hal yang salah**
- [x] **Warisan ke kriptografi pascakuantum** — Subbagian *Pelajaran dan
  Warisan*: persoalan kisi yang dipakai Shamir dan tim Lagarias untuk
  meruntuhkan Merkle--Hellman kini menjadi landasan **ML-KEM pada FIPS~203**
  \citep{fips203}
- [x] **Verifikasi silang dengan perkakas daring** — Contoh~\ref{ex:demo-online}
  dan Tabel~\ref{tab:demo-online}: perkakas daring dengan
  $W_{priv} = \{3,5,15,25,54,110,225\}$, $m = 439$, $n = 10$, $n^{-1} = 44$,
  pesan \code{1001000110010111011001101111} $\to (280,236,431,708)$ $\to$
  \code{H}, \code{e}, \code{l}, \code{o}. Gambar raster baru
  Gambar~\ref{fig:demo-knapsack-online} (`demo-knapsack-online.png`, disalin
  dari `referensi/16-*/images/llm/page_022_img_01.png`)
- [x] **Delapan persamaan bernomor** — \eqref{eq:knapsack-dasar},
  \eqref{eq:superincreasing}, \eqref{eq:mh-kunci}, \eqref{eq:mh-enkripsi},
  \eqref{eq:mh-dekripsi}, \eqref{eq:mh-bukti}, \eqref{eq:mh-bukti-eksak},
  \eqref{eq:densitas-knapsack}. Semula **nol**.
- [x] **Lemma dan pembuktiannya** — Lemma~\ref{lem:greedy-superincreasing}
  (keunikan pilihan elemen terbesar) beserta bukti bahwa $B_n = 0$ berakibat
  $M \le \sum_{j<n} w_j < w_n$
- [x] **Program verifikasi** `code/python/knapsack_uji.py` — 347 baris, ASCII +
  LF, empat banner komentar tepat 68 karakter. Memuat `pbb`, `invers`,
  `prima`, `superincreasing`, `greedy`, `semua_solusi`, `bits_dari`,
  `ke_string`, `jumlah_bobot`, `urai`, `bangkitkan_kunci`, lalu sepuluh blok
  `uji_*` yang **seluruhnya lulus** (baris terakhir: `Seluruh pengujian
  LULUS`). Lima blok disisipkan ke `praktikum.tex` sebagai
  Listing~\ref{lst:knapsack-kunci}, \ref{lst:knapsack-greedy},
  \ref{lst:knapsack-enkripsi}, \ref{lst:knapsack-kerapatan}, dan
  \ref{lst:knapsack-balik}
- [x] **Pertumbuhan komponen OBE** — `praktikum.tex` 1 → 5 `obeactivity`
  (1 → 25 butir), `latihan.tex` 1 → 2 `obereflection` (3 → 14 butir),
  `rangkuman.tex` 7 → 17 butir, `evaluasi.tex` 3 → 8 butir kuis dan
  **`competencychecklist` 5 → 13 baris**

### Koreksi terhadap sumber (wajib dicatat)

Dek `16-*` mengandung **tiga salah cetak teks dan satu anjuran parameter yang
tidak konsisten dengan dirinya sendiri.** Semua angka telah diperiksa ulang
dengan `code/python/knapsack_uji.py` sebelum ditata huruf:

| Klaim dek | Verifikasi |
|---|---|
| $w = \{1,5,6,11,14,20\}$: blok $\to 32, 30, 0, 11$ | lulus (UJI 1) |
| $M = 70$ pada $\{2,3,6,13,27,52\}$ $\to$ \code{110101} | lulus (UJI 2) |
| $m = 105$, $n = 31$: $\text{PBB} = 1$ dan $31^{-1} = 61$ | lulus (UJI 3) |
| $w'_i = 31 w_i \bmod 105 \to \{62,93,81,88,102,37\}$ | lulus (UJI 3) |
| $174, 280, 333$; $174 \cdot 61 \equiv 9$, $280 \cdot 61 \equiv 70$, $333 \cdot 61 \equiv 48$ | lulus (UJI 4) |
| $m = 293$, $n = 37$: $37 \cdot 198 = 25 \cdot 293 + 1$ | lulus (UJI 5) |
| $C = 252, 356 \Rightarrow C' = 86, 168$ | lulus (UJI 5) |
| Perkakas daring: $m = 439$, $n = 10$, $n^{-1} = 44$ | lulus (UJI 10 / Contoh~\ref{ex:demo-online}) |
| Perkakas daring: $(280, 236, 431, 708) \to (28, 287, 87, 422)$ | lulus (Contoh~\ref{ex:demo-online}) |
| Shamir: $n \approx 100$, $a_i \approx 200$ bit | sesuai kutipan abstrak dek sendiri |

1. **Panjang plainteks tidak konsisten (dua kali).** Dek menuliskan plainteks
   Contoh 1 sebagai \code{1110010101100000000011000} (25 bit) padahal keempat
   bloknya jelas 24 bit, dan plainteks Contoh 4 sebagai
   \code{01100011010101101110} (20 bit) yang bahkan tidak habis dibagi enam
   padahal ketiga kriptogramnya sepadan dengan 18 bit. Buku memakai rangkaian
   yang benar dan **mencatat kekeliruan itu apa adanya** pada
   Contoh~\ref{ex:knapsack-dasar} dan Contoh~\ref{ex:mh-105}.
2. **Bit terakhir terbalik pada Contoh 2.** Dek menuliskan langkah terakhir
   sebagai ``$2 - 2 = 0 \Rightarrow b_1 = 0$''. Bila $b_1 = 0$ maka sisanya tetap
   $2$, bukan $0$. Nilai yang benar adalah $b_1 = 1$, sebagaimana ditegaskan
   oleh jawaban \code{110101} pada dek yang sama. Catatan itu ada di
   Contoh~\ref{ex:greedy-superincreasing}.
3. **Anjuran parameter bertentangan dengan dirinya sendiri.** Dek menuntut
   ``paling sedikit 250 elemen, nilai setiap elemen antara 200 sampai 400 bit''
   sekaligus ``nilai modulus antara 100 sampai 200 bit''. Karena $m$ wajib
   melampaui jumlah seluruh elemen barisan privat, dan 250 elemen bernilai
   200 bit ke atas sudah berjumlah lebih dari $2^{201}$, modulus sependek itu
   mustahil sah. Derivasi yang self-konsisten ($m$ sekitar 300 bit) ada di
   Subbagian *Parameter yang Dianjurkan dan Kelemahannya*.
4. **Estimasi \textit{brute force} $10^{46}$ tahun.** Angka itu tidak sepadan
   dengan 250 elemen yang dianjurkan (yang seharusnya $\pm 5{,}7 \times
   10^{61}$ tahun); ia hanya cocok untuk $\pm 200$ elemen. Di luar soal
   aritmetika, buku menegaskan bahwa ukuran semacam itu **bukan ukuran
   keamanan yang tepat**, sebab tidak ada penyerang yang menelusuri $2^n$
   kandidat.
5. **Serangan kerapatan rendah tidak disebut dek sama sekali.** Dek hanya
   memuat serangan Shamir. Buku menambahkan ambang kerapatan
   Lagarias--Odlyzko ($d < 0{,}645$) dan Coster--LaMacchia--Odlyzko--Schnorr
   ($d < 0{,}9408$) beserta perhitungan $d$ untuk kedua rejim parameter.
   **Koreksi atas asumsi awal saya sendiri:** ambang $0{,}9408$ **bukan** milik
   Lagarias--Odlyzko, melainkan milik Coster dan kawan-kawan (EUROCRYPT '91);
   ambang Lagarias--Odlyzko sendiri adalah $0{,}645$.

## Bab 14 — Kriptografi Kurva Eliptik (ECC)  `[x]` SELESAI
Sumber: `referensi/17-ECC-Bagian1-2026` (2.883 kata) + `18-ECC-Bagian2-2026`
(5.706 kata) — total 8.589 kata, 32 topik, 31 gambar; sumber terkaya di
kelompok asimetris. Target: ±5.500 kata. **Bab ini semula tanpa satu pun
sitasi** — kini menyitasi 9 kunci, dengan **6 entri baru** di `references.bib`
(`miller1986`, `koblitz1987`, `hankerson2004`, `washington2008`,
`bernstein2006curve25519`, `pollard1978`); `references.bib` 62 → **68 entri**.

Hasil: **15.727 kata** pada sembilan berkas (empat section 9.966, contoh 2.513,
praktikum 1.334, latihan 751, rangkuman 728, evaluasi 435) — semula 1.737 kata,
jadi **9,1 kali** — **47 halaman mandiri**, **12 tabel bernomor** (semula 1),
**7 gambar bernomor** (4 di antaranya raster baru disalin dari referensi),
**6 contoh terhitung** di dalam environment `example` (semula **nol**),
**20 persamaan bernomor** (semula **nol**), dan **24 subbagian** (10 → 24).
Bab semula 1.737 kata dengan 10 subbagian bernama, **nol** persamaan bernomor,
**nol** environment `example`, dan hanya satu tabel.

- [x] **Aritmetika medan berhingga $GF(p)$ dan $GF(2^m)$** — representasi
  polinom (Persamaan~\eqref{eq:gf2m-polinom}, \eqref{eq:gf2m-tambah}),
  penjumlahan = XOR (Gambar~\ref{fig:tabel-gf11}),
  perkalian `'57'·'83'` mod $x^8+x^4+x^3+x+1$ → `'C1'` dengan pembagian
  panjang (Gambar~\ref{fig:pembagian-polinom}, Tabel~\ref{tab:gf2m-kali}),
  dan Contoh~\ref{ex:gf2m} (`0D`+`06` = `0B`, `57`+`83` = `D4`)
- [x] **Kedalaman aljabar abstrak** — aksioma grup, $\langle\Z_n,\oplus\rangle$
  vs $\langle\Z_p^*,\otimes\rangle$ (Tabel~\ref{tab:contoh-grup}), medan
  berhingga $F_{23}$ ($12+20=9$, $8 \cdot 9 = 3$) dan $GF(11)$
  (Tabel~\ref{tab:contoh-medan}), penyelesaian $x^2 \equiv 5 \pmod{11}$
  (Persamaan~\eqref{eq:akar-gf11}), serta penjelasan mengapa $\Z$ **bukan**
  medan
- [x] **Geometri kurva + penurunan analitik** — bentuk Weierstrass dan syarat
  ketak-singularan (Persamaan~\eqref{eq:weierstrass}, \eqref{eq:diskriminan}),
  galeri lima kurva (Gambar~\ref{fig:galeri-kurva}), titik di ketakhinggaan
  (Persamaan~\eqref{eq:titik-o}), penjumlahan geometris
  (Gambar~\ref{fig:penjumlahan-titik}), penurunan $P+Q$ dari hubungan Vieta
  (Persamaan~\eqref{eq:koordinat-pq}), penggandaan titik
  (Persamaan~\eqref{eq:koordinat-penggandaan}, Gambar~\ref{fig:penggandaan-titik}),
  kasus khusus $y_p = 0$, pelelaran dan \textit{double-and-add} pada $23P$,
  lalu pemeriksaan kelima aksioma grup (Tabel~\ref{tab:aksioma-grup-eliptik})
- [x] **Enumerasi penuh EC atas $GF(11)$** — Tabel~\ref{tab:enumerasi-gf11}
  (12 titik + $\mathcal{O}$, orde 13), Gambar~\ref{fig:sebaran-titik-gf11},
  dan Tabel~\ref{tab:pelelaran-gf11} (tiga belas kelipatan $P$); Contoh~\ref{ex:gf11}
  menghitung $P(2,4)+Q(5,9) = (8,8)$ sekaligus menemukan $2P = (5,9) = Q$
- [x] **ECDLP dan biaya penyerangan** — Subbagian~\ref{subsec:ecdlp}
  dengan Persamaan~\eqref{eq:ecdlp}, mengapa \textit{index calculus} tidak
  dapat dipindahkan ke kurva, serangan transfer, dan
  Tabel~\ref{tab:ecdlp-vs-faktorisasi} ($2^{40}$ / $2^{64}$ / $2^{128}$ langkah
  vs kunci RSA 1024 / 3072 / 15360 bit)
- [x] **ECDH lengkap** — Persamaan~\eqref{eq:ecdh-kunci},
  Tabel~\ref{tab:ecdh-gf5} dan Contoh~\ref{ex:ecdh}: variasi mod 5
  ($a=2$, $b=3$ → $K=(0,4)$) dan mod 23 ($a=2$, $b=3$ → $K=(12,4)$)
- [x] **ECEG (EC-ElGamal) lengkap + tabel perbandingan** —
  Persamaan~\eqref{eq:eceg-cipher} dan Persamaan~\eqref{eq:eceg-dekripsi},
  Contoh~\ref{ex:eceg} (mod 23, $b=3$, $k=5$: $C_1 = 5B = (9,16)$,
  $C_2 = (18,3)$, dekripsi memulihkan $P_M = (7,12)$), ditutup argumen
  enkripsi probabilistik; Tabel~\ref{tab:elgamal-vs-eceg}
  (`tab:ecc-vs-rsa` untuk sisi efisiensinya)
- [x] **Metode Koblitz \textit{encoding} pesan → titik** —
  Subbagian~\ref{subsec:koblitz}, Persamaan~\eqref{eq:koblitz-x} dan
  Persamaan~\eqref{eq:koblitz-dekode}, Tabel~\ref{tab:koblitz-b}, dan
  Contoh~\ref{ex:koblitz}: karakter \texttt{B} ($m = 11$, $k = 20$) menjadi
  $(224, 248)$ pada $y^2 \equiv x^3 - x + 188 \pmod{751}$ dengan $N = 727$
  dalam empat percobaan, lalu dekode $\lfloor 223/20 \rfloor = 11$
- [x] **Pemetaan langsung vs metode Koblitz** —
  Subbagian~\ref{subsec:pemetaan-langsung}: pemetaan tetap mengulang kelemahan
  buku kode (dua plainteks sama → titik $P_M$ sama), dan syarat $N \ge 36k$
  agar ruang $x$ tiap karakter tidak tumpang tindih
- [x] **Efisiensi dan kurva baku** — Tabel~\ref{tab:kurva-standar} (secp256k1,
  NIST P-256, Curve25519, NIST P-384) beserta alasan Curve25519 dirancang
  untuk \emph{menghilangkan} pilihan parameter, lalu rasionalisasi mengapa
  ECDLP lebih sukar daripada faktorisasi (serangan transfer vs rho Pollard,
  Tabel~\ref{tab:ecdlp-vs-faktorisasi})
- [x] **Pertumbuhan komponen OBE** — `praktikum.tex` 1 → 7 `obeactivity`
  (4 → 35 butir bernomor; Listing~\ref{lst:ecc-invers}, \ref{lst:ecc-gf2m},
  \ref{lst:ecc-kurva}, \ref{lst:ecc-real}, \ref{lst:ecc-koblitz},
  \ref{lst:ecc-bsgs}, \ref{lst:ecc-protokol}), `latihan.tex` 1 → 3
  `obereflection` (3 → 27 butir: Latihan 14.1 medan & struktur aljabar,
  14.2 geometri & aritmetika titik, 14.3 protokol/pemetaan/efisiensi),
  `rangkuman.tex` 7 → 22 butir, `evaluasi.tex` 3 → 10 butir kuis dan
  **`competencychecklist` 5 → 15 baris**
- [x] **Program verifikasi** `code/python/ecc_uji.py` — 494 baris, ASCII + LF,
  enam banner komentar tepat 68 karakter. Memuat `pbb`, `invers`,
  `akar_kuadrat`, `polinom_tambah/kali/bagi`, `tak_tereduksi`, `pada_kurva`,
  `lawan`, `tambah`, `gandakan`, `kali`, `enumerasi`, `orde`, `bsgs`,
  `tambah_real`, `gandakan_real`, `koblitz_kode`, `koblitz_dekode`, lalu
  **sebelas blok `uji_*`** (`uji_gf2m`, `uji_polinom`, `uji_medan`,
  `uji_geometri_real`, `uji_enumerasi`, `uji_penjumlahan`, `uji_ecdh`,
  `uji_eceg`, `uji_koblitz`, `uji_penyerangan`, `uji_latihan`) yang
  **seluruhnya lulus** (baris terakhir: `Hasil: 11 dari 11 blok pengujian
  LULUS`)
- [x] **Contoh terhitung baru** — enam `example`: Contoh~\ref{ex:gf2m}
  (aritmetika $GF(2^8)$ dan $GF(2^4)$), Contoh~\ref{ex:gf11} (kurva mod 11),
  Contoh~\ref{ex:real} (dua kurva riil), Contoh~\ref{ex:ecdh} (dua variasi
  ECDH), Contoh~\ref{ex:eceg} (ECEG + dekripsi), Contoh~\ref{ex:koblitz}
  (Koblitz mod 751); semuanya diverifikasi dengan `ecc_uji.py` sebelum
  ditata huruf

### Koreksi terhadap sumber (wajib dicatat)

Dek `17-*` dan `18-*` mengandung **lima kekeliruan** — satu salah kaprah
struktur aljabar, dua salah faktorisasi polinom, satu daftar titik yang tidak
lengkap sehingga orderya salah, dan satu salah penulisan bit. Semua angka pada
bab ini sudah diperiksa ulang dengan `code/python/ecc_uji.py`:

| Klaim dek | Verifikasi |
|---|---|
| Penjumlahan $GF(2^8)$: `0D`+`06` = `0B`, `57`+`83` = `D4` | lulus (`uji_gf2m`) |
| Perkalian `57`·`83` = `C1` mod $x^8+x^4+x^3+x+1$ | lulus (`uji_gf2m`) |
| $F_{23}$: $12 + 20 = 9$, $8 \cdot 9 = 3$ | lulus (`uji_medan`) |
| $x^2 \equiv 5 \pmod{11} \Rightarrow x = 4$ atau $7$ | lulus (`uji_medan`) |
| Kurva $y^2 \equiv x^3+x+6 \pmod{11}$: 12 titik + $\mathcal{O}$, orde 13 | lulus (`uji_enumerasi`) |
| $P(2,4) + Q(5,9) = (8,8)$ dan $2P = (5,9)$, sehingga $Q = 2P$ | lulus (`uji_penjumlahan`) |
| Koblitz mod 751: `B` → $(224, 248)$ dalam 4 percobaan | lulus (`uji_koblitz`) |
| ECEG mod 23, $k = 5$: $C_1 = (9,16)$, $C_2 = (18,3) \to P_M = (7,12)$ | lulus (`uji_eceg`) |
| Kurva mod 23: 27 titik berhingga, **orde grup 28**; $(3,10)$ pembangkit | lulus (`uji_enumerasi`) |
| $(4,0)$ berorde 2, $(13,16)$ berorde 7, $(0,1)$ berorde 28 | lulus (`uji_enumerasi`) |
| Dek: "mod 23 punya 26 titik, orde 26" | **salah** — 27 titik berhingga; dengan $\mathcal{O}$ ordenya **28** |
| Dek: "$x^2+1$ tereduksi di $GF(2)$" | **salah** — $(x+1)^2 = x^2+1$, jadi ia dapat direduksi |
| Dek: $x^5+x^2+x+1 = (x^3+x^2+1)(x^2+1)$ | **salah** — hasil kali itu $x^5+x^4+x^3+1$; yang benar $(x^2+1)(x^3+x+1)$ |
| Dek: $\langle \Z, +, \cdot \rangle$ adalah medan | **salah** — $\Z$ bukan medan ($2$ tidak punya invers di $\Z$) |
| Dek: hasil kali $GF(2^4)$ ditulis `10110` | **salah** — seharusnya `101110` (derajat $x^5$) |

Catatan tambahan: dek juga menuliskan "`0101010111` di dalam $GF(2^8)$",
padahal `57` heksadesimal adalah `01010111` — dua bit depan itu berlebih dan
tidak tertampung $m = 8$. Kelima kekeliruan itu **disebutkan apa adanya** di
dalam bab (Contoh~\ref{ex:gf2m}, Contoh~\ref{ex:gf11}, dan catatan koreksi pada
Subbagian~\ref{subsec:enumerasi-gf-p}) supaya pembaca yang membandingkan dengan
berkas sumber tidak mengira buku ini yang salah hitung.

## Bab 15 — Fungsi Hash dan MAC (tanpa sumber referensi)  `[x]` SELESAI
Sumber: `menezes1996` (HAC Bab 9), `stallings2017`, `katz2020`, FIPS 180-4, FIPS 202,
SP 800-107, SP 800-38B, RFC 4231, RFC 4493. Target: ±5.000 kata. Bab ini tidak
punya berkas di `referensi/`, sehingga seluruh materi disusun dari sumber
silabus tersebut. **22 entri baru** di `references.bib` (`merkle1989`,
`damgard1989`, `rivest1992md5`, `kelsey2005second`, `wang2004md5`, `wang2005sha1`,
`stevens2009rogue`, `stevens2017shattered`, `leurent2020sha1`, `bertoni2011keccak`,
`fips1804`, `fips202`, `bellare1996hmac`, `fips1981`, `rfc2104`, `rfc3174`,
`rfc4231`, `rfc4493`, `sp800107`, `sp80038b`, `sp80038d`,
`bernstein2005poly1305`); `references.bib` 68 → **90 entri**.

Hasil: **11.990 kata** pada sembilan berkas (tiga section 8.385, contoh 1.602,
praktikum 678, latihan 412, rangkuman 383, evaluasi 352) — semula 1.830 kata, jadi
**6,6 kali** — **39 halaman mandiri**, **16 persamaan bernomor** (semula **nol**),
**8 tabel bernomor** (semula **nol**), **5 gambar bernomor** (semula 2 diagram
TikZ: `alur-fungsi-hash`, `skema-hmac`; kini ditambah `batas-birthday`,
`konstruksi-sponge`, dan satu gambar raster `longsoran-sha256`), **7 contoh
terhitung** di dalam environment `example` (semula **nol**), **21 subbagian**
(14 → 21), dan **38 sitasi** (semula 10).

- [x] **Mekanisme internal kompresi + gambar alur** — Subbagian
  `subsec:anatomi-sha256`: jadwal pesan (Persamaan~\eqref{eq:sha256-jadwal}),
  enam fungsi pembantu $\mathrm{Ch}$, $\mathrm{Maj}$, $\Sigma_0$, $\Sigma_1$
  (Persamaan~\eqref{eq:sha256-fungsi}), pembaruan register
  (Persamaan~\eqref{eq:sha256-kompresi}), jejak kompresi pesan `abc` pada enam
  putaran terpilih (Tabel~\ref{tab:trace-sha256}), plus anatomi MD5
  (Persamaan~\eqref{eq:md5-putaran}) dan konstruksi Merkle--Damgård
  (Persamaan~\eqref{eq:md-iterasi})
- [x] **Vektor uji nyata menggantikan hash mainan** — vektor HMAC-SHA-256
  RFC 4231 TC1--TC4 dan TC6 (Tabel~\ref{tab:hmac-vektor}), jejak kompresi SHA-256
  satu blok 512 bit (`ba7816bf…f20015ad`), dan serangan panjang-ekstensi
  sungguhan pada `H(K‖m)` dengan $K = \texttt{"kunci"}$
  (Contoh~\ref{ex:length-extension}); seluruh angka dicocokkan dengan
  `hashlib`/`hmac` di `code/python/hash_uji.py`
- [x] **Serangan tabrakan nyata** — Subbagian `subsec:kriptanalisis-hash`:
  Wang 2004 (MD5) \citep{wang2004md5}, Wang 2005 (SHA-1) \citep{wang2005sha1},
  *chosen-prefix* Stevens 2009 \citep{stevens2009rogue}, **SHAttered** 2017
  $\approx 2^{63{,}1}$ operasi kompresi \citep{stevens2017shattered}, dan
  serangan pilih-awalan SHA-1 berbiaya $2^{63{,}4}$ oleh Leurent--Peyrin 2020
  \citep{leurent2020sha1}
- [x] **SHA-3/Keccak** — Subbagian `subsec:konstruksi-hash` dan diagram
  `figures/konstruksi-sponge`: pemisahan *rate* dan kapasitas, Keccak-f[1600]
  24 putaran, padding, dan alasan mengapa konstruksi sponge tahan terhadap
  serangan panjang-ekstensi serta tidak bergantung pada ketahanan kolisi sebuah
  fungsi kompresi \citep{bertoni2011keccak,fips202}
- [x] **Batas ulang tahun + perbandingan parameter** — penurunan
  Persamaan~\eqref{eq:birthday-peluang} sampai \eqref{eq:birthday-50}, diagram
  skala relatif `figures/batas-birthday`, dan Tabel~\ref{tab:parameter-hash}
  (MD5, SHA-1, SHA-224/256, SHA-384/512, SHA-3) beserta status keamanannya
- [x] **Banyak MAC, bukan hanya HMAC** — Subbagian `subsec:hmac` (HMAC,
  Persamaan~\eqref{eq:hmac-panjang-kunci} dan \eqref{eq:hmac-rumus}, diagram
  `figures/skema-hmac`), CBC-MAC (Persamaan~\eqref{eq:cbc-mac}) beserta serangan
  sambungannya, CMAC (Persamaan~\eqref{eq:cmac-subkunci}), Poly1305
  (Persamaan~\eqref{eq:poly1305}), dan GMAC — dihimpun pada
  Tabel~\ref{tab:perbandingan-mac}
- [x] **AEAD dan syarat keunikan nonce** — Subbagian `subsec:aead`: GCM, CCM,
  dan ChaCha20-Poly1305 beserta keunggulan/kelemahan masing-masing
  (Tabel~\ref{tab:aead}), dan akibat pengulangan nonce pada GCM
  \citep{sp80038d,rfc8439}
- [x] **Notasi formal PRF/PRP dan EUF-CMA** — permainan EUF-CMA pada
  Subbagian `sec:mac` dengan peluang menang $\approx 2^{-t}$
  \citep{katz2020}, penegasan bahwa keamanan HMAC bersandar pada sifat PRF dan
  **bukan** pada ketahanan kolisi, serta tiga bentuk naif $H(K\|m)$,
  $H(m\|K)$, dan $H(K\|m\|K)$ beserta alasan kegagalan masing-masing
- [x] **Perbandingan tag waktu-konstan** — Subbagian `subsec:tag-waktu-konstan`:
  perbandingan naif yang berhenti pada byte pertama berbeda menurunkan biaya
  pemalsuan dari $2^{t}$ menjadi sekitar $t \cdot 256$, dibandingkan dengan
  bentuk waktu-konstan, ditutup sitasi SP 800-107 \citep{sp800107}
- [x] **Gambar raster pertama untuk bab ini** — `longsoran-sha256.png`
  (Gambar~\ref{fig:longsoran-sha256}): digest 256 bit dua pesan yang berbeda
  satu huruf kecil-besar ditampilkan sebagai dua petak $16 \times 16$, ditambah
  petak ketiga yang menyorot $115$ bit yang berubah. Dibangkitkan oleh
  `scripts/refactor/figures/avalanche_hash.py` dengan pustaka standar saja
  (`hashlib` + `zlib`) karena matplotlib tidak tersedia di lingkungan ini;
  dilengkapi pembahasan uji longsoran (harapan $128$ bit, simpangan baku $8$,
  nilai $115$ berada $1{,}6$ simpangan baku dari harapan)
- [x] **Program verifikasi** `code/python/hash_uji.py` (10.017 byte, ASCII + LF):
  jejak kompresi SHA-256, aturan padding Merkle--Damgård, serangan
  panjang-ekstensi, lima vektor RFC 4231, batas ulang tahun untuk empat panjang
  digest, dan perbandingan tag waktu-konstan. Seluruh nilainya dicocokkan dengan
  `hashlib`/`hmac` dan **cocok**; `praktikum.tex` memuat enam `lstinputlisting`
  yang menampilkan potongan-potongan berkas ini melalui `\codefile{}`
- [x] **Pertumbuhan komponen OBE** — `praktikum.tex` 1 → 4 `obeactivity`
  (Aktivitas 15.1 efek longsoran, 15.2 jejak kompresi, 15.3 panjang-ekstensi,
  15.4 vektor MAC), `latihan.tex` 1 → 4 `obereflection` (3 → 15 butir),
  `rangkuman.tex` 7 → 12 butir, `evaluasi.tex` 3 → 10 butir kuis dan
  `competencychecklist` 5 → 12 baris

### Koreksi angka (temuan verifikasi sendiri)

Contoh CMAC pada bab ini semula ditulis dengan **kunci yang seluruhnya nol**
(`0000…0000`) dan empat tag. Verifikasi silang dengan OpenSSL 3.2.4 menunjukkan
klaim itu tidak konsisten dengan angkanya:

| Klaim semula | Verifikasi |
|---|---|
| Kunci yang dipakai adalah nol | **salah** — $E_K(0^{128})$ hanya memberi `7df76b0c…` bila $K = \texttt{2b7e151628aed2a6abf7158809cf4f3c}$ (kunci vektor uji RFC 4493); dengan kunci nol hasilnya `66e94bd4ef8a2c3b884cfa59ca342b2e` |
| `320 bit (3 blok): ce0cbf17…` | **salah** — itu CMAC pesan **256 bit**; nilai 320 bit yang benar `dfa66747de9ae63030ca32611497c827` |
| `512 bit (4 blok): c47c4d9d…` | **salah** — tidak cocok dengan kunci mana pun dan pesan mana pun yang diuji; nilai 512 bit yang benar `51f0bebf7e3b9d92fc49741779363cfe` |
| Subkunci $K_1$, $K_2$ | **benar** — `fbeed618…` dan `f7ddac30…` memang penggandaan berurutan dari `7df76b0c…` dengan $\mathrm{Rb} = \texttt{0x87}$ |
| Perintah OpenSSL pada contoh | **tidak lengkap** — tidak ada pesan yang disalurkan dan kuncinya salah; diganti bentuk `printf '…' \| xxd -r -p \| openssl mac …` yang benar-benar menghasilkan `070a16b4…` |

Seluruh angka CMAC pada `contoh.tex` dan `section-03.tex` kini bersesuaian dengan
vektor uji RFC 4493 \citep{rfc4493} (0, 128, 320, dan 512 bit), dan keempatnya
sudah diverifikasi ulang dengan OpenSSL. Nilai $L$, $K_1$, $K_2$, dan $E_K(K_2)$
yang semula benar tetap dipertahankan.

## Bab 16 — Otentikasi dan Tanda Tangan Digital (tanpa sumber referensi)  `[x]` SELESAI
Sumber: `stallings2017`, `menezes1996`, `rsa1978`, `katz2020`, FIPS 186-5, RFC 5280,
RFC 8032, RFC 8446, RFC 8017, Bleichenbacher 1998, ROCA 2017. Target: ±5.000 kata.
Bab ini juga tidak punya berkas di `referensi/`, sehingga seluruh materi disusun dari
sumber silabus tersebut. **Empat entri baru** di `references.bib` (`rfc5280`,
`rfc8032`, `nemec2017roca`, `bernstein2012ed25519`); `references.bib` 90 → **94 entri**.

Hasil: **10.658 kata** pada sembilan berkas (empat section 7.321, contoh 1.602,
praktikum 543, latihan 350, rangkuman 343, evaluasi 402) — semula 2.177 kata, jadi
**4,9 kali** — **10 persamaan bernomor** (semula **nol**), **5 tabel bernomor**
(semula **nol**), **5 gambar bernomor** (semula tiga diagram TikZ:
`alur-tanda-tangan`, `alur-tls`, `rantai-sertifikat`; kini ditambah diagram
`jabat-tangan-tls` dan satu gambar raster `ukuran-tanda-tangan`), **6 contoh terhitung**
di dalam environment `example` (semula **nol**), **25 subbagian** (16 → 25), dan
**31 sitasi** (semula 12).

- [x] **X.509 v3 penuh (ASN.1) + contoh sertifikat nyata** — Subbagian
  `Sertifikat X.509` (Tabel~\ref{tab:x509-v3}, sembilan bidang, kolom `p{4.6cm}`) dan
  `Isi dan Tanda Tangan Sertifikat X.509` dengan **angka hasil pengukuran sendiri**:
  berkas DER **831 byte** = kunci publik 294 + tanda tangan 256 + sisa 281, dibangkitkan dengan
  perintah `openssl` yang benar-benar ditampilkan utuh pada bab
  \citep{rfc5280} — disertai catatan bahwa perintah pendek itu **tidak** memasang
  ekstensi *Key Usage* maupun *Subject Alternative Name*
- [x] **TLS 1.2 vs 1.3: urutan pesan + key schedule** — Subbagian `Jabat Tangan TLS
  1.2` (diagram `figures/alur-tls`) dan `Jabat Tangan TLS 1.3 dan Jadwal Kunci`
  (diagram baru `figures/jabat-tangan-tls`, TLS 1.2 dan TLS 1.3 berdampingan),
  termasuk *key transport* RSA vs (EC)DHE, *forward secrecy*, dan jadwal kunci HKDF
  (*early secret* → *handshake secret* → *master secret*) \citep{rfc8446}
- [x] **Validasi sertifikat: jalur, name constraints, CRL vs OCSP** — Subbagian
  `Validasi Sertifikat dan Status Pencabutan` (`subsec:validasi-sertifikat`):
  pembangunan jalur, pemeriksaan tanda tangan tiap tautan, masa berlaku, pencocokan
  nama, batasan nama, lalu CRL vs OCSP vs *OCSP stapling* beserta *Certificate
  Transparency*
- [x] **Schnorr, EdDSA/Ed25519, RSA-PSS + tabel perbandingan** — Subbagian `Tanda
  Tangan Schnorr dan EdDSA` (`subsec:eddsa`) dan `Perbandingan Algoritma Tanda
  Tangan` (Tabel~\ref{tab:perbandingan-tanda-tangan} + Gambar~\ref{fig:ukuran-tanda-tangan}),
  berikut subbagian `Tanda Tangan RSA` yang membahas PKCS\#1 v1.5 vs PSS
  \citep{rsa1978,rfc8017,stallings2017}
- [x] **Permukaan serangan padding + Bleichenbacher + ROCA** — pemalsuan
  eksistensial multiplikatif (Persamaan~\eqref{eq:rsa-multiplikatif} dan
  \eqref{eq:rsa-pemalsuan}), subbagian `Kesalahan Fatal: Pemakaian Ulang k`
  (`subsec:pemakaian-ulang-k`), dan paragraf `Verifikasi padding yang longgar`
  \citep{bleichenbacher1998}, `Serangan galat pada penandatanganan dengan CRT`, serta
  ROCA \citep{nemec2017roca}
- [x] **Vektor uji nyata (RFC 8032)** — Contoh~\ref{ex:ed25519-rfc8032} memakai
  **vektor uji kedua** RFC 8032 (pesan satu byte `72`), dengan tanda tangan yang
  direproduksi **byte demi byte** lewat `openssl pkeyutl -sign -rawin`; vektor uji
  pertama (pesan kosong) tetap ditampilkan pada Subbagian~\ref{subsec:eddsa}
  \citep{rfc8032}
- [x] **Otentikasi timbal balik, signcryption, certificate transparency** — Subbagian
  `Otentikasi Entitas dengan Tantangan dan Respons` (`subsec:tantangan-respons`,
  dengan contoh XOR `0x3C` $\oplus$ `0x5A` = `0x66` dan pengulangan *nonce*),
  `Otentikasi Entitas vs Otentikasi Pesan` (`subsec:entitas-vs-pesan` +
  Tabel~\ref{tab:entitas-vs-pesan}), catatan *signcryption* pada penutup
  section-01, dan *Certificate Transparency* pada Subbagian~\ref{subsec:validasi-sertifikat}
- [x] **Gambar + entri `.bib`** — satu gambar raster baru
  `figures/ukuran-tanda-tangan.png` (632 kali 274 piksel, dibangkitkan oleh
  `scripts/refactor/figures/ukuran_tanda_tangan.py` dengan pustaka standar saja
  karena matplotlib tidak tersedia) dan satu diagram TikZ baru
  `figures/jabat-tangan-tls.tex`; empat entri `.bib` baru
- [x] **Persamaan bernomor** — sepuluh `equation` berlabel pada section-02:
  `eq:rsa-tanda-tangan`, `eq:rsa-multiplikatif`, `eq:rsa-pemalsuan`,
  `eq:dsa-tanda-tangan`, `eq:dsa-verifikasi`, `eq:dsa-bukti-1`, `eq:dsa-bukti-2`,
  `eq:dsa-ulang-s`, `eq:dsa-pulih-k`, `eq:dsa-pulih-x`
- [x] **Pertumbuhan komponen OBE** — `praktikum.tex` 1 → 4 `obeactivity`
  (Aktivitas 16.1 sertifikat browser, 16.2 rantai sertifikat dengan OpenSSL,
  16.3 vektor uji Ed25519, 16.4 pemulihan kunci dari pemakaian ulang $k$),
  `latihan.tex` 1 → 4 `obereflection` (3 → 12 butir), `rangkuman.tex` 7 → 13 butir,
  `evaluasi.tex` 3 → 10 butir kuis + studi kasus dan `competencychecklist`
  5 → 12 baris

### Koreksi angka (temuan verifikasi sendiri)

| Klaim semula | Verifikasi |
|---|---|
| Pemulihan kunci privat $x$ dari pemakaian ulang $k$ pada DSA | **salah** — rumus yang tercetak semula, $x = \frac{s_1 - s_2}{r} \cdot \frac{1}{h_1 - h_2} \bmod q$, tidak menurunkan hasil yang benar (memberi $x = 6$, bukan $5$). Bentuk yang benar adalah dua langkah pada Persamaan~\eqref{eq:dsa-pulih-k} dan \eqref{eq:dsa-pulih-x}: $k \equiv (h_1-h_2)(s_1-s_2)^{-1} \pmod q$, lalu $x \equiv (s_1 k - h_1) r^{-1} \pmod q$. Diuji dengan Python pada $p=23$, $q=11$, $g=2$, $x=5$, $h_1=10$, $h_2=7$, $k=3$ → $k=3$ dan $x=5$ **tepat** |
| `praktikum.tex` menjanjikan padanan C++ dan MATLAB yang tidak ada | **salah** — berkas `code/cpp/tanda_tangan.cpp` dan `code/matlab/tanda_tangan.m`. Keduanya **dibuat** (bukan janji dihapus), mengikuti pola `hash_avalanche.{cpp,m}` dengan SHA-256 satu blok. Logikanya disimulasikan di Python (karena `g++`/`cl` tidak tersedia): hash `696`, $d=1019$, tanda tangan `644`, pemalsuan ditolak, dan $n^2 = 11.135.569 < 2^{32}$ sehingga seluruh hasil antara `uint64` aman |
| RFC 8032 vektor uji 1 (pesan kosong) dapat direproduksi lokal | **tidak dapat** — OpenSSL 3.2.4 menolak dengan `pkeyutl: Could not allocate 0 bytes for oneshot sign/verify buffer`. Contoh terhitung karena itu dipindahkan ke **vektor uji 2** (pesan `72`) yang berhasil direproduksi tepat; keterbatasan itu dicatat jujur di akhir Contoh~\ref{ex:ed25519-rfc8032} |
| Ukuran sertifikat X.509 | **diukur ulang** — percobaan pertama memakai perintah `-addext` (1.071 byte DER), sedangkan perintah yang ditampilkan pada bab lebih pendek. Perintah pada bab dijalankan **persis seperti tertulis** → **831 byte** DER; prose disesuaikan dan ditambah catatan bahwa perintah itu tidak memasang *Key Usage*/*SAN* |

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
  `eq:mitm-k1`, `eq:mitm-k2`); Bab 12 menambah 10 (`eq:dlp-elgamal`,
  `eq:elgamal-kunci`, `eq:elgamal-a`, `eq:elgamal-b`, `eq:elgamal-invers`,
  `eq:elgamal-dekripsi`, `eq:elgamal-bukti`, `eq:elgamal-homomorfik`,
  `eq:elgamal-k-ulang`, `eq:elgamal-k-ulang-m2`); Bab 13 menambah 8
  (`eq:knapsack-dasar`, `eq:superincreasing`, `eq:mh-kunci`, `eq:mh-enkripsi`,
  `eq:mh-dekripsi`, `eq:mh-bukti`, `eq:mh-bukti-eksak`, `eq:densitas-knapsack`);
  **Bab 14 menambah 20** (`eq:gf2m-polinom`, `eq:gf2m-tambah`, `eq:gf2m-kali`,
  `eq:akar-gf11`, `eq:weierstrass`, `eq:diskriminan`, `eq:titik-o`,
  `eq:gradien-pq`, `eq:koordinat-pq`, `eq:gradien-mod-p`,
  `eq:gradien-penggandaan`, `eq:koordinat-penggandaan`, `eq:pelelaran`,
  `eq:ecdlp`, `eq:ecc-kunci-publik`, `eq:ecdh-kunci`, `eq:eceg-cipher`,
  `eq:eceg-dekripsi`, `eq:koblitz-x`, `eq:koblitz-dekode`).
  **Bab 15 menambah 16** (`eq:sha256-jadwal`, `eq:sha256-fungsi`,
  `eq:sha256-kompresi`, `eq:md5-putaran`, `eq:md-iterasi`, `eq:birthday-peluang`,
  `eq:birthday-50`, `eq:hmac-panjang-kunci`, `eq:hmac-rumus`, `eq:cbc-mac`,
  `eq:cmac-subkunci`, `eq:poly1305`, dan empat persamaan penunjang), dan
  **Bab 16 menambah 10** (`eq:rsa-tanda-tangan`, `eq:rsa-multiplikatif`,
  `eq:rsa-pemalsuan`, `eq:dsa-tanda-tangan`, `eq:dsa-verifikasi`, `eq:dsa-bukti-1`,
  `eq:dsa-bukti-2`, `eq:dsa-ulang-s`, `eq:dsa-pulih-k`, `eq:dsa-pulih-x`).
  **Tersisa hanya Bab 01 dan 02, yang memang tidak memuat penurunan rumus** — keduanya
  bab konseptual (urgensi kriptografi; jenis/tujuan serangan), sehingga penomoran
  persamaan tidak diperlukan. Keempat belas bab lainnya sudah memakai `equation`
  berlabel.
- [x] **`contoh.tex` tidak konsisten** — bab 13 (6 `example`, semula **nol**),
  bab 14 (6, semula **nol**), bab 15 (7, semula **nol**), dan bab 16 (6, semula
  **nol**) sudah beres. **Seluruh 16 bab kini konsisten memakai environment
  `example`.**
- [x] **Bab 15 dan 16 tanpa gambar raster.** (Bab 03, 04, dan 14 sudah punya.)
  Bab 15 mendapat `longsoran-sha256.png` dan bab 16 `ukuran-tanda-tangan.png`,
  keduanya dibangkitkan dengan pustaka standar saja oleh skrip di
  `scripts/refactor/figures/` (`avalanche_hash.py`, `ukuran_tanda_tangan.py`).
  Skrip pembuat gambar raster yang lebih lama: `entropi_ternate.py`.
- [x] **Bab tanpa sitasi: 14.** (02, 03, 04, 05, 06, 07, 14, 15, dan 16 sudah selesai;
  Bab 14 semula **nol** sitasi, kini menyitasi `stallings2017`, `menezes1996`,
  `fips1865`, dan enam entri baru — `miller1986`, `koblitz1987`,
  `hankerson2004`, `washington2008`, `bernstein2006curve25519`,
  `pollard1978`. Bab 07 menyitasi `fips46`, `biham1991`, `matsui1994`,
  `eff1998`, `stallings2017`, dan `menezes1996`; Bab 06 menyitasi
  `shannon1949`, `stallings2017`, dan `menezes1996`.)

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
