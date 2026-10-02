@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "TEX_FILE=silabus_kriptografi.tex"
set "JOBNAME=silabus_kriptografi"

echo ============================================================
echo Compiling %TEX_FILE%
echo ============================================================
echo.

pushd "%ROOT_DIR%"

if not exist "%TEX_FILE%" (
    echo ERROR: File %TEX_FILE% tidak ditemukan di %ROOT_DIR%
    goto :failed
)

where pdflatex >nul 2>nul
if errorlevel 1 (
    echo ERROR: pdflatex tidak ditemukan. Pastikan TeX Live/MiKTeX terpasang dan ada di PATH.
    goto :failed
)

echo Running Stage 1: pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error "%TEX_FILE%"
if errorlevel 1 goto :failed

echo Running Stage 2: pdflatex (stabilize refs/hyperref)...
pdflatex -interaction=nonstopmode -halt-on-error "%TEX_FILE%"
if errorlevel 1 goto :failed

echo.
echo Cleaning up intermediate files (keep PDF and LOG)...
call :cleanup "%ROOT_DIR%" "%JOBNAME%"

echo.
echo Final PDF: %ROOT_DIR%%JOBNAME%.pdf
echo Log file:  %ROOT_DIR%%JOBNAME%.log
echo Operation Completed.
goto :end

:failed
popd
echo.
echo ERROR: Compilation failed. Periksa %JOBNAME%.log jika ada.
goto :end

:cleanup
REM Hapus artefak kompilasi untuk jobname ini, kecuali .pdf dan .log
set "TARGET_FOLDER=%~1"
set "BASE=%~2"
pushd "%TARGET_FOLDER%"
for %%E in (aux bbl blg bcf out toc lof lot lol fls fdb_latexmk nav snm vrb idx ilg ind acn acr alg glg glo gls ist xdy run.xml synctex synctex.gz pdfsync xdv tmp bak) do (
    if exist "%BASE%.%%E" del /q "%BASE%.%%E" 2>nul
)
REM synctex.gz kadang bernama jobname.synctex.gz
if exist "%BASE%.synctex.gz" del /q "%BASE%.synctex.gz" 2>nul
popd
exit /b 0

:end
popd 2>nul
echo.
pause
exit /b 0
