from banco_de_dados.sqlite import projeto_de_lei_bd
from bib import le_projetos_de_lei


pls = le_projetos_de_lei.obtem_lista()


#print(" *********************************************************************** ")
bd = projeto_de_lei_bd()
bd.ApagaTudo()

for a in pls:
    print(f"{a.numero_formatado} - {a.numero} - {a.tipo}\n{a.ementa}\n{a.comissoes}\n{a.autor}\n{a.data_publicacao}\n")
    bd.Insere(a.numero, a.ementa, a.data_publicacao, a.autor, a.comissoes, a.tipo)
    #print("")

print(f"Total: {len(pls)}")
print("* FIM *")

