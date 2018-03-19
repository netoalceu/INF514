def abre_arquivo(file_path):
    ref_arquivo = open(file_path,"r")
    lista_de_linhas = ref_arquivo.readlines()
    ref_arquivo.close()
    return lista_de_linhas

def Linhas_para_dicionario(lista_de_linhas):
    lista_key = lista_de_linhas[0].replace("\n","").split(";")
    lista_value = lista_de_linhas[1:]

    lista_de_dicionarios=[]
    for value in lista_value:
        lista_de_dicionarios.append(dict(zip(lista_key,value.replace("\n","").split(";"))))
    return lista_de_dicionarios
