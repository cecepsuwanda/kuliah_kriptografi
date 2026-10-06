% Pertukaran kunci Diffie-Hellman pada bilangan kecil.
% Bab 11, Aktivitas 11.1 dan Contoh Terhitung Bab 11.
%
% Jalankan: diffie_hellman   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

jalankan_dh(11, 7, 6, 9, ...
    'Contoh Terhitung Bab 11 (1): p = 11, g = 7, a = 6, b = 9');

jalankan_dh(353, 3, 97, 233, ...
    'Aktivitas 11.1: p = 353, g = 3, a = 97, b = 233');

fprintf('Catatan keamanan:\n');
fprintf('Semua nilai yang dipertukarkan (p, g, A, B) bersifat publik. Penyerang\n');
fprintf('yang menyadapnya harus mencari a atau b dari A = g^a mod p, yaitu\n');
fprintf('persoalan logaritma diskret. Untuk p = 353 persoalan itu dapat\n');
fprintf('diselesaikan seketika; untuk p berukuran 2048 bit atau lebih, cara\n');
fprintf('terbaik yang diketahui tetap tidak praktis. Karena itu p harus prima\n');
fprintf('dan g harus akar primitif, supaya rentang nilai g^x mencakup seluruh\n');
fprintf('grup dan tidak menyisakan celah yang mempermudah penyerangan.\n');

% --- Fungsi lokal -----------------------------------------------------------

% Jalankan satu pertukaran lengkap dan cetak setiap langkahnya.
function jalankan_dh(p, g, a, b, catatan)
fprintf('%s\n', repmat('=', 1, 68));
fprintf('%s\n', catatan);
fprintf('%s\n', repmat('=', 1, 68));

if ~akar_primitif(g, p)
    fprintf('PERINGATAN: %d bukan akar primitif dari %d\n', g, p);
    return
end

A = pangkat_mod(g, a, p);
B = pangkat_mod(g, b, p);
K_alice = pangkat_mod(B, a, p);
K_bob = pangkat_mod(A, b, p);

fprintf('Parameter publik : p = %d, g = %d  (g akar primitif dari p)\n', p, g);
fprintf('Kunci privat Alice a = %d\n', a);
fprintf('Kunci privat Bob   b = %d\n\n', b);
fprintf('Alice -> A = g^a mod p = %d^%d mod %d = %d\n', g, a, p, A);
fprintf('Bob   -> B = g^b mod p = %d^%d mod %d = %d\n\n', g, b, p, B);
fprintf('Alice menghitung K = B^a mod p = %d^%d mod %d = %d\n', B, a, p, K_alice);
fprintf('Bob   menghitung K = A^b mod p = %d^%d mod %d = %d\n', A, b, p, K_bob);
fprintf('Kedua kunci rahasia sama: %d (K = %d)\n\n', K_alice == K_bob, K_alice);
end

% Periksa apakah g membangkitkan seluruh 1..p-1 modulo p.
% Pangkat g^1, g^2, ... harus menghasilkan (p-1) nilai berbeda sebelum kembali
% ke 1. Cara memeriksa langsung ini hanya terjangkau untuk p kecil.
function benar = akar_primitif(g, p)
pernah = false(1, p);
pangkat = 1;
jumlah = 0;
for i = 1:p - 1
    pangkat = mod(pangkat * g, p);
    if ~pernah(pangkat)
        pernah(pangkat) = true;
        jumlah = jumlah + 1;
    end
end
benar = (jumlah == p - 1);
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
