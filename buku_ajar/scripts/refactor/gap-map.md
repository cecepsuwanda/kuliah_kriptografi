# Peta Celah: Referensi → Buku Ajar

Berkas kerja untuk Tahap 0–16 rencana `dynamic-brewing-stream.md`.
Keadaan awal: buku 178 halaman, 0 error, 0 warning. Tiap bab 1.100–2.200 kata.
Sasaran: ±4.000–6.000 kata/bab (prosa naratif), tabel, contoh terhitung, gambar.

Legenda status: `[ ]` belum · `[~]` sedang dikerjakan · `[x]` selesai.

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

## Bab 02 — Layanan Keamanan dan Serangan
Sumber: `referensi/06-Serangan-pada-kriptografi-(2026)` (4.241 kata, 21 topik, 63 gambar).
Target: ±4.000 kata. **Belum punya sitasi.**

- [ ] Definisi formal tiap tipe serangan + contoh kerja per tipe (Caesar, Vigenère, adaptive, chosen-ciphertext)
- [ ] Tujuan serangan: key-recovery, plaintext-recovery, distinguishing, forgery, replay
- [ ] Tabel 7 kategori serangan Stallings + contoh
- [ ] *Side-channel* konkret: elektromagnetik, akustik, penyadapan kabel, Wireshark
- [ ] Kasus ATM, pemalsuan dan pengulangan pesan

## Bab 03 — Landasan Matematika untuk Kriptografi
Sumber: `referensi/02-*` (**hanya 1.071 kata, 2 topik — paling tipis**); lengkapi dari
`referensi/materi_buku.tex` + `menezes1996` (HAC Bab 2). Target: ±3.500 kata.
**Belum punya sitasi. Nol gambar raster.**

- [ ] Tabel peta topik matematika untuk kriptografi + penanda prasyarat
- [ ] Teori bilangan: sifat pembagian, Algoritma Euclidean, kombinasi lanjar, totient, Teorema Euler, akar primitif, logaritma diskret
- [ ] Contoh entropi teks nyata (berita Kota Ternate: 3,8988 vs 4,3035 bit)
- [ ] $H_{\max}$ 26 huruf = 4,7004 bit; 256 ASCII = 8 bit
- [ ] Latihan modulo negatif dan invers modulo
- [ ] 1–2 gambar baru

## Bab 04 — Kriptografi Klasik
Sumber: `referensi/03-*` (3.455) + `04-*` (11.746) + `05-*` (2.565). Target: ±6.000 kata.

- [ ] Transposisi kolom (kata kunci TOMBAK), Rail Fence $k=3$, transposisi blok
- [ ] Super-enkripsi (Caesar+transposisi → KROHZGZOUZ), ROT13
- [ ] Analisis frekuensi: tabel bigram & trigram, indeks kebetulan
- [ ] Kasiski dengan contoh nyata (jarak 15/15/15/10/10 → SCRAM)
- [ ] Hill 3×3 + kriptanalisis *known-plaintext*
- [ ] Affine: contoh, kriptanalisis, ruang kunci 300, varian blok 4 huruf
- [ ] Vigenère varian: Full, Auto-Key, Running-Key
- [ ] Playfair: sejarah, alasan J dihapus, kriptanalisis bigram
- [ ] Enigma: rotor/plugboard, contoh rotor 6 huruf + gambar
- [ ] OTP: syarat formal, Vernam, contoh, Shannon 1949, alasan tak cocok untuk WhatsApp/HTTPS

## Bab 05 — Stream Cipher
Sumber: `referensi/07-*` (9.039 kata, 35 topik, 94 gambar). Target: ±4.500 kata.
**Belum punya sitasi.**

- [ ] Tabel konversi bit/byte/heksadesimal + tabel kebenaran XOR
- [ ] Tabel daftar cipher alir beserta tahun + tabel perbandingan
- [ ] A5/1: frame 228 bit/4,6 ms, tiga LFSR, clocking mayoritas, kriptanalisis Anderson
- [ ] Trivium: NLFSR 93/84/111, tabel tap, inisialisasi, 1152 warm-up
- [ ] Salsa20/ChaCha20: blok 512 bit, AXR, quarter-round, TLS 1.3
- [ ] RC4: RFC 7465, buang byte awal, varian RC4A/VMPC

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
- [ ] **Nol environment `equation`/`align` ber-nomor** di seluruh buku → pakai untuk
  penurunan RSA, ElGamal, ECDLP, hash.
- [ ] **`contoh.tex` tidak konsisten** — bab 13–16 nol `\begin{example}`.
- [ ] **Bab 03, 15, 16 tanpa gambar raster.**
- [ ] **Bab tanpa sitasi: 02, 03, 05, 06, 07, 14.**
