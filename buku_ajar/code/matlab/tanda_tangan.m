% Tanda tangan digital RSA: penandatanganan, verifikasi, dan uji pemalsuan.
% Bab 16, Aktivitas 16.1.
%
% Padanan MATLAB dari code/python/tanda_tangan.py. Pasangan kunci diambil dari
% Contoh Terhitung Bab 10 (p = 47, q = 71, e = 79, d = 1019) supaya hasilnya
% dapat diperiksa dengan angka yang sudah dikenal.
%
% SHA-256 tidak tersedia sebagai fungsi bawaan MATLAB tanpa toolbox tambahan,
% jadi fungsi kompresinya diimplementasikan sendiri. Versi ini sengaja
% dibatasi pada pesan yang muat dalam satu blok 512 bit, yaitu pesan yang
% lebih pendek dari 56 byte; pesan yang lebih panjang memerlukan pemrosesan
% blok demi blok. Kedua kalimat uji pada bab ini hanya 43 byte, sehingga
% hasilnya sama dengan SHA-256 yang dihitung Python.
%
% Catatan: MATLAB menjenuhkan (saturasi) bilangan bulat pada operasi
% aritmetika, bukan membiarkannya berputar seperti pada C. Karena itu setiap
% penjumlahan 32 bit dilewatkan fungsi add32 agar perilakunya sama dengan
% standar SHA-256.
%
% Jalankan: tanda_tangan   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

% Kunci Bob: publik untuk memverifikasi, privat untuk menandatangani.
p = 47; q = 71; e = 79;
n = p * q;
d = invers_modulo(e, (p - 1) * (q - 1));

fprintf('Kunci publik  (e, n) = (%d, %d)\n', e, n);
fprintf('Kunci privat  (d, n) = (%d, %d)\n\n', d, n);

pesan = 'Transfer Rp5.000.000 ke rekening 1234567890';
tanda_tangan = tanda_tangani(pesan, d, n);

fprintf('Pesan        : %s\n', pesan);
fprintf('Hash (mod n) : %d\n', hash_pesan(pesan, n));
fprintf('Tanda tangan : %d\n\n', tanda_tangan);
fprintf('Verifikasi pesan asli        : %d\n\n', ...
        verifikasi(pesan, tanda_tangan, e, n));

% Penyerang mengubah isi pesan, tetapi tanda tangannya tetap yang lama.
pesan_palsu = 'Transfer Rp5.000.000 ke rekening 9999999999';
fprintf('Pesan diubah : %s\n', pesan_palsu);
fprintf('Hash (mod n) : %d\n', hash_pesan(pesan_palsu, n));
fprintf('Verifikasi pesan yang diubah : %d\n\n', ...
        verifikasi(pesan_palsu, tanda_tangan, e, n));

fprintf('Tanda tangan tidak lagi cocok karena hash pesan yang diubah berbeda\n');
fprintf('dari nilai hash yang dipulihkan dengan kunci publik. Penyerang yang\n');
fprintf('ingin memalsukan tanda tangan harus menemukan kolisi SHA-256, yaitu\n');
fprintf('dua pesan berbeda dengan hash sama, dan itu tidak praktis. Inilah\n');
fprintf('yang memberi sifat nirpenyangkalan (non-repudiation): hanya pemegang\n');
fprintf('kunci privat yang dapat membuat tanda tangan yang sah.\n');

% --- Fungsi lokal -----------------------------------------------------------

% Cari d sehingga e * d = 1 (mod phi), memakai Algoritma Euclidean lanjar.
function d = invers_modulo(e, phi)
lama_d = 0; d = 1;
lama_phi = phi; sisa = e;
while sisa ~= 0
    hasil_bagi = floor(lama_phi / sisa);
    [lama_d, d] = deal(d, lama_d - hasil_bagi * d);
    [lama_phi, sisa] = deal(sisa, lama_phi - hasil_bagi * sisa);
end
if lama_phi ~= 1
    error('e tidak relatif prima terhadap phi(n)');
end
d = mod(lama_d, phi);
end

% Hash pesan sebagai bilangan bulat modulo n. Digest 256 bit direduksi kata
% demi kata dengan basis 2^32; cara ini sama dengan menghitung
% int(hexdigest, 16) % n seperti pada Python.
function nilai = hash_pesan(pesan, n)
digest = sha256(pesan);
nilai = uint64(0);
for i = 1:8
    nilai = mod(nilai * uint64(4294967296) + uint64(digest(i)), uint64(n));
