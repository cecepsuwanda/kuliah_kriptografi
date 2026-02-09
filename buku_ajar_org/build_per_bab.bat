@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
cd /d "%~dp0"

set "OUTDIR=output"
set "CHAPLIST=chap01_pengantar chap02_aritmetika chap03_euclid chap04_teori_bilangan chap05_caesar chap06_vigenere chap07_block_cipher chap08_rsa chap09_hash chap10_tanda_tangan chap11_protokol chap12_manajemen_kunci chap13_kriptanalisis chap14_implementasi"
set "total=14"
set "n=0"

:: Opsi: satu bab saja, misalnya build_per_bab.bat chap03_euclid
if not "%~1"=="" (
    set "CHAPLIST=%~1"
    set "total=1"
)

:: Pastikan pdflatex ada di PATH
where pdflatex >nul 2>&1
if errorlevel 1 (
    echo ERROR: pdflatex tidak ditemukan. Pastikan MiKTeX/TeX Live ada di PATH.
    exit /b 1
)

echo ============================================
echo   Kompilasi Buku Ajar (Per Bab)
echo ============================================
echo.

if not exist "%OUTDIR%" mkdir "%OUTDIR%"

pushd chapters 2>nul
if errorlevel 1 (
    echo ERROR: Folder chapters tidak ditemukan.
    exit /b 1
)

for %%c in (%CHAPLIST%) do (
    set /a n+=1
    set "chap=%%c"
    set "num=00!n!"
    set "num=!num:~-2!"
    if "!total!"=="1" set "num=!chap:~3,2!"

    echo.
    echo [Bab !n!/%total%] %%c
    echo   [1/4] pdflatex...
    pdflatex -interaction=nonstopmode "%%c.tex" > "..\%OUTDIR%\%%c_step1.log" 2>&1
    if not exist "%%c.pdf" (
        echo   ERROR: Tahap pertama gagal. Lihat %OUTDIR%\%%c_step1.log
        goto :err
    )

    echo   [2/4] BibTeX...
    if exist "%%c.aux" (
        bibtex "%%c" > "..\%OUTDIR%\%%c_bibtex.log" 2>&1
    )

    echo   [3/4] pdflatex run 2...
    pdflatex -interaction=nonstopmode "%%c.tex" > "..\%OUTDIR%\%%c_step2.log" 2>&1
    echo   [4/4] pdflatex run 3...
    pdflatex -interaction=nonstopmode "%%c.tex" > "..\%OUTDIR%\%%c_step3.log" 2>&1

    if not exist "%%c.pdf" (
        echo   ERROR: PDF tidak dihasilkan.
        goto :err
    )
    move /y "%%c.pdf" "..\%OUTDIR%\bab!num!_%%c.pdf" >nul
    echo   OK: %OUTDIR%\bab!num!_%%c.pdf
)

popd
echo.
echo Membersihkan file sampingan di chapters...
for /r chapters %%f in (*.aux) do del /q "%%f" 2>nul
for /r chapters %%f in (*.out) do del /q "%%f" 2>nul
for /r chapters %%f in (*.toc) do del /q "%%f" 2>nul
for /r chapters %%f in (*.bbl) do del /q "%%f" 2>nul
for /r chapters %%f in (*.blg) do del /q "%%f" 2>nul
for /r chapters %%f in (*.synctex.gz) do del /q "%%f" 2>nul
echo.
echo ============================================
echo   Selesai. %total% bab di %OUTDIR%\
echo ============================================
exit /b 0

:err
popd
echo.
echo ============================================
echo   PROSES DIHENTIKAN KARENA ERROR
echo ============================================
exit /b 1
