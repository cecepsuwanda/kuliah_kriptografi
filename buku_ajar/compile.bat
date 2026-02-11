@echo off
cd /d "c:\Matakuliah\kuliah_kriptografi\buku_ajar"
pdflatex main.tex
if %ERRORLEVEL% NEQ 0 (
    echo Compilation failed!
    pause
) else (
    echo Compilation successful!
    echo PDF generated: main.pdf
)
