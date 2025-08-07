@echo off

j:
cd \Deploy\procura_ementa
rem ***source vprod/bin/activate
rem .\vprod\Scripts\activate

.\vprod\scripts\python .\le_ementas.py >> output.txt
