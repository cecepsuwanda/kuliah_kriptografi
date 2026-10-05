@echo off
REM =====================================================================
REM  scripts/build-all.bat
REM  Membangun seluruh buku (front matter + 16 bab + back matter + daftar
REM  pustaka) dari buku_ajar/main.tex.
REM
REM  Skrip ini sengaja hanya meneruskan ke compile_main.bat di akar
REM  repositori, agar logika build tidak diduplikasi (Aturan AI #2). Lokasi
REM  berkas tetap di scripts/ sesuai Arsitektur_Buku_Ajar.md Bagian 3.
REM
REM  Pakai: scripts\build-all.bat
REM =====================================================================

setlocal
set "SCRIPTS_DIR=%~dp0"
set "ROOT_DIR=%SCRIPTS_DIR%..\.."

if not exist "%ROOT_DIR%\compile_main.bat" (
    echo ERROR: compile_main.bat tidak ditemukan di "%ROOT_DIR%".
    exit /b 1
)

call "%ROOT_DIR%\compile_main.bat"
exit /b %errorlevel%
