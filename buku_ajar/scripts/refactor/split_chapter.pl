#!/usr/bin/perl
# split_chapter.pl -- pecah satu berkas chapters/NN/chapter.tex menjadi
#   section-NN.tex, praktikum.tex, latihan.tex, evaluasi.tex,
#   contoh.tex, rangkuman.tex  + chapter.tex baru yang merangkai semuanya.
#
# Isi dipindahkan apa adanya (byte-for-byte); skrip ini tidak menulis ulang
# materi. Dipakai sekali saat refactor Tahap 1d.
#
# Kotak OBE ditarik dari posisi mana pun, bukan diasumsikan selalu di akhir
# bab: pada Bab 4 kotak `obeactivity` menyelip di tengah bagian pertama,
# jadi pendekatan "potong dari kotak OBE pertama" akan membuang bagian 2-5.
use strict;
use warnings;

my $file = shift or die "usage: split_chapter.pl chapters/NN/chapter.tex\n";
$file =~ m{^(.*)[/\\]chapter\.tex$} or die "nama berkas harus chapter.tex\n";
my $dir = $1;

open(my $fh, '<', $file) or die "buka $file: $!";
my @L = <$fh>;
close $fh;

my %dest = (
    obeactivity         => 'praktikum.tex',
    obereflection       => 'latihan.tex',
    obeassessment       => 'evaluasi.tex',
    competencychecklist => 'evaluasi.tex',
);
my %seen;

# --- 1. tarik setiap kotak OBE keluar dari aliran baris -------------------
my (%buf, @sisa);
my $env;
for my $ln (@L) {
    if (!defined $env
        && $ln =~ /^\\begin\{(obeactivity|obereflection|obeassessment|competencychecklist)\}\s*$/) {
        $env = $1;
        $seen{$env}++;
    }
    if (defined $env) {
        $buf{$dest{$env}} = '' unless defined $buf{$dest{$env}};
        $buf{$dest{$env}} .= $ln;
        undef $env if $ln =~ /^\\end\{\Q$env\E\}\s*$/;
    } else {
        push @sisa, $ln;
    }
}

for my $e (qw(obeactivity obereflection obeassessment competencychecklist)) {
    die "$file: kotak $e tidak ditemukan\n" unless $seen{$e};
    die "$file: kotak $e muncul lebih dari sekali\n" if $seen{$e} > 1;
}

# buang \end{document}; ditulis ulang di akhir chapter.tex
my $end_doc;
for my $i (0 .. $#sisa) {
    if ($sisa[$i] =~ /^\\end\{document\}/) { $end_doc = splice(@sisa, $i, 1); last }
}
die "$file: \\end{document} tidak ditemukan\n" unless defined $end_doc;

# --- 2. batas header / isi materi ----------------------------------------
my $body;
for my $i (0 .. $#sisa) {
    if ($sisa[$i] =~ /^\\section\{/) { $body = $i; last }
}
die "$file: tidak ada \\section\n" unless defined $body;
die "$file: \\begin{learningoutcome} tidak ikut di header\n"
    unless grep { /^\\begin\{learningoutcome\}/ } @sisa[0 .. $body - 1];

my @header = @sisa[0 .. $body - 1];
my @isi    = @sisa[$body .. $#sisa];

# --- 3. pisahkan tiap \section menjadi section-NN.tex ---------------------
my @sec_name;
my $cur = -1;
for my $ln (@isi) {
    if ($ln =~ /^\\section\{/) {
        $cur++;
        push @sec_name, sprintf('section-%02d', $cur + 1);
        open(my $o, '>', "$dir/$sec_name[-1].tex") or die "$dir/$sec_name[-1].tex: $!";
        print $o $ln;
        close $o;
    } else {
        die "$file: baris sebelum \\section pertama\n" if $cur < 0;
        open(my $o, '>>', "$dir/$sec_name[-1].tex") or die "append: $!";
        print $o $ln;
        close $o;
    }
}

# --- 4. tulis berkas komponen kotak OBE ----------------------------------
for my $k (keys %buf) {
    open(my $o, '>', "$dir/$k") or die "$dir/$k: $!";
    print $o "\n", $buf{$k};
    close $o;
}

# --- 5. komponen yang masih kosong (diisi pada Tahap 5) -------------------
for my $k (qw(contoh.tex rangkuman.tex)) {
    next if -e "$dir/$k";
    open(my $o, '>', "$dir/$k") or die "$dir/$k: $!";
    close $o;
}

# --- 6. tulis chapter.tex yang baru --------------------------------------
open(my $o, '>', $file) or die "tulis $file: $!";
print $o @header;
print $o "\\subfile{$_}\n" for @sec_name;
print $o "\\input{contoh}\n";
print $o "\\input{praktikum}\n";
print $o "\\input{latihan}\n";
print $o "\\input{rangkuman}\n";
print $o "\\input{evaluasi}\n";
print $o "\n";
print $o $end_doc;
close $o;

printf "%-14s %d bagian: %s\n", $dir, scalar(@sec_name), join(' ', @sec_name);
