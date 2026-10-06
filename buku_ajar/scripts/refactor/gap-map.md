# Peta Celah: Referensi → Buku Ajar

Berkas kerja untuk Tahap 0–16 rencana `dynamic-brewing-stream.md`.
Keadaan awal: buku 178 halaman, 0 error, 0 warning. Tiap bab 1.100–2.200 kata.
Sasaran: ±4.000–6.000 kata/bab (prosa naratif), tabel, contoh terhitung, gambar.

Legenda status: `[ ]` belum · `[~]` sedang dikerjakan · `[x]` selesai.

**Kemajuan:** Tahap 1–5 (Bab 01–05) selesai. Buku 220 halaman, gerbang kebersihan
`output/main_build.log` = 0 pada ketujuh pola. Berikutnya: Tahap 6 (Bab 06).

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

## Bab 06 — Block Cipher: Konsep dan Mode Operasi
Sumber: `referensi/08-*` (6.812 kata, 21 topik, 92 gambar). Target: ±4.000 kata.
**Belum punya sitasi.**

- [ ] Tabel perbandingan lima mode operasi (ECB/CBC/CFB/OFB/CTR)
- [ ] Contoh padding ECB
- [ ] CFB s-bit (CFB-8): shift register, IV
- [ ] OFB: tanpa propagasi galat, kasus $s=b$
- [ ] Contoh konkret confusion/diffusion (S-box DES & AES)
- [ ] Contoh cipher mainan 8 bit

## Bab 07 — Analisis Algoritma Block Cipher: DES
Sumber: `referensi/09-*` (5.218 kata, 16 topik, 74 gambar). Target: ±5.000 kata.
**Prioritas #1.** **Belum punya sitasi.**

- [ ] **Tabel bit resmi DES**: IP, IP⁻¹, E, S-box S1–S8, P, PC-1, PC-2
- [ ] Nilai kunci lemah (4 nilai heksadesimal)
- [ ] Sejarah DES: NIST 1972, Lucifer, NSA, FIPS PUB 46
- [ ] Brute force terukur + kronologi DESCHALL / EFF DES Cracker
- [ ] Contoh DES putaran demi putaran + tabel *avalanche*
- [ ] Meet-in-the-middle $X=E_{K_1}(P)=D_{K_2}(C)$ + tabel varian 3DES
- [ ] Mode DES + kecepatan implementasi + misteri S-box NSA

## Bab 08 — Analisis Algoritma Block Cipher: AES
Sumber: `referensi/10-*` (5.580 kata, 21 topik, 55 gambar). Target: ±5.500 kata.

- [ ] **Dekripsi AES** (InvSubBytes, InvShiftRows, InvMixColumns) — absen total
- [ ] Konstruksi S-box: inversi GF(2⁸) + affine + tabel penuh
- [ ] Key Expansion: $w[0..43]$, temp, $g$, Rcon + daftar RC[1..10]
- [ ] Tabel lima finalis AES + tabel parameter Rijndael
- [ ] Contoh perkalian GF(2⁸): $02\cdot26=4C$, $03\cdot7B=8D$, dst.
- [ ] AES-256: 14 putaran, aturan SubWord/Rcon
- [ ] Justifikasi keamanan terukur

## Bab 09 — Studi Algoritma Block Cipher Lainnya
Sumber: `referensi/11-*` (3.352 kata, 11 topik, 19 gambar). Target: ±4.500 kata.

- [ ] **Koreksi keamanan GOST** + tabel kompleksitas serangan + batas rekeying 2³² blok
- [ ] Identitas standar GOST 28147-89 → Magma → Kuznyechik
- [ ] Jadwal kunci RC5: $P_w$/$Q_w$, array $S$, algoritma enkripsi
- [ ] Tabel jadwal kunci GOST + contoh substitusi S-box
- [ ] Kedalaman Blowfish, Serpent, Twofish, MARS (masing-masing 1 TikZ)
- [ ] Ganti gambar raster tabel perbandingan → tabel `booktabs`

