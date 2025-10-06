@echo off

j:
cd \Deploy\procura_ementa

rem ***source vprod/bin/activate
rem .\vprod\Scripts\activate

:: --- Cria a pasta Log se não existir ---
if not exist "Log" (
    mkdir "Log"
)

:: --- Gera timestamp no formato AAAA-MM-DD_HH-MM-SS ---
for /f "tokens=1-3 delims=/" %%a in ("%date%") do (
    set "ano=%%c"
    set "mes=%%b"
    set "dia=%%a"
)
for /f "tokens=1-3 delims=:." %%a in ("%time%") do (
    set "hora=%%a"
    set "min=%%b"
    set "seg=%%c"
)
:: Remove espaços e ajusta zero na hora, se necessário
set "hora=%hora: =0%"

set "timestamp=%ano%-%mes%-%dia%_%hora%-%min%-%seg%"
set "output=.\Log\log_%timestamp%.txt"

echo Executando script Python... > "%output%"
.\vprod\scripts\python .\le_ementas.py >> "%output%"

echo Log salvo como: %output%