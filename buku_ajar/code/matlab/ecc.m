% Penjumlahan dan penggandaan titik pada kurva eliptik.
% Bab 14, Aktivitas 14.1 dan Contoh Terhitung Bab 14.
%
% Kurva ditulis dalam bentuk umum y^2 = x^3 + a*x + b. Dua medan didukung:
% kurva atas bilangan real dan kurva atas medan berhingga modulo prima p.
% Titik di ketakhinggaan (unsur identitas) diwakili oleh tanda takhingga.
%
% Jalankan: ecc   (atau buka berkas ini lalu tekan Run)
% Berkas ini berupa skrip dengan fungsi lokal, sehingga memerlukan MATLAB
% R2016b atau lebih baru.

% --- Kurva atas bilangan real: contoh terhitung bab -------------------------
a_real = -3;
b_real = 3;
P = titik(1, 1);
Q = titik(-2, 1);
fprintf('Kurva y^2 = x^3 - 3x + 3\n');
fprintf('  P pada kurva: %d\n', pada_kurva_real(P, a_real, b_real));
fprintf('  Q pada kurva: %d\n', pada_kurva_real(Q, a_real, b_real));
cetak_real('P + Q', tambah_real(P, Q, a_real));
cetak_real('2P   ', gandakan_real(P, a_real));
fprintf('\n');

% --- Kurva dari Aktivitas 14.1 ----------------------------------------------
a_akt = 2;
b_akt = 4;
P2 = titik(2, 4);
Q2 = titik(0, 2);
fprintf('Kurva y^2 = x^3 + 2x + 4 (Aktivitas 14.1)\n');
cetak_real('P + Q', tambah_real(P2, Q2, a_akt));
cetak_real('2P   ', gandakan_real(P2, a_akt));
fprintf('\n');

% --- Kurva modulo prima 23 ---------------------------------------------------
a_mod = 1;
b_mod = 1;
p = 23;
Pm = titik(3, 10);
dua_p = gandakan_mod(Pm, a_mod, p);
tiga_p = tambah_mod(dua_p, Pm, a_mod, p);
fprintf('Kurva y^2 = x^3 + x + 1 (mod 23)\n');
fprintf('  P pada kurva: %d\n', pada_kurva_mod(Pm, a_mod, b_mod, p));
cetak_mod('2P    ', dua_p);
cetak_mod('3P    ', tiga_p);
fprintf('\n');

% --- Pertukaran kunci ECDH pada kurva yang sama ------------------------------
a_privat = 2;
b_privat = 3;
basis = titik(3, 10);
PA = kali_mod(a_privat, basis, a_mod, p);
PB = kali_mod(b_privat, basis, a_mod, p);
K_alice = kali_mod(a_privat, PB, a_mod, p);
K_bob = kali_mod(b_privat, PA, a_mod, p);
fprintf('Pertukaran kunci ECDH pada kurva yang sama\n');
fprintf('  Kunci privat Alice a = %d, publik A = aB\n', a_privat);
cetak_mod('A    ', PA);
fprintf('  Kunci privat Bob   b = %d, publik B = bB\n', b_privat);
cetak_mod('B    ', PB);
cetak_mod('a*(bB)', K_alice);
cetak_mod('b*(aB)', K_bob);
fprintf('  Kunci bersama sama: %d\n\n', sama_titik(K_alice, K_bob));
fprintf('Penyerang yang melihat B, PA, dan PB harus menyelesaikan ECDLP\n');
fprintf('untuk memperoleh a atau b. Dengan modulus 23 persoalan itu dapat\n');
fprintf('diselesaikan dengan mencoba seluruh kemungkinan; pada kurva nyata\n');
fprintf('modulusnya berukuran 256 bit atau lebih.\n');

% --- Fungsi lokal: titik ------------------------------------------------------

function P = titik(x, y)
P = struct('x', x, 'y', y, 'takhingga', false);
end

function P = tak_hingga()
P = struct('x', 0, 'y', 0, 'takhingga', true);
end

function benar = sama_titik(P, Q)
if P.takhingga && Q.takhingga
    benar = true;
elseif ~P.takhingga && ~Q.takhingga && P.x == Q.x && P.y == Q.y
    benar = true;
else
    benar = false;
end
end

% --- Fungsi lokal: kurva atas bilangan real -----------------------------------

