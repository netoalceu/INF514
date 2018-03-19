from arquivo import *
from buscas import *
from relatorios import *

# trata o arquivo .csv para uma lista de dicionarios
arquivo = Linhas_para_dicionario(abre_arquivo("alunos5k.csv"))

# executa a busca por homonimos
dicionario_de_homonimos = localiza_homonimos(arquivo)
qnt_homonimos = sum(dicionario_de_homonimos.values())

# executa a busca por documentos repetidos
dicionario_de_docs_duplicados = localiza_docs_duplicados(arquivo)
qnt_docs_duplicados = sum(dicionario_de_docs_duplicados.values())

# executa a busca por Cursos e qnt de alunos
dicionario_de_qnt_de_alunos_por_curso = localiza_alunos_por_curso(arquivo)
qnt_cursos=len(dicionario_de_qnt_de_alunos_por_curso.keys())

# Imprime o relatorio
imprime_cabecalho_do_relatorio()
imprime_homonimos_do_relatorio(qnt_homonimos,dicionario_de_homonimos)
imprime_docs_duplicados_do_relatorio(qnt_docs_duplicados,dicionario_de_docs_duplicados)
imprime_qnt_de_alunos_por_curso_do_relatorio(qnt_cursos,dicionario_de_qnt_de_alunos_por_curso)
imprime_rodape_do_relatorio()
