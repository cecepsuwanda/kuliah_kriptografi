% ElGamal: pembangkitan kunci, enkripsi, dan dekripsi pada bilangan kecil.
% Bab 12, Aktivitas 12.1 dan Contoh Terhitung Bab 12.
%
% Jalankan: elgamal   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

jalankan_elgamal(2273, 3, 243, 700, 1463, ...
    'Contoh Terhitung Bab 12: p = 2273, g = 3, x = 243');

jalankan_elgamal(2357, 2, 1751, 2035, 1520, ...
    'Aktivitas 12.1: p = 2357, g = 2, x = 1751');

fprintf('Catatan keamanan:\n');
fprintf('Ukuran cipherteks ElGamal dua kali ukuran plainteks, karena tiap\n');
fprintf('pesan menghasilkan pasangan (a, b). Keamanannya bersandar pada\n');
fprintf('persoalan logaritma diskret: penyerang yang melihat y, g, dan p\n');
fprintf('harus mencari x. Selain itu, k harus dipilih acak dan tidak boleh\n');
fprintf('digunakan ulang; memakai k yang sama untuk dua pesan membuat rasio\n');
fprintf('kedua cipherteks membuka perbandingan plainteksnya.\n');

% --- Fungsi lokal -----------------------------------------------------------

% Jalankan satu siklus ElGamal lengkap dan cetak setiap langkahnya.
function jalankan_elgamal(p, g, x, m, k, catatan)
fprintf('%s\n', repmat('=', 1, 68));
fprintf('%s\n', catatan);
fprintf('%s\n', repmat('=', 1, 68));

if m < 0 || m >= p
    error('Pesan m harus berada pada selang [0, p-1]');
end

y = pangkat_mod(g, x, p);            % kunci publik
a = pangkat_mod(g, k, p);            % a = g^k mod p
b = mod(pangkat_mod(y, k, p) * m, p); % b = y^k * m mod p
m_pulih = dekripsi_elgamal(a, b, x, p);

fprintf('Parameter publik : p = %d, g = %d\n', p, g);
fprintf('Kunci privat Bob : x = %d\n', x);
fprintf('Kunci publik Bob : y = g^x mod p = %d^%d mod %d = %d\n\n', g, x, p, y);
fprintf('Pesan       m = %d\n', m);
fprintf('Kunci acak  k = %d\n', k);
fprintf('a = g^k mod p     = %d^%d mod %d = %d\n', g, k, p, a);
fprintf('b = y^k * m mod p = %d^%d * %d mod %d = %d\n', y, k, m, p, b);
fprintf('Cipherteks  (a, b) = (%d, %d)\n\n', a, b);
fprintf('Dekripsi m = b * (a^x)^-1 mod p = %d\n', m_pulih);
fprintf('Pesan pulih dengan tepat: %d\n\n', m_pulih == m);
end

% Dekripsi: m = b * (a^x)^-1 mod p.
% Invers a^x dihitung sebagai a^(p-1-x) mod p, karena a^(p-1) = 1 (mod p)
% menurut Teorema Kecil Fermat.
function m = dekripsi_elgamal(a, b, x, p)
invers_a_x = pangkat_mod(a, p - 1 - x, p);
m = mod(b * invers_a_x, p);
end

% Hitung basis^pangkat mod modulus dengan kuadrat berulang.
% Hasil kali terbesar adalah (modulus-1)^2, sehingga modulus harus lebih kecil
% dari akar 2^53 (sekitar 9,4 x 10^7) agar tetap tepat dalam bilangan
% berpresisi ganda.
function hasil = pangkat_mod(basis, pangkat, modulus)
hasil = 1;
basis = mod(basis, modulus);
while pangkat > 0
    if mod(pangkat, 2) == 1
        hasil = mod(hasil * basis, modulus);
    end
    basis = mod(basis * basis, modulus);
    pangkat = floor(pangkat / 2);
end
end
