@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "OUTPUT_DIR=%ROOT_DIR%output"
set "SOURCE_DIR=%ROOT_DIR%buku_ajar"
set "JOBNAME=main_build"

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%" 2>nul

echo ============================================================
echo Compiling Main Document
echo ============================================================
echo Jika main.pdf terbuka di viewer, tutup dulu agar bisa ditimpa.
echo.

pushd "%SOURCE_DIR%"

REM Check for latexmk AND perl
where latexmk >nul 2>nul
if errorlevel 1 (
    echo Latexmk not found. Using pdflatex loop...
    goto :pdflatex_loop
) else (
    where perl >nul 2>nul
    if errorlevel 1 (
        echo Latexmk found but Perl is missing. Skipping latexmk.
        goto :pdflatex_loop
    ) else (
        echo Latexmk and Perl found. Using latexmk...
        latexmk -pdf -interaction=nonstopmode -output-directory="%OUTPUT_DIR%" -jobname="%JOBNAME%" "main.tex"
        if errorlevel 1 (
            echo Latexmk failed. Falling back to pdflatex loop...
            goto :pdflatex_loop
        ) else (
            goto :success
        )
    )
)

:pdflatex_loop
echo Running Stage 1: pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="%OUTPUT_DIR%" -jobname="%JOBNAME%" "main.tex"
if errorlevel 1 goto :failed

echo Running Stage 2: bibtex...
bibtex "%OUTPUT_DIR%\%JOBNAME%"

echo Running Stage 3: pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="%OUTPUT_DIR%" -jobname="%JOBNAME%" "main.tex"

echo Running Stage 4: pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="%OUTPUT_DIR%" -jobname="%JOBNAME%" "main.tex"

echo Running Stage 5: pdflatex (stabilize refs)...
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="%OUTPUT_DIR%" -jobname="%JOBNAME%" "main.tex"
if errorlevel 1 goto :failed

:success
popd

echo Cleaning up intermediate files...
call :cleanup "%OUTPUT_DIR%"
call :cleanup "%SOURCE_DIR%"
REM Log di output dipertahankan untuk analisis warning/badbox
del /s /q "%SOURCE_DIR%\*.log" >nul 2>&1

REM Coba timpa main.pdf; jika terkunci, hasil tetap di main_build.pdf
copy /Y "%OUTPUT_DIR%\%JOBNAME%.pdf" "%OUTPUT_DIR%\main.pdf" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Hasil build: %OUTPUT_DIR%\%JOBNAME%.pdf
    echo ^(main.pdf kemungkinan terbuka di program lain - tutup lalu jalankan lagi untuk mendapatkan main.pdf^)
) else (
    del "%OUTPUT_DIR%\%JOBNAME%.pdf" 2>nul
    echo.
    echo Final PDF: %OUTPUT_DIR%\main.pdf
)
echo Operation Completed.
goto :end

:failed
popd
echo.
echo ERROR: Compilation failed.
goto :end

:cleanup
set "TARGET_FOLDER=%~1"
pushd "%TARGET_FOLDER%"
REM File terkait daftar pustaka SENGAJA tidak dihapus:
REM   *.bib  - basis data pustaka (references.bib), sumber dari bibtex
REM   *.bbl  - hasil olahan bibtex, dipakai pdflatex untuk mencetak daftar pustaka
REM   *.blg  - log bibtex, untuk menelusuri entri/sitasi yang bermasalah
REM Keduanya dipertahankan agar hasil bibliografi tetap tersimpan setelah build
REM dan bisa diperiksa atau dipakai ulang tanpa harus menjalankan bibtex lagi.
REM Ekstensi bibliografi yang hanya dihasilkan biblatex (bcf, run.xml) tetap
REM dibersihkan karena proyek ini memakai bibtex klasik.
for %%E in (aux toc lof lot lol out bcf fls fdb_latexmk nav snm vrb idx ilg ind acn acr alg glg glo gls ist xdy run.xml synctex pdfsync synctex.gz) do (
    del /s /q "*.%%E" >nul 2>&1
)
popd
exit /b 0

:end
echo.
pause
exit /b 0