#!/usr/bin/perl
# Menambahkan blok gambar dari build/figs.txt ke berkas bagian bab.
# Format berkas data: baris penanda "===FILE <path>" lalu isi blok sampai
# penanda berikutnya. Blok di-append ke akhir berkas tujuan sehingga gambar
# berada di dalam seksi yang benar (gambar adalah float, jadi posisi di
# sumber hanya menentukan keanggotaan seksi).
use strict;
use warnings;

my $data = shift @ARGV or die "pakai: perl insert_figures.pl <berkas-data>\n";
open my $fh, '<:raw', $data or die "tidak bisa buka $data: $!\n";
my @L = <$fh>;
close $fh;
s/\r\n/\n/ for @L;

my %blok;
my @urut;
my $tujuan;
for my $ln (@L) {
    if ($ln =~ /^===FILE\s+(\S+)\s*$/) {
        $tujuan = $1;
        push @urut, $tujuan unless exists $blok{$tujuan};
        $blok{$tujuan} = '';
    } elsif (defined $tujuan) {
        $blok{$tujuan} .= $ln;
    }
}

my $jumlah = 0;
for my $path (@urut) {
    die "berkas tujuan tidak ada: $path\n" unless -f $path;
    my $isi = $blok{$path};
    $isi =~ s/\s+\z/\n/;          # rapikan akhir blok
    open my $out, '>>:raw', $path or die "tidak bisa tulis $path: $!\n";
    print {$out} "\n", $isi;
    close $out;
    my $n = () = $isi =~ /\\begin\{figure\}/g;
    $jumlah += $n;
    printf "OK  %-34s +%d gambar\n", $path, $n;
}
print "total $jumlah blok gambar disisipkan ke ", scalar(@urut), " berkas\n";
