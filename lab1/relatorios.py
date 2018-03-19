def imprime_cabecalho_do_relatorio():
    print("===============================")
    print("===Relatorio: Laboratorio 1====")
    print("===============================")
    return True

def imprime_homonimos_do_relatorio(qnt_homonimos,dicionario_de_homonimos):
    print("Homonimos: %s" % qnt_homonimos)
    for e in dicionario_de_homonimos:
        print("%s %s"%(e,dicionario_de_homonimos[e]))
    print("\n")
    return True

def imprime_docs_duplicados_do_relatorio(qnt_docs_duplicados,dicionario_de_docs_duplicados):
    print("Documentos Repetidos: %s" % qnt_docs_duplicados)
    for e in dicionario_de_docs_duplicados:
        print("%s %s"%(e,dicionario_de_docs_duplicados[e]))
    print("\n")
    return True

def imprime_qnt_de_alunos_por_curso_do_relatorio(qnt_cursos,dicionario_de_qnt_de_alunos_por_curso):
    print("Cursos: %s" % qnt_cursos)
    for e in dicionario_de_qnt_de_alunos_por_curso:
        print("%s %s"%(e,dicionario_de_qnt_de_alunos_por_curso[e]))
    print("\n")
    return True


def imprime_rodape_do_relatorio():
    print("===============================")
    print("=======Fim do relatorio========")
    print("===============================")
    return True
