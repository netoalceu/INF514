from json import loads

def abre_arquivo_json(file_path):
    ref_arquivo = open(file_path,"r")
    json = loads(ref_arquivo.read())
    return json
