% Demonstrasi kebocoran pola pada mode ECB dibandingkan mode CBC.
% Bab 6, Aktivitas 6.1.
%
% Untuk kejelasan, block cipher-nya diganti dengan permutasi sederhana
% (block cipher mainan). Tujuannya menunjukkan perilaku mode, bukan kekuatan
% algoritmanya.
%
% Jalankan: mode_operasi   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

% Pola berulang yang mencolok, seperti area warna rata pada sebuah gambar.
plainteks = 'AAAAAAAABBBBBBBBAAAAAAAA';
kunci = 90;        % 0x5A
iv = 'INIT';

blok_ecb = enkripsi_ecb(plainteks, kunci);
blok_cbc = enkripsi_cbc(plainteks, kunci, iv);
blok_asli = bagi_blok(plainteks);

fprintf('Plainteks   : %s\n', plainteks);
fprintf('Blok        :');
for i = 1:numel(blok_asli)
    fprintf(' %s |', blok_asli{i});
end
fprintf('\n\n');

fprintf('ECB (blok identik -> cipher identik):\n');
for i = 1:numel(blok_ecb)
    fprintf('   %s\n', tampilkan_hex(blok_ecb{i}));
end

fprintf('\nCBC (blok identik -> cipher berbeda):\n');
for i = 1:numel(blok_cbc)
    fprintf('   %s\n', tampilkan_hex(blok_cbc{i}));
end

fprintf('\nPada ECB, blok 1 dan 2 (AAAA) menghasilkan cipherteks yang sama,\n');
fprintf('demikian pula blok 3 dan 4 (BBBB), sehingga pola data asli terbaca.\n');
fprintf('Pada CBC, setiap blok terkait dengan blok sebelumnya, sehingga\n');
fprintf('blok yang sama menghasilkan cipherteks yang berbeda.\n');

% --- Fungsi lokal -----------------------------------------------------------

% Block cipher mainan: XOR dengan kunci yang bergeser tiap posisi, lalu putar.
% Kunci bergeser per posisi (kunci + indeks) supaya tiap posisi dalam blok
% mendapat nilai berbeda. Penyandian tetap dapat dibalik, sehingga hasilnya sah
% sebagai block cipher walau sengaja dibuat lemah.
function hasil = kunci_putaran(blok, kunci)
tergeser = blok;
for i = 1:numel(blok)
    tergeser(i) = char(bitand(bitxor(double(blok(i)), kunci + i - 1), 127));
end
hasil = [tergeser(2:end), tergeser(1)];  % putar satu posisi
end

% Potong teks menjadi blok berukuran tetap, tambah padding bila perlu.
function blok = bagi_blok(teks)
UKURAN = 4;
padding = mod(UKURAN - mod(numel(teks), UKURAN), UKURAN);
lengkap = [teks, repmat(' ', 1, padding)];

blok = cell(1, numel(lengkap) / UKURAN);
for i = 1:numel(blok)
    blok{i} = lengkap((i - 1) * UKURAN + 1 : i * UKURAN);
end
end

% XOR dua blok karakter per karakter.
function hasil = tambah_xor(a, b)
hasil = a;
for i = 1:numel(a)
    hasil(i) = char(bitxor(double(a(i)), double(b(i))));
end
end

% Setiap blok dienkripsi sendiri-sendiri, tanpa kaitan antar blok.
function hasil = enkripsi_ecb(plainteks, kunci)
blok = bagi_blok(plainteks);
hasil = cell(1, numel(blok));
for i = 1:numel(blok)
    hasil{i} = kunci_putaran(blok{i}, kunci);
end
end

% Setiap blok di-XOR dengan cipherteks sebelumnya sebelum dienkripsi.
function hasil = enkripsi_cbc(plainteks, kunci, iv)
blok = bagi_blok(plainteks);
hasil = cell(1, numel(blok));
sebelumnya = iv;
for i = 1:numel(blok)
    blok_cipher = kunci_putaran(tambah_xor(blok{i}, sebelumnya), kunci);
    hasil{i} = blok_cipher;
    sebelumnya = blok_cipher;
end
end

% Tampilkan blok sebagai heksadesimal agar tiap byte terbaca jelas.
function teks = tampilkan_hex(blok)
teks = sprintf('%02X ', double(blok));
teks = strtrim(teks);
end
