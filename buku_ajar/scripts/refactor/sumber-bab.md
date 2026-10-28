# Sumber Tiap Bab

Peta ini mencatat berkas, topik, dan halaman `pages/llm` yang menopang setiap
bab. Baris yang berasal dari luar korpus ditandai **TERBATAS** dan memuat URL.
Berkas ini tidak dimasukkan ke dalam buku.

## Bab 01 — Pengantar dan Urgensi Kriptografi

Modul: `referensi/01-Pengantar-Kriptografi-(2026)`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Model komunikasi, Alice/Bob, penyusup, lima tindakan penyerang | p2–3, p27–29 |
| `section-02.tex` | Empat masalah keamanan dan tabelnya | p6–14 |
| `section-03.tex` | Definisi, empat layanan, tiga jenis algoritma, dua aplikasi, sejarah | p11–15, p36–42, p44–58 |
| `section-04.tex` | Terminologi, sistem kriptografi, miskonsepsi | p25–41, p71–72 |
| `section-05.tex` | Kriptanalisis, Al-Kindi, Telegram Zimmermann, kriptologi | p44–47 |
| `section-06.tex` | Kebocoran data, penyadapan, lembaga, tantangan masa depan | p16–24, p43, p64–70 |
| `contoh.tex` | Base64 bukan enkripsi; jumlah kunci simetri dan nir-simetri | p71–72; p58–60 |
| `praktikum.tex` | Enkripsi at rest/in motion, encoding/hashing, insiden kebocoran | p43, p71–72, p19–23 |
| `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–72 |

## Bab 02 — Layanan Keamanan dan Serangan Kriptografi

Modul: `referensi/06-Serangan-pada-kriptografi-(2026)`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Definisi serangan dan Prinsip Kerckhoffs | p2–3 |
| `section-02.tex` | Lima jenis serangan berdasarkan informasi | p4–20 |
| `section-03.tex` | Lima tujuan serangan | p22–27 |
| `section-04.tex` | Serangan pasif dan aktif, metode penyadapan | p29–51 |
| `section-05.tex` | Keamanan komputasi dan serangan saluran samping | p21, p52 |
| `contoh.tex` | Ciphertext-only Caesar, chosen-plaintext Vigenère, replay | p7, p13–14, p27 |
| `praktikum.tex` | Wireshark, kebocoran waktu, pemutaran ulang | p33–34, p52, p27 |
| `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–52 |

## Bab 03 — Landasan Matematika untuk Kriptografi

Modul: `referensi/02-Landasan-Matematika-Kriptografi-(2026)`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Peta topik matematika, modulo, kekongruenan, relatif prima, Algoritma Euclidean, invers modulo, bilangan prima | p2–3 |
| `section-02.tex` | Kuantisasi informasi, entropi, rentang, entropi maksimum, studi kasus | p4–9 |
| `contoh.tex` | Modulo dan invers, entropi `AABBCBDB`, entropi berita Ternate | p3, p6, p9 |
| `praktikum.tex` | Eksperimen modulo/invers, Algoritma Euclidean, entropi teks | p3–9 |
| `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–9 |

## Bab 04 — Kriptografi Klasik

Modul: `referensi/03-Kriptografi-klasik-bagian1-(2026)`,
`referensi/04-Kriptografi-klasik-bagian2-(2026)`,
`referensi/05-One-Time-Pad-(2026)`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Cipher substitusi dan transposisi, super-enkripsi, analisis frekuensi | 03: p2–42; 04: p2–26 |
| `section-02.tex` | Vigenère, Extended Vigenère, Kasiski, varian Vigenère | 04: p27–65 |
| `section-03.tex` | Playfair dan Hill | 04: p66–107 |
| `section-04.tex` | Mesin Enigma, rotor, contoh, kriptanalisis | 04: p108–119 |
| `section-05.tex` | Affine cipher, contoh, kriptanalisis | 04: p86–94 |
| `section-06.tex` | One-time pad, tiga syarat, kerahasiaan sempurna, kelemahan | 05: p2–25 |
| `contoh.tex` | Caesar, Vigenère, OTP | 03: p24; 04: p27–48; 05: p4–11 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | 03: p2–42; 04: p2–119; 05: p2–25 |

## Bab 05 — Stream Cipher

Modul: `referensi/07-Kripto-modern-dan-stream-cipher-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Bit/byte/heksadesimal, XOR, cipher XOR sederhana | p2–24 |
| `section-02.tex` | Stream cipher, keystream generator, LFSR/FSR, penyebaran galat | p22–39 |
| `section-03.tex` | RC4, A5/1, Trivium, Salsa20/ChaCha20 | p40–94 |
| `contoh.tex` | Keystream LFSR, RC4 mainan, cipher XOR | p12–48 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–94 |

## Bab 06 — Block Cipher

Modul: `referensi/08-Block-Cipher-Bagian1-(2026)`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Konsep cipher blok, ukuran blok/kunci, padding | p2–8 |
| `section-02.tex` | Mode ECB, CBC, CFB, OFB, CTR | p9–50 |
| `section-03.tex` | Confusion dan diffusion | p51–59 |
| `section-04.tex` | Cipher berulang, jaringan Feistel, kunci putaran, ukuran blok/kunci | p60–74 |
| `contoh.tex` | ECB dan CBC | p11–31 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–74 |

## Bab 07 — DES

