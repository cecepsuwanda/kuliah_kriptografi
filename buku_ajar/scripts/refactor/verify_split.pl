use strict; use warnings;

my @skip_orig = (qr/^\\documentclass/, qr/^\\begin\{document\}/, qr/^\\end\{document\}/);
my @skip_new  = (@skip_orig, qr/^\\subfile\{/, qr/^\\input\{/);

# Berkas kerja memakai CRLF, blob git memakai LF: samakan sebelum dibandingkan.
sub norm { return sort grep { /\S/ } map { s/\r\n/\n/r } @_ }

my $bad = 0;
for my $n (qw(01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16)) {
    open(my $g, '-|', "git show HEAD:buku_ajar/chapters/$n/chapter.tex") or die "git: $!";
    my @orig = <$g>;
    close $g;
    @orig = grep { my $x = $_; !grep { $x =~ $_ } @skip_orig } @orig;

    my @new;
    for my $f (sort glob "chapters/$n/*.tex") {
        open(my $h, '<', $f) or die "$f: $!";
        my @c = <$h>;
        close $h;
        @c = grep { my $x = $_; !grep { $x =~ $_ } @skip_new } @c;
        push @new, @c;
    }

    my @a = norm(@orig);
    my @b = norm(@new);
    my $same = (@a == @b) && !grep { $a[$_] ne $b[$_] } 0 .. $#a;
    printf "ch%s  orig=%-4d baru=%-4d  %s\n", $n, scalar(@a), scalar(@b), $same ? "IDENTIK" : "!!! BEDA";
    $bad++ unless $same;
}
print $bad ? "\n$bad bab BERBEDA - materi ada yang hilang\n"
           : "\nSemua 16 bab identik: tidak ada materi yang hilang\n";
