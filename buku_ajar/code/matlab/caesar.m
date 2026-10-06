% Cipher Caesar: enkripsi, dekripsi, dan pemecahan dengan analisis frekuensi.
% Bab 4, Aktivitas 4.1.
%
% Jalankan: caesar   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

plainteks = 'KRIPTOGRAFI ADALAH ILMU DAN SENI MENJAGA KEAMANAN PESAN';
kunci = 3;

cipherteks = caesar_enkripsi(plainteks, kunci);

fprintf('Plainteks : %s\n', plainteks);
fprintf('Kunci     : %d\n', kunci);
fprintf('Cipherteks: %s\n', cipherteks);
fprintf('Dekripsi  : %s\n\n', caesar_dekripsi(cipherteks, kunci));

[huruf, jumlah] = caesar_frekuensi(cipherteks);
fprintf('Frekuensi huruf cipherteks (10 teratas):\n');
dicetak = 0;
for i = 1:numel(huruf)
    if jumlah(i) > 0 && dicetak < 10
        fprintf('  %s: %d\n', huruf(i), jumlah(i));
        dicetak = dicetak + 1;
    end
end

[kunci_tebakan, hasil] = caesar_pecahkan(cipherteks);
fprintf('\nKunci hasil analisis frekuensi: %d\n', kunci_tebakan);
fprintf('Hasil pemecahan              : %s\n', hasil);

% --- Fungsi lokal -----------------------------------------------------------

% Geser setiap huruf sejauh k posisi (Caesar cipher).
function hasil = caesar_enkripsi(plainteks, k)
ABJAD = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
hasil = plainteks;
for i = 1:numel(plainteks)
    huruf = upper(plainteks(i));
    posisi = find(ABJAD == huruf, 1);
    if isempty(posisi)
        hasil(i) = huruf;  % spasi dan tanda baca tidak diubah
    else
        geser = mod(posisi - 1 + k, 26) + 1;
        hasil(i) = ABJAD(geser);
    end
end
end

% Kebalikan enkripsi: geser balik sejauh k posisi.
function hasil = caesar_dekripsi(cipherteks, k)
hasil = caesar_enkripsi(cipherteks, -k);
end

% Pasangan (huruf, jumlah) terurut dari yang paling sering muncul.
function [huruf, jumlah] = caesar_frekuensi(teks)
ABJAD = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
hitung = zeros(1, 26);
for i = 1:numel(teks)
    posisi = find(ABJAD == upper(teks(i)), 1);
    if ~isempty(posisi)
        hitung(posisi) = hitung(posisi) + 1;
    end
end
[jumlah, urut] = sort(hitung, 'descend');
huruf = ABJAD(urut);
end

% Tebak kunci dengan menyelaraskan huruf tersering ke urutan huruf bahasa.
function [tebakan_kunci, hasil] = caesar_pecahkan(cipherteks)
ABJAD = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
URUTAN_BAHASA = 'AENIRSTUDKMLGBOPWYHFCJZVXQ';

hitung = zeros(1, 26);
for i = 1:numel(cipherteks)
    posisi = find(ABJAD == upper(cipherteks(i)), 1);
    if ~isempty(posisi)
        hitung(posisi) = hitung(posisi) + 1;
    end
end
[~, urut] = sort(hitung, 'descend');
if hitung(urut(1)) == 0
    tebakan_kunci = -1;  % tidak ada huruf yang bisa dianalisis
    hasil = cipherteks;
    return
end
posisi_tertinggi = urut(1);  % indeks huruf tersering di dalam ABJAD
posisi_bahasa = find(ABJAD == URUTAN_BAHASA(1), 1);
tebakan_kunci = mod(posisi_tertinggi - posisi_bahasa, 26);
hasil = caesar_dekripsi(cipherteks, tebakan_kunci);
end
