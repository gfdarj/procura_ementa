#

Lista de projetos de lei da legislatura 23-27
http://alerjln1.alerj.rj.gov.br/scpro2327.nsf/Internet/LeiInt?OpenForm&Count=999&ResortAscending=1?ID=20250305667



------
https://www.computersciencemaster.com.br/como-executar-codigo-python-dentro-do-excel/

Dim objShell As Object
Dim PythonExePath As String, PythonScriptPath As String
ActiveWorkbook.Save
ChDir ActiveWorkbook.Path

Set objShell = VBA.CreateObject("Wscript.Shell")
    
PythonExePath = """C:\Python310\python.exe"""
PythonScriptPath = """C:\Users\Vinicius\Desktop\pyExcel\gerargrafico.py"""
    
objShell.Run PythonExePath & PythonScriptPath