Modul: `referensi/09-Beberapa-block-cipher-bagian1-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Sejarah DES, pembangkitan kunci, permutasi awal, enciphering, invers IP, putaran Feistel | p3–34 |
| `section-02.tex` | Efek longsoran, mode DES, kunci lemah, implementasi, keamanan | p32–49 |
| `section-03.tex` | Double DES dan Triple DES | p46–53 |
| `contoh.tex` | Jejak putaran DES dan vektor uji | p10–34 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p3–53 |

## Bab 08 — AES

Modul: `referensi/10-Beberapa-block-cipher-bagian2-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Latar belakang, Rijndael, AES-128 | p2–17 |
| `section-02.tex` | SubBytes, ShiftRows, MixColumns, AddRoundKey, S-box, dekripsi | p18–45 |
| `section-03.tex` | Pembangkitan kunci putaran | p31–38 |
| `section-04.tex` | Galois Field GF(2^8) | p54–59 |
| `contoh.tex` | Contoh transformasi dan jejak AES | p13–52 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–59 |

## Bab 09 — Block Cipher Lain

Modul: `referensi/11-Beberapa-block-cipher-bagian3-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | GOST/Magma | p3–13 |
| `section-02.tex` | RC5 dan RC6 | p14–28 |
| `section-03.tex` | Blowfish, Serpent, Twofish, MARS | p29–37 |
| `contoh.tex` | Jadwal kunci RC5 dan putaran GOST | p15–28 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p3–37 |

## Bab 10 — RSA

Modul: `referensi/13-Algoritma-RSA-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Pendahuluan dan properti RSA | p2–7 |
| `section-02.tex` | Penurunan rumus enkripsi dan dekripsi | p5–8 |
| `section-03.tex` | Pembangkitan kunci, enkripsi, dekripsi, contoh | p8–16 |
| `section-04.tex` | Keamanan, parameter, kelemahan, MITM, OAEP, program | p17–38 |
| `contoh.tex` | Contoh pembangkitan kunci dan pengiriman pesan | p11–16 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–54 |

## Bab 11 — Diffie–Hellman

Modul: `referensi/15-Algoritma-Diffie-Hellman-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Persoalan distribusi kunci dan kriptografi hibrida | p2–7 |
| `section-02.tex` | Algoritma pertukaran kunci dan parameter | p8–16 |
| `section-03.tex` | Serangan pada Diffie–Hellman | p17–18 |
| `section-04.tex` | Pertukaran kunci tiga pihak dan contoh | p19–22 |
| `contoh.tex` | Contoh numerik pertukaran kunci | p8–22 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–22 |

## Bab 12 — ElGamal

Modul: `referensi/14-Algoritma-Elgamal-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Pendahuluan dan kedudukan ElGamal | p2–4 |
| `section-02.tex` | Akar primitif dan logaritma diskrit | p5–9 |
| `section-03.tex` | Pembangkitan kunci, enkripsi, dekripsi | p10–12 |
| `section-04.tex` | Simulasi daring | p20 |
| `contoh.tex` | Contoh numerik ElGamal | p14–19 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–20 |

## Bab 13 — Knapsack

Modul: `referensi/16-Algoritma-kripto-knapsack-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Persoalan knapsack | p2–6 |
| `section-02.tex` | Superincreasing knapsack | p7–11 |
| `section-03.tex` | Sistem Merkle–Hellman: kunci, enkripsi, dekripsi | p12–20 |
| `section-04.tex` | Kriptanalisis dan implementasi | p21, p23–24 |
| `contoh.tex` | Empat contoh terhitung knapsack | p5–20 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | p2–24 |

## Bab 14 — Kriptografi Kurva Eliptik (ECC)

Modul: `referensi/17-ECC-Bagian1-2026`,
`referensi/18-ECC-Bagian2-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Grup, medan, medan berhingga, aritmetika polinomial | 17: p3–24 |
| `section-02.tex` | Kurva eliptik, penjumlahan titik, penggandaan, perkalian skalar | 18: p4–30 |
| `section-03.tex` | ECDLP, ECDH, ECEG, perbandingan dengan RSA | 18: p31–43 |
| `section-04.tex` | Pemetaan pesan, metode Koblitz, efisiensi, keamanan | 18: p44–52 |
| `contoh.tex` | Contoh GF, kurva, ECDH, ECEG, Koblitz | 17–18: p3–52 |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Seluruh topik bab | 17: p3–24; 18: p4–52 |

## Bab 15 — Fungsi Hash dan MAC

Modul: `referensi/01-Pengantar-Kriptografi-(2026)`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Fungsi hash sebagai jenis algoritma ketiga, kompresi, ireversibel | p58, p60, p62–63 |
| `section-02.tex` | Nama algoritma hash (MD5, SHA-1, SHA-2, SHA-3, RIPEMD, WHIRLPOOL) | p62 |
| `section-03.tex` | Catatan cakupan: MAC tidak dibahas dalam modul | — |
| `contoh.tex` | Catatan cakupan: tidak ada contoh hitung di modul | — |
| `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Panjang digest tetap dan perubahan digest | p62–63 |

## Bab 16 — Otentikasi dan Tanda Tangan Digital

Modul: `referensi/01-Pengantar-Kriptografi-(2026)`,
`referensi/13-Algoritma-RSA-2026`,
`referensi/18-ECC-Bagian2-2026`

| Berkas | Topik | Halaman llm |
|---|---|---|
| `section-01.tex` | Nir-penyangkalan | 01: p9, p13 |
| `section-02.tex` | Tanda tangan digital: verifikasi dengan kunci publik, pembangkitan dengan kunci privat; RSA dan ECDSA | 13: p33; 18: p37 |
| `section-03.tex` | Catatan cakupan: PKI tidak dibahas dalam modul | — |
| `section-04.tex` | Catatan cakupan: TLS hanya disebut sebagai nama algoritma | 01: p50 |
| `contoh.tex`, `praktikum.tex`, `latihan.tex`, `rangkuman.tex`, `evaluasi.tex` | Sesuai sisa materi | 01: p9, p13, p50; 13: p33; 18: p37 |
