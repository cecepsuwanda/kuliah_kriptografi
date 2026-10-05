@echo off
REM =====================================================================
REM  scripts/build-chapter.bat
REM  Mengompilasi SATU bab secara mandiri, tanpa master main.tex.
REM  Ini yang membuktikan Aturan AI #4: setiap bab harus bisa dikompilasi
REM  sendiri (berkat \documentclass[../../main.tex]{subfiles} di chapter.tex).
REM
REM  Pakai: scripts\build-chapter.bat NN      contoh: scripts\build-chapter.bat 07
REM
REM  Hasil: buku_ajar\build\bab-NN.pdf
REM
REM  Catatan: daftar pustaka dirakit oleh main.tex, jadi pada kompilasi
REM  mandiri ini sitasi tampil sebagai tanda tanya. Itu wajar -- yang diuji
REM  di sini adalah bahwa berkas bab beserta preamble dan gambarnya dapat
REM  diproses tanpa error.
REM =====================================================================

setlocal
set "SCRIPTS_DIR=%~dp0"
set "BOOK_DIR=%SCRIPTS_DIR%.."

if "%~1"=="" goto :pakai

set "NN=%~1"
set "CHAPTER_DIR=%BOOK_DIR%\chapters\%NN%"
set "BUILD_DIR=%BOOK_DIR%\build"

if not exist "%CHAPTER_DIR%\chapter.tex" (
    echo ERROR: bab "%NN%" tidak ditemukan.
    echo        Dicari di: "%CHAPTER_DIR%\chapter.tex"
    exit /b 1
)

if not exist "%BUILD_DIR%" mkdir "%BUILD_DIR%"

echo ============================================================
echo  Kompilasi mandiri bab %NN%
echo ============================================================

pushd "%CHAPTER_DIR%"

echo Tahap 1/2: pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="%BUILD_DIR%" -jobname="bab-%NN%" chapter.tex
if errorlevel 1 goto :gagal

echo Tahap 2/2: pdflatex (menstabilkan referensi silang)...
pdflatex -interaction=nonstopmode -output-directory="%BUILD_DIR%" -jobname="bab-%NN%" chapter.tex

popd
echo.
echo Selesai. Hasil: "%BUILD_DIR%\bab-%NN%.pdf"
echo Periksa "%BUILD_DIR%\bab-%NN%.log" bila ada warning yang perlu ditindak.
exit /b 0

:gagal
popd
echo.
echo ERROR: kompilasi bab %NN% gagal. Lihat "%BUILD_DIR%\bab-%NN%.log".
exit /b 1

:pakai
echo Pakai: %~nx0 NN      contoh: %~nx0 07
exit /b 1