## Bab 10 — Algoritma RSA
Sumber: `referensi/13-*` (6.603 kata, 20 topik, 17 gambar). Target: ±5.000 kata.

- [ ] Penurunan rumus RSA dari Teorema Euler (environment `equation`)
- [ ] **Contoh multi-blok "HELLO ALICE"** lengkap
- [ ] Contoh totient $\varphi(20)=8$
- [ ] Tabel parameter rahasia/umum + tabel kesulitan faktorisasi
- [ ] Ancaman kuantum (Shor) + himpunan parameter kedua

## Bab 11 — Protokol Diffie-Hellman
Sumber: `referensi/15-*` (2.457 kata, 8 topik, 11 gambar). Target: ±4.000 kata.
**Belum punya sitasi.**

- [ ] Kriptografi hibrida dengan persamaan eksplisit + diagram
- [ ] Serangan MITM dengan dua kunci bersama eksplisit
- [ ] Protokol tiga pihak lengkap (11 langkah)
- [ ] Catatan sejarah "Diffie–Hellman–Merkle"
- [ ] Contoh numerik kedua ($G=1601$, $N=4789$)

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

- [ ] **Bab 09 menyesatkan soal keamanan GOST** — buku menyiratkan GOST "lebih aman";
  referensi `11-*` menyatakan sebaliknya (2²⁵⁶ → 2¹⁷⁸). Perbaiki + imbangi di `praktikum.tex`.
- [~] **Environment `equation`/`align` ber-nomor** mulai dipakai sejak Bab 03
  (`eq:pembagian`, `eq:mod-tambah`, `eq:mod-kali`, `eq:invers`, `eq:euler`,
  `eq:entropi`); Bab 04 menambah 8 persamaan bernomor (`eq:caesar`,
  `eq:indeks-kebetulan`, `eq:hill`, `eq:affine-enkripsi`, `eq:affine-dekripsi`,
  `eq:affine-simultan-1/2`, `eq:otp-enkripsi`, `eq:otp-dekripsi`, `eq:two-time-pad`,
  `eq:perfect-secrecy`); Bab 05 menambah 7 (`eq:xor-enkripsi`, `eq:xor-dekripsi`,
  `eq:stream-enkripsi`, `eq:stream-dekripsi`, `eq:a51-luaran`, `eq:trivium-luaran`,
  `eq:salsa-final`). Lanjutkan untuk penurunan RSA, ElGamal, ECDLP, hash.
- [ ] **`contoh.tex` tidak konsisten** — bab 13–16 nol `\begin{example}`.
- [ ] **Bab 15 dan 16 tanpa gambar raster.** (Bab 03 dan 04 sudah punya.)
  Skrip pembuat gambar raster: `scripts/refactor/figures/entropi_ternate.py`.
- [ ] **Bab tanpa sitasi: 06, 07, 14.** (02, 03, 04, dan 05 sudah selesai; Bab 05 kini
  menyitasi `estream2008`, `canniere2006trivium`, `bernstein2005salsa20`,
  `bernstein2008chacha`, `anderson1994`, `briceno1999`, `fluhrer2001`, `rfc7465`,
  `rfc8439`, `massey1969`.)

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
  AND" → "Masukan AND").
- **Tanda pisah `---` diikuti kata panjang pada akhir baris** memindahkan titik potong ke
  tempat yang salah dan menghasilkan `Overfull` beberapa pt (Bab 05, paragraf penutup
  section-03) → ganti dengan titik dua atau ubah susunan kalimatnya.
- **Rangkaian `\texttt` berisi biner/heksadesimal di dalam `array`** aman selama tiap baris
  di bawah ~68 karakter; bila lebih, pecah menjadi dua tampilan atau pindahkan ke `tabular`.
- **Label persamaan bersifat global** — sebelum menambah `eq:...` baru, periksa dulu
  dengan `grep -rho "label{eq:nama}" chapters/ | wc -l` agar tidak menimpa label bab lain.
