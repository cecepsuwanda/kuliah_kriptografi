@echo off
setlocal enabledelayedexpansion

REM ====================================================================
REM  compile-ppt.bat -- kompilasi slide minggu-*.tex di folder ini
REM
REM  Pemakaian:  compile-ppt.bat            (semua deck)
REM              compile-ppt.bat 05         (hanya minggu-05)
REM
REM  Tiap deck dikompilasi DUA kali agar \inserttotalframenumber
REM  (nomor halaman "n / N") stabil. Hasil: minggu-NN.pdf.
REM
REM  Perhatikan: TIDAK memakai "goto" di dalam blok for, sebab goto
REM  keluar dari loop dan hanya berkas pertama yang akan diproses.
REM ====================================================================

set "PPT_DIR=%~dp0"
pushd "%PPT_DIR%"

where pdflatex >nul 2>nul
if errorlevel 1 (
    echo ERROR: pdflatex tidak ditemukan. Pastikan MiKTeX/TeX Live terpasang dan ada di PATH.
    popd
    exit /b 1
)

set "FILTER=%~1"
if "%FILTER%"=="" set "FILTER=*"

set "GAGAL=0"
set "JUMLAH=0"

for %%F in (minggu-%FILTER%.tex) do (
    set "BASE=%%~nF"
    set /a JUMLAH+=1

    echo ============================================================
    echo Mengompilasi !BASE!.tex
    echo ============================================================

    set "OK=1"
    pdflatex -interaction=nonstopmode -halt-on-error "!BASE!.tex" >nul 2>&1
    if errorlevel 1 set "OK=0"
    if "!OK!"=="1" (
        pdflatex -interaction=nonstopmode -halt-on-error "!BASE!.tex" >nul 2>&1
        if errorlevel 1 set "OK=0"
    )

    if "!OK!"=="1" (
        set "PERINGATAN=0"
        for /f %%C in ('findstr /r /c:"^!" /c:"Overfull" /c:"Underfull" /c:"LaTeX Warning" "!BASE!.log" 2^>nul ^| find /c /v ""') do set "PERINGATAN=%%C"
        echo   selesai: !BASE!.pdf   ^(peringatan: !PERINGATAN!^)
        for %%E in (aux nav out snm toc lof lot vrb synctex.gz) do (
            if exist "!BASE!.%%E" del /q "!BASE!.%%E" 2>nul
        )
    ) else (
        echo   GAGAL -- periksa !BASE!.log
        set "GAGAL=1"
    )
)

echo.
echo ============================================================
if "%JUMLAH%"=="0" echo Tidak ada berkas yang cocok dengan pola "minggu-%FILTER%.tex".
if "%GAGAL%"=="1" (
    echo SELESAI DENGAN KEGAGALAN. Periksa log yang ditandai GAGAL di atas.
) else (
    echo SELESAI. %JUMLAH% deck berhasil dikompilasi.
)
echo ============================================================

popd
exit /b %GAGAL%
