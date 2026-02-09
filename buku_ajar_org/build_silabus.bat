@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

set "DOC=silabus_kriptografi"
set "OUTDIR=output"

echo ============================================
echo   Kompilasi Silabus Kriptografi
echo ============================================
echo.

if not exist "%OUTDIR%" mkdir "%OUTDIR%"

echo [1/4] pdflatex tahap pertama...
pdflatex -interaction=nonstopmode "%DOC%.tex" >nul 2>&1
if %errorlevel% neq 0 (
    echo GAGAL. Lihat %DOC%.log
    pdflatex -interaction=nonstopmode "%DOC%.tex"
    exit /b 1
)

echo [2/4] BibTeX...
if exist "%DOC%.aux" (
    bibtex "%DOC%" >nul 2>&1
)

echo [3/4] pdflatex tahap kedua...
pdflatex -interaction=nonstopmode "%DOC%.tex" >nul 2>&1
echo [4/4] pdflatex tahap ketiga...
pdflatex -interaction=nonstopmode "%DOC%.tex" >nul 2>&1

if not exist "%DOC%.pdf" (
    echo GAGAL: PDF tidak dihasilkan.
    exit /b 1
)

move /y "%DOC%.pdf" "%OUTDIR%\" >nul
echo.
echo Berhasil: %OUTDIR%\%DOC%.pdf
echo.
echo ============================================
echo   Selesai. %OUTDIR%\%DOC%.pdf
echo ============================================
exit /b 0