function benar = pada_kurva_real(P, a, b)
if P.takhingga
    benar = true;
    return
end
benar = abs(P.y ^ 2 - (P.x ^ 3 + a * P.x + b)) < 1e-9;
end

% Hitung R = 2P dengan rumus penggandaan titik: m = (3x^2 + a) / (2y).
function R = gandakan_real(P, a)
if P.takhingga
    R = P;
    return
end
if abs(P.y) < 1e-9  % garis singgung tegak: hasilnya titik di ketakhinggaan
    R = tak_hingga();
    return
end
m = (3 * P.x ^ 2 + a) / (2 * P.y);
x3 = m ^ 2 - 2 * P.x;
y3 = m * (P.x - x3) - P.y;
R = titik(x3, y3);
end

% Hitung R = P + Q dengan rumus m = (y2 - y1) / (x2 - x1).
function R = tambah_real(P, Q, a)
if P.takhingga
    R = Q;
    return
end
if Q.takhingga
    R = P;
    return
end
if abs(P.x - Q.x) < 1e-9
    if abs(P.y + Q.y) < 1e-9
        R = tak_hingga();
    else
        R = gandakan_real(P, a);  % P == Q, pakai rumus penggandaan
    end
    return
end
m = (Q.y - P.y) / (Q.x - P.x);
x3 = m ^ 2 - P.x - Q.x;
y3 = m * (P.x - x3) - P.y;
R = titik(x3, y3);
end

% --- Fungsi lokal: kurva modulo prima p --------------------------------------

% Invers perkalian nilai modulo p dengan Algoritma Euclidean diperluas.
function d = invers_modulo(nilai, p)
lama_d = 0;
d = 1;
lama_p = p;
sisa = mod(nilai, p);
while sisa ~= 0
    hasil_bagi = floor(lama_p / sisa);
    d_baru = lama_d - hasil_bagi * d;
    sisa_baru = lama_p - hasil_bagi * sisa;
    lama_d = d;
    d = d_baru;
    lama_p = sisa;
    sisa = sisa_baru;
end
d = mod(lama_d, p);
end

function benar = pada_kurva_mod(P, a, b, p)
if P.takhingga
    benar = true;
    return
end
benar = mod(P.y ^ 2 - (P.x ^ 3 + a * P.x + b), p) == 0;
end

% Hitung R = 2P pada kurva modulo p.
function R = gandakan_mod(P, a, p)
if P.takhingga || mod(P.y, p) == 0
    R = tak_hingga();
    return
end
m = mod(mod(3 * P.x ^ 2 + a, p) * invers_modulo(mod(2 * P.y, p), p), p);
x3 = mod(m ^ 2 - 2 * P.x, p);
y3 = mod(m * (P.x - x3) - P.y, p);
R = titik(x3, y3);
end

% Hitung R = P + Q pada kurva modulo p.
function R = tambah_mod(P, Q, a, p)
if P.takhingga
    R = Q;
    return
end
if Q.takhingga
    R = P;
    return
end
if mod(P.x - Q.x, p) == 0
    if mod(P.y + Q.y, p) == 0
        R = tak_hingga();
    else
        R = gandakan_mod(P, a, p);
    end
    return
end
m = mod(mod(Q.y - P.y, p) * invers_modulo(mod(Q.x - P.x, p), p), p);
x3 = mod(m ^ 2 - P.x - Q.x, p);
y3 = mod(m * (P.x - x3) - P.y, p);
R = titik(x3, y3);
end

% Hitung k*P dengan metode double-and-add.
function R = kali_mod(k, P, a, p)
R = tak_hingga();
penambah = P;
while k > 0
    if mod(k, 2) == 1
        R = tambah_mod(R, penambah, a, p);
    end
    penambah = gandakan_mod(penambah, a, p);
    k = floor(k / 2);
end
end

% --- Fungsi lokal: penyajian hasil -------------------------------------------

function cetak_real(label, P)
if P.takhingga
    fprintf('  %s = O (titik di ketakhinggaan)\n', label);
else
    fprintf('  %s = (%.10g, %.10g)\n', label, P.x, P.y);
end
end

function cetak_mod(label, P)
if P.takhingga
    fprintf('  %s = O (titik di ketakhinggaan)\n', label);
else
    fprintf('  %s = (%d, %d)\n', label, P.x, P.y);
end
end
