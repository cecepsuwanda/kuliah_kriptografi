@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "SOURCE_DIR=%ROOT_DIR%rps_silabus"
set "OUTPUT_DIR=%ROOT_DIR%output"
set "TEX_FILE=silabus_kriptografi.tex"
set "PDF_NAME=silabus_kriptografi"
set "JOBNAME=silabus_build"
set "EXIT_CODE=0"

echo ============================================================
echo Compiling %TEX_FILE%
echo ============================================================
echo Jika %PDF_NAME%.pdf terbuka di viewer, tutup dulu agar bisa ditimpa.
echo.

if not exist "%SOURCE_DIR%\%TEX_FILE%" (
    echo ERROR: File %TEX_FILE% tidak ditemukan di %SOURCE_DIR%
    set "EXIT_CODE=1"
    goto :end
)

where pdflatex >nul 2>nul
if errorlevel 1 (
    echo ERROR: pdflatex tidak ditemukan. Pastikan TeX Live/MiKTeX terpasang dan ada di PATH.
    set "EXIT_CODE=1"
    goto :end
)

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%" 2>nul

pushd "%SOURCE_DIR%"

echo Running Stage 1: pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="%OUTPUT_DIR%" -jobname="%JOBNAME%" "%TEX_FILE%"
if errorlevel 1 goto :failed

echo Running Stage 2: pdflatex (stabilize refs/hyperref)...
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="%OUTPUT_DIR%" -jobname="%JOBNAME%" "%TEX_FILE%"
if errorlevel 1 goto :failed

popd

echo.
echo Cleaning up intermediate files (keep PDF and LOG)...
call :cleanup "%OUTPUT_DIR%" "%JOBNAME%"

REM Coba timpa PDF final; jika terkunci, hasil tetap di %JOBNAME%.pdf
copy /Y "%OUTPUT_DIR%\%JOBNAME%.pdf" "%OUTPUT_DIR%\%PDF_NAME%.pdf" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Hasil build: %OUTPUT_DIR%\%JOBNAME%.pdf
    echo ^(%PDF_NAME%.pdf kemungkinan terbuka di program lain - tutup lalu jalankan lagi^)
) else (
    del "%OUTPUT_DIR%\%JOBNAME%.pdf" 2>nul
    echo.
    echo Final PDF: %OUTPUT_DIR%\%PDF_NAME%.pdf
)
echo Log file:  %OUTPUT_DIR%\%JOBNAME%.log
echo Operation Completed.
goto :end

:failed
popd
set "EXIT_CODE=1"
echo.
echo ERROR: Compilation failed. Periksa %OUTPUT_DIR%\%JOBNAME%.log
goto :end

:cleanup
REM Hapus artefak kompilasi untuk jobname ini, kecuali .pdf dan .log
pushd "%~1"
for %%E in (aux bbl blg bcf out toc lof lot lol fls fdb_latexmk nav snm vrb idx ilg ind run.xml synctex.gz pdfsync xdv) do (
    if exist "%~2.%%E" del /q "%~2.%%E" 2>nul
)
popd
exit /b 0

:end
echo.
if /i not "%~1"=="nopause" pause
exit /b %EXIT_CODE%
