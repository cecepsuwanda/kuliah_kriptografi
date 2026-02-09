@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

if "%~1"=="" (
    echo Penggunaan: build.bat ^<target^>
    echo.
    echo Target:
    echo   penuh   - Kompilasi buku utuh (buku_kriptografi.pdf)
    echo   perbab  - Kompilasi 14 bab terpisah ke output\
    echo   silabus - Kompilasi silabus (silabus_kriptografi.pdf)
    echo   all     - Kompilasi penuh + perbab + silabus
    echo.
    exit /b 0
)

set "target=%~1"
if /i "%target%"=="penuh" (
    call build_buku_penuh.bat
    exit /b %errorlevel%
)
if /i "%target%"=="perbab" (
    call build_per_bab.bat
    exit /b %errorlevel%
)
if /i "%target%"=="silabus" (
    call build_silabus.bat
    exit /b %errorlevel%
)
if /i "%target%"=="all" (
    echo === Buku utuh ===
    call build_buku_penuh.bat
    if errorlevel 1 exit /b 1
    echo.
    echo === Per bab ===
    call build_per_bab.bat
    if errorlevel 1 exit /b 1
    echo.
    echo === Silabus ===
    call build_silabus.bat
    exit /b %errorlevel%
)

echo Opsi tidak dikenal: %target%
echo Gunakan: penuh, perbab, silabus, atau all
exit /b 1
