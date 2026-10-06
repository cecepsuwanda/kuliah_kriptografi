% Perhitungan waktu brute force DES, Double DES, Triple DES, dan AES.
% Bab 7, Aktivitas 7.1.
%
% Karena 2^128 dan 2^256 jauh melampaui jangkauan bilangan bulat biasa,
% perhitungan dilakukan pada skala logaritma: log10(detik) = bit * log10(2).
% Hasil akhirnya ditampilkan dalam satuan waktu yang mudah dibaca.
%
% Jalankan: kompleksitas_kunci   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

KECEPATAN_LOG10 = 9;  % 10^9 kunci per detik

% (nama, panjang kunci, panjang efektif, ruang kunci efektif)
% Panjang efektif inilah yang menentukan waktu pencarian: Double DES hanya
% menyisakan 2^57 karena serangan meet-in-the-middle (Bab 7 bagian 3),
% sedangkan Triple DES dua kunci menyisakan 2^112.
nama    = {'DES', 'Double DES', 'Triple DES', 'AES-128', 'AES-256'};
panjang = [56, 112, 168, 128, 256];
efektif = [56, 57, 112, 128, 256];
ruang   = {'2^56', '2^57 efektif', '2^112 efektif', '2^128', '2^256'};

fprintf('Asumsi kecepatan penyerang: 1,000,000,000 kunci per detik\n\n');
fprintf('%-13s%-8s%-18s%s\n', 'Algoritma', 'Kunci', 'Ruang kunci', 'Waktu');
fprintf('%s\n', repmat('-', 1, 70));

for i = 1:numel(nama)
    detik_log10 = efektif(i) * log10(2) - KECEPATAN_LOG10;
    label_kunci = sprintf('%d bit', panjang(i));
    fprintf('%-13s%-8s%-18s%s\n', nama{i}, label_kunci, ruang{i}, ...
            ke_satuan_manusiawi(detik_log10));
end

fprintf('\nCatatan: Double DES hanya menambah satu bit keamanan efektif (2^57, bukan 2^112)\n');
fprintf('karena serangan meet-in-the-middle. Karena itu, memperpanjang kunci (AES-128)\n');
fprintf('jauh lebih efektif daripada mengulang algoritma yang sama.\n');

% --- Fungsi lokal -----------------------------------------------------------

% Ubah log10(detik) menjadi satuan waktu yang mudah dibaca manusia.
function teks = ke_satuan_manusiawi(detik_log10)
% Tiap langkah: bagi nilai dengan faktor, lalu satuan berganti ke nama berikut.
faktor = [log10(60), log10(60), log10(24), log10(365.25), ...
          log10(1000), log10(1000), log10(1000)];
satuan = {'menit', 'jam', 'hari', 'tahun', 'ribu tahun', ...
          'juta tahun', 'miliar tahun'};

nilai = detik_log10;
nama = 'detik';
for i = 1:numel(faktor)
    if nilai < faktor(i)
        teks = sprintf('%.2f %s', 10 ^ nilai, nama);
        return
    end
    nilai = nilai - faktor(i);
    nama = satuan{i};
end
teks = sprintf('%.2e %s', 10 ^ nilai, nama);
end
