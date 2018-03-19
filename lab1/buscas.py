def localiza_homonimos(lista_de_dicionarios):
    qnt_de_nomes={}
    dicionario_de_homonimos={}
    for dic_dados in lista_de_dicionarios:
        if qnt_de_nomes.has_key(dic_dados["Nome"]):
            qnt_de_nomes[dic_dados["Nome"]] = qnt_de_nomes[dic_dados["Nome"]] + 1
            dicionario_de_homonimos[dic_dados["Nome"]] = qnt_de_nomes[dic_dados["Nome"]]
        else:
            qnt_de_nomes.update({dic_dados["Nome"]:1})
    return dicionario_de_homonimos

def localiza_docs_duplicados(lista_de_dicionarios):
    qnt_de_docs={}
    dicionario_de_docs_duplicados={}
    for dic_dados in lista_de_dicionarios:
        if qnt_de_docs.has_key(dic_dados["Documento"]):
            qnt_de_docs[dic_dados["Documento"]] = qnt_de_docs[dic_dados["Documento"]] + 1
            dicionario_de_docs_duplicados[dic_dados["Documento"]] = qnt_de_docs[dic_dados["Documento"]]
        else:
            qnt_de_docs.update({dic_dados["Documento"]:1})
    return dicionario_de_docs_duplicados

def localiza_alunos_por_curso(lista_de_dicionarios):
    qnt_de_alunos_por_curso={}
    dicionario_de_qnt_de_alunos_por_curso={}
    for dic_dados in lista_de_dicionarios:
        if qnt_de_alunos_por_curso.has_key(dic_dados["Curso"]):
            qnt_de_alunos_por_curso[dic_dados["Curso"]] = qnt_de_alunos_por_curso[dic_dados["Curso"]] + 1
            dicionario_de_qnt_de_alunos_por_curso[dic_dados["Curso"]] = qnt_de_alunos_por_curso[dic_dados["Curso"]]
        else:
            qnt_de_alunos_por_curso.update({dic_dados["Curso"]:1})
    return dicionario_de_qnt_de_alunos_por_curso
