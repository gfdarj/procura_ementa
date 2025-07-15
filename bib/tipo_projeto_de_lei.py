
def mostra(numero_pl):
    codigo_tipo = numero_pl[4:6]
    tipo = ""

    if codigo_tipo == "01":
        tipo = "PEC"    #Proposta de Emenda Constitucional
    elif codigo_tipo == "02":
        tipo = "PLC"    #Projeto de Lei Complementar
    elif codigo_tipo == "03":
        tipo = "PL"     #Projeto de Lei
    elif codigo_tipo == "04":
        tipo = "PDL"    #Projeto Decreto Legislativo
    elif codigo_tipo == "05":
        tipo = "PR"     #Projeto de Resolucao
    elif codigo_tipo == "06":
        tipo = "IL"     #Indicação Legislativa
    elif codigo_tipo == "07":
        tipo = "IND"    #Cadastro de Indicação
    elif codigo_tipo == "08":
        tipo = "MSG"    #MENSAGEM
    elif codigo_tipo == "09":
        tipo = "REQIN"  #Requerimento de Informações
    elif codigo_tipo == "10":
        tipo = "REQ"    #Requerimento
    elif codigo_tipo == "11":
        tipo = "OFI"    #Ofícios
    elif codigo_tipo == "12":
        tipo = "12"    #
    elif codigo_tipo == "13":
        tipo = "13"    #
    elif codigo_tipo == "14":
        tipo = "MOC"  # MOÇÔES
    elif codigo_tipo == "15":
        tipo = "REQSN"  #Requerimento sem numero

    return tipo