end
nilai = double(nilai);
end

% Buat tanda tangan: S = hash(pesan)^d mod n, memakai kunci privat.
function s = tanda_tangani(pesan, d, n)
s = pangkat_mod(hash_pesan(pesan, n), d, n);
end

% Verifikasi tanda tangan dengan kunci publik.
function sah = verifikasi(pesan, tanda_tangan, e, n)
sah = pangkat_mod(tanda_tangan, e, n) == hash_pesan(pesan, n);
end

% Perpangkatan modular: basis^eksponen mod modulus.
function hasil = pangkat_mod(basis, eksponen, modulus)
modulus = uint64(modulus);
hasil = uint64(1);
basis = mod(uint64(basis), modulus);
while eksponen > 0
    if mod(eksponen, 2) == 1
        hasil = mod(hasil * basis, modulus);
    end
    basis = mod(basis * basis, modulus);
    eksponen = floor(eksponen / 2);
end
hasil = double(hasil);
end

% Hitung SHA-256 untuk pesan yang muat dalam satu blok 512 bit.
function hash = sha256(pesan)
if numel(pesan) >= 56
    error('Versi ini hanya menangani pesan yang lebih pendek dari 56 byte');
end

% Konstanta putaran SHA-256 dan nilai awal hash.
K = uint32([0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, ...
    0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, ...
    0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, ...
    0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, ...
    0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, ...
    0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, ...
    0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, ...
    0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, ...
    0x106aa070, 0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, ...
    0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, ...
    0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]);

hash = uint32([0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, ...
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]);

% Padding: bit 1, lalu nol secukupnya, lalu panjang pesan dalam bit.
blok = zeros(1, 64, 'uint8');
for i = 1:numel(pesan)
    blok(i) = uint8(pesan(i));
end
blok(numel(pesan) + 1) = 0x80;
panjang_bit = numel(pesan) * 8;
for i = 0:7
    blok(64 - i) = uint8(mod(panjang_bit, 256));
    panjang_bit = floor(panjang_bit / 256);
end

% Jadwal pesan: 16 kata pertama dari blok, sisanya diperluas.
w = zeros(1, 64, 'uint32');
for t = 1:16
    w(t) = bitshift(uint32(blok(4 * t - 3)), 24) + ...
           bitshift(uint32(blok(4 * t - 2)), 16) + ...
           bitshift(uint32(blok(4 * t - 1)), 8) + ...
           uint32(blok(4 * t));
end
for t = 17:64
    s0 = bitxor(bitxor(rotr(w(t - 15), 7), rotr(w(t - 15), 18)), ...
                bitshift(w(t - 15), -3));
    s1 = bitxor(bitxor(rotr(w(t - 2), 17), rotr(w(t - 2), 19)), ...
                bitshift(w(t - 2), -10));
    w(t) = add32(add32(w(t - 16), s0), add32(w(t - 7), s1));
end

a = hash(1); b = hash(2); c = hash(3); d = hash(4);
e = hash(5); f = hash(6); g = hash(7); h = hash(8);

for t = 1:64
    s1 = bitxor(bitxor(rotr(e, 6), rotr(e, 11)), rotr(e, 25));
    ch = bitxor(bitand(e, f), bitand(bitcmp(e, 'uint32'), g));
    temp1 = add32(add32(add32(add32(h, s1), ch), K(t)), w(t));
    s0 = bitxor(bitxor(rotr(a, 2), rotr(a, 13)), rotr(a, 22));
    maj = bitxor(bitxor(bitand(a, b), bitand(a, c)), bitand(b, c));
    temp2 = add32(s0, maj);

    h = g; g = f; f = e; e = add32(d, temp1);
    d = c; c = b; b = a; a = add32(temp1, temp2);
end

hash(1) = add32(hash(1), a);
hash(2) = add32(hash(2), b);
hash(3) = add32(hash(3), c);
hash(4) = add32(hash(4), d);
hash(5) = add32(hash(5), e);
hash(6) = add32(hash(6), f);
hash(7) = add32(hash(7), g);
hash(8) = add32(hash(8), h);
end

% Penjumlahan 32 bit yang berputar (bukan menjenuh), sesuai perilaku SHA-256.
function s = add32(a, b)
s = uint32(mod(double(a) + double(b), 4294967296));
end

% Geser kanan siklik (rotate right) sejauh n bit.
function y = rotr(x, n)
y = bitor(bitshift(x, -n), bitshift(x, 32 - n));
end
