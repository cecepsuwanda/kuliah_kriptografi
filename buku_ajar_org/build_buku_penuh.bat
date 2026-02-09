@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

set "MAIN=buku_kriptografi"
set "OUTDIR=output"

echo ============================================
echo   Kompilasi Buku Ajar Kriptografi (Utuh)
echo ============================================
echo.

if not exist "%OUTDIR%" mkdir "%OUTDIR%"

echo [1/4] pdflatex tahap pertama...
pdflatex -interaction=nonstopmode "%MAIN%.tex" >nul 2>&1
if %errorlevel% neq 0 (
    echo GAGAL. Jalankan untuk melihat pesan:
    echo   pdflatex -interaction=nonstopmode %MAIN%.tex
    type "%MAIN%.log" 2>nul | findstr /i "error !"
    exit /b 1
)

echo [2/4] BibTeX...
bibtex "%MAIN%" >nul 2>&1
if %errorlevel% neq 0 (
    echo Peringatan: BibTeX gagal. Lihat %MAIN%.blg
    bibtex "%MAIN%" 2>&1
    exit /b 1
)

echo [3/4] pdflatex tahap kedua (TOC, referensi)...
pdflatex -interaction=nonstopmode "%MAIN%.tex" >nul 2>&1
if %errorlevel% neq 0 (
    echo GAGAL tahap kedua.
    exit /b 1
)

echo [4/4] pdflatex tahap ketiga (final)...
pdflatex -interaction=nonstopmode "%MAIN%.tex" >nul 2>&1
if %errorlevel% neq 0 (
    echo GAGAL tahap ketiga.
    exit /b 1
)

if not exist "%MAIN%.pdf" (
    echo GAGAL: PDF tidak dihasilkan.
    exit /b 1
)

echo.
echo Berhasil. Membersihkan file sampingan...

del /q "%MAIN%.aux" 2>nul
del /q "%MAIN%.out" 2>nul
del /q "%MAIN%.toc" 2>nul
del /q "%MAIN%.lof" 2>nul
del /q "%MAIN%.lot" 2>nul
del /q "%MAIN%.synctex.gz" 2>nul
del /q "%MAIN%.bbl" 2>nul
del /q "%MAIN%.blg" 2>nul
for /r chapters %%f in (*.aux) do del /q "%%f" 2>nul

move /y "%MAIN%.pdf" "%OUTDIR%\" >nul
echo PDF: %OUTDIR%\%MAIN%.pdf
echo Log: %MAIN%.log (dipertahankan)
echo.
echo ============================================
echo   Selesai. %OUTDIR%\%MAIN%.pdf
echo ============================================
exit /b 0
