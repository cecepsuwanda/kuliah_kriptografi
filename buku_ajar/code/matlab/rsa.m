% RSA: pembangkitan kunci, enkripsi, dan dekripsi dengan bilangan prima kecil.
% Bab 10, Aktivitas 10.1 dan Contoh Terhitung Bab 10.
%
% Jalankan: rsa   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

% Kasus 1: parameter kecil dari Aktivitas 10.1, dipakai untuk memeriksa
% setiap langkah secara manual tanpa alat bantu.
jalankan_rsa(3, 11, 3, 5, ...
    'Aktivitas 10.1: p = 3, q = 11, e = 3, m = 5');

% Kasus 2: parameter pada Contoh Terhitung Bab 10.
jalankan_rsa(47, 71, 79, 16, ...
    'Contoh Terhitung Bab 10: p = 47, q = 71, e = 79, m = 16');

fprintf('Catatan keamanan:\n');
fprintf('Pada kedua kasus di atas, n dapat difaktorkan hanya dalam hitungan\n');
fprintf('detik, sehingga kunci privat dapat ditemukan. RSA yang dipakai\n');
fprintf('sehari-hari menggunakan n minimal 2048 bit, yaitu sekitar 617\n');
fprintf('digit, yang membuat pemfaktoran menjadi tidak praktis.\n');

% --- Fungsi lokal -----------------------------------------------------------

% Jalankan satu siklus RSA lengkap dan cetak setiap langkahnya.
function jalankan_rsa(p, q, e, m, catatan)
fprintf('%s\n', repmat('=', 1, 68));
fprintf('%s\n', catatan);
fprintf('%s\n', repmat('=', 1, 68));

n = p * q;
phi = (p - 1) * (q - 1);
if ~(e > 1 && e < phi) || pbb(e, phi) ~= 1
    error('e harus memenuhi 1 < e < phi(n) dan PBB(e, phi(n)) = 1');
end
d = invers_modulo(e, phi);

c = pangkat_mod(m, e, n);       % enkripsi
m_pulih = pangkat_mod(c, d, n); % dekripsi

fprintf('p = %d, q = %d\n', p, q);
fprintf('n = p * q           = %d\n', n);
fprintf('phi(n) = (p-1)(q-1) = %d\n', phi);
fprintf('Kunci publik  (e, n) = (%d, %d)\n', e, n);
fprintf('Kunci privat  (d, n) = (%d, %d)\n', d, n);
fprintf('Periksa e * d mod phi(n) = %d\n\n', mod(e * d, phi));
fprintf('Plainteks  m = %d\n', m);
fprintf('Enkripsi   c = m^e mod n = %d^%d mod %d = %d\n', m, e, n, c);
fprintf('Dekripsi   m = c^d mod n = %d^%d mod %d = %d\n', c, d, n, m_pulih);
fprintf('Pesan pulih dengan tepat: %d\n\n', m_pulih == m);
end

% Pembagi bersama terbesar dengan Algoritma Euclidean.
function g = pbb(a, b)
while b ~= 0
    sisa = mod(a, b);
    a = b;
    b = sisa;
end
g = a;
end

% Cari d sehingga e * d = 1 (mod phi) dengan Algoritma Euclidean diperluas.
function d = invers_modulo(e, phi)
lama_d = 0;
d = 1;
lama_phi = phi;
sisa = e;
while sisa ~= 0
    hasil_bagi = floor(lama_phi / sisa);
    d_baru = lama_d - hasil_bagi * d;
    sisa_baru = lama_phi - hasil_bagi * sisa;
    lama_d = d;
    d = d_baru;
    lama_phi = sisa;
    sisa = sisa_baru;
end
if lama_phi ~= 1
    error('e tidak relatif prima terhadap phi(n); invers tidak ada');
end
d = mod(lama_d, phi);
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
