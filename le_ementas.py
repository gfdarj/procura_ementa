from banco_de_dados import sqlite
from banco_de_dados import msacess
from bib import le_projetos_de_lei


#### CHAMA AS ROTINAS WEB PARA CARREGAR UMA LISTA DOS PROJETOS
print("*** Lendo as páginas html")
pls = le_projetos_de_lei.obtem_lista()


print("*** Gravando os projetos no banco de dados")
#### CONECTA COM O BANCO DE DADOS E SALVA OS PROJETOS
bd = msacess.conexao_msacess()
bd.ApagaTudo()

for a in pls:
    print(f"{a.numero_formatado} - {a.numero} - {a.tipo}\n{a.ementa}\n{a.comissoes}\n{a.autor}\n{a.data_publicacao}\n")
    bd.Insere(a.numero, a.ementa, a.data_publicacao, a.autor, a.comissoes, a.tipo, a.numero_formatado)
    #print("")

print(f"Total: {len(pls)}")



#### CONECTA COM O BANCO DE DADOS E SALVA OS PROJETOS
#bd = sqlite.conexao_sqlite()
#bd.ApagaTudo()
#
#for a in pls:
#    print(f"{a.numero_formatado} - {a.numero} - {a.tipo}\n{a.ementa}\n{a.comissoes}\n{a.autor}\n{a.data_publicacao}\n")
#    bd.Insere(a.numero, a.ementa, a.data_publicacao, a.autor, a.comissoes, a.tipo, a.numero_formatado)
#    #print("")

#print(f"Total: {len(pls)}")


print("* FIM *")

