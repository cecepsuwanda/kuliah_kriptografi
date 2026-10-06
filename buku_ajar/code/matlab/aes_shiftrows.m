% Simulasi tahap ShiftRows pada matriks state AES.
% Bab 8, Aktivitas 8.1.
%
% Blok 16 byte dipetakan ke matriks state 4 x 4, lalu baris ke-r digeser
% siklik ke kiri sejauh r byte (baris 0 tetap, baris 1 geser 1 byte, baris 2
% geser 2 byte, baris 3 geser 3 byte).
%
% Jalankan: aes_shiftrows   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

BLOK = 'Kriptografi-AES!';  % tepat 16 byte, satu blok AES

% reshape mengisi matriks kolom demi kolom, sama seperti pemetaan state AES:
% byte ke-i masuk ke state(i mod 4, i div 4).
state_awal = reshape(uint8(BLOK), 4, 4);
state_geser = shift_rows(state_awal);
state_kembali = inv_shift_rows(state_geser);

fprintf('Blok plainteks : %s\n', BLOK);
fprintf('Panjang        : %d byte\n\n', numel(BLOK));

% Nomor byte 0..15, supaya perpindahan posisi mudah dilihat.
fprintf('Nomor byte pada state awal (sebelum ShiftRows):\n');
nomor = reshape(uint8(0:15), 4, 4);
for baris = 1:4
    fprintf('    %3d %3d %3d %3d\n', nomor(baris, :));
end
fprintf('\n');

tampilkan(state_awal, 'State awal (baris, kolom):');
tampilkan(state_geser, 'Setelah ShiftRows:');
tampilkan(state_kembali, 'Setelah InvShiftRows (kembali ke awal):');

fprintf('Baris 0 tidak bergeser, baris 1 bergeser 1 byte, baris 2 bergeser\n');
fprintf('2 byte, dan baris 3 bergeser 3 byte. Akibatnya byte-byte dari satu\n');
fprintf('kolom yang sama menyebar ke empat kolom berbeda. Inilah difusi:\n');
fprintf('perubahan satu byte cepat memengaruhi seluruh state pada putaran\n');
fprintf('berikutnya.\n\n');
fprintf('InvShiftRows mengembalikan susunan semula: %d\n', ...
        isequal(char(state_kembali(:))', BLOK));

% --- Fungsi lokal -----------------------------------------------------------

% Geser baris ke-r siklik ke kiri sejauh r byte.
function hasil = shift_rows(state)
hasil = state;
for baris = 1:4
    hasil(baris, :) = circshift(state(baris, :), [0, -(baris - 1)]);
end
end

% Kebalikan ShiftRows: geser baris ke-r siklik ke kanan sejauh r byte.
function hasil = inv_shift_rows(state)
hasil = state;
for baris = 1:4
    hasil(baris, :) = circshift(state(baris, :), [0, baris - 1]);
end
end

% Cetak matriks sebagai bilangan sekaligus karakternya.
function tampilkan(state, judul)
fprintf('%s\n', judul);
for baris = 1:4
    fprintf('    %3d %3d %3d %3d    %s\n', state(baris, :), ...
            char(state(baris, :)));
end
fprintf('\n');
end
