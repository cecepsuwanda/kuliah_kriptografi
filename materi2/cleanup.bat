@echo off
echo Cleaning up LaTeX auxiliary files...
echo Keeping .log and .bib files as requested.

REM Remove auxiliary files
if exist "*.aux" del "*.aux"
if exist "*.bbl" del "*.bbl"
if exist "*.blg" del "*.blg"
if exist "*.fdb_latexmk" del "*.fdb_latexmk"
if exist "*.fls" del "*.fls"
if exist "*.out" del "*.out"
if exist "*.synctex.gz" del "*.synctex.gz"
if exist "*.toc" del "*.toc"
if exist "*.lof" del "*.lof"
if exist "*.lot" del "*.lot"
if exist "*.lol" del "*.lol"
if exist "*.nav" del "*.nav"
if exist "*.snm" del "*.snm"
if exist "*.vrb" del "*.vrb"
if exist "*.xdv" del "*.xdv"
if exist "*.run.xml" del "*.run.xml"

REM Remove temporary files
if exist "*.tmp" del "*.tmp"
if exist "*~" del "*~"
if exist "*.bak" del "*.bak"

echo Cleanup completed!
echo Remaining files: .tex, .pdf, .log, .bib
pause
