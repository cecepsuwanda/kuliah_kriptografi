% Stream cipher sederhana berbasis XOR dan demonstrasi efek bit-flip.
% Bab 5, Aktivitas 5.1.
%
% Jalankan: stream_cipher   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

plainteks = 'KRIPTO';
kunci = 'RAHASI';          % panjang kunci harus sama dengan panjang pesan

if numel(kunci) ~= numel(plainteks)
    error('Panjang kunci harus sama dengan panjang plainteks');
end

biner_plainteks = ke_biner(plainteks);
biner_kunci = ke_biner(kunci);

% Enkripsi dan dekripsi adalah operasi yang sama: XOR dengan kunci.
cipherteks = xor_biner(biner_plainteks, biner_kunci);
hasil_dekripsi = dari_biner(xor_biner(cipherteks, biner_kunci));

fprintf('Plainteks      : %s\n', plainteks);
fprintf('Kunci          : %s\n', kunci);
fprintf('Biner plainteks: %s\n', biner_plainteks);
fprintf('Biner kunci    : %s\n', biner_kunci);
fprintf('Biner cipher   : %s\n', cipherteks);
fprintf('Dekripsi       : %s\n\n', hasil_dekripsi);

% Ubah bit pertama cipherteks, lalu dekripsi kembali.
cipherteks_rusak = cipherteks;
if cipherteks_rusak(1) == '0'
    cipherteks_rusak(1) = '1';
else
    cipherteks_rusak(1) = '0';
end
hasil_rusak = dari_biner(xor_biner(cipherteks_rusak, biner_kunci));

fprintf('Cipherteks dengan bit pertama dibalik: %s\n', cipherteks_rusak);
fprintf('Hasil dekripsinya                   : %s\n\n', hasil_rusak);
fprintf('Perhatikan bahwa satu bit yang berubah hanya merusak satu karakter.\n');
fprintf('Pada mode operasi seperti CBC, kesalahan itu menjalar ke blok berikutnya.\n');

% --- Fungsi lokal -----------------------------------------------------------

% Ubah teks menjadi string biner 8 bit per karakter.
function biner = ke_biner(teks)
biner = '';
for i = 1:numel(teks)
    biner = [biner, dec2bin(double(teks(i)), 8)];
end
end

% Ubah string biner (kelipatan 8 bit) kembali menjadi teks.
function teks = dari_biner(biner)
if mod(numel(biner), 8) ~= 0
    error('Panjang string biner harus kelipatan 8');
end
teks = '';
for i = 1:8:numel(biner)
    teks = [teks, char(bin2dec(biner(i:i + 7)))];
end
end

% XOR dua string biner dengan panjang sama.
function hasil = xor_biner(a, b)
if numel(a) ~= numel(b)
    error('Panjang kedua string biner harus sama');
end
hasil = a;
for i = 1:numel(a)
    if a(i) == b(i)
        hasil(i) = '0';
    else
        hasil(i) = '1';
    end
end
end
