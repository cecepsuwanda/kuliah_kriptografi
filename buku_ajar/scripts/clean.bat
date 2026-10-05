@echo off
REM =====================================================================
REM  scripts/clean.bat
REM  Menghapus berkas antara (aux, toc, lof, lot, log, dll.) dari buku_ajar
REM  dan dari buku_ajar\build.
REM
REM  Berkas yang SENGAJA dipertahankan:
REM    *.bib  - basis data pustaka (references.bib), sumber bibtex
REM    *.bbl  - hasil olahan bibtex, dipakai pdflatex untuk daftar pustaka
REM    *.blg  - log bibtex, untuk menelusuri entri/sitasi bermasalah
REM  Alasan sama dengan compile_main.bat: hasil bibliografi tetap tersimpan
REM  setelah build dan tidak perlu menjalankan bibtex lagi.
REM
REM  Pakai: scripts\clean.bat
REM =====================================================================

setlocal
set "SCRIPTS_DIR=%~dp0"
set "BOOK_DIR=%SCRIPTS_DIR%.."

echo Membersihkan berkas antara di "%BOOK_DIR%"...
call :bersihkan "%BOOK_DIR%"
call :bersihkan "%BOOK_DIR%\build"

echo Selesai.
exit /b 0

:bersihkan
if not exist "%~1" exit /b 0
pushd "%~1"
REM *.pdf tidak dihapus: berkas itu hasil akhir, bukan berkas antara.
for %%E in (aux toc lof lot lol out bcf fls fdb_latexmk nav snm vrb idx ilg ind acn acr alg glg glo gls ist xdy run.xml synctex pdfsync synctex.gz) do (
    del /s /q "*.%%E" >nul 2>&1
)
del /s /q "*.log" >nul 2>&1
popd
exit /b 0
