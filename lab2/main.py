#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from json import loads

def abre_arquivo_json(file_path):
    ref_arquivo = open(file_path,"r")
    json = loads(ref_arquivo.read())
    return json

def busca(cd_list,string_de_referencia,tipo=2):
    #Dicionario de tipos de pesquisa
    #1:"author"
    #2:"name"
    #3:"time"
    dic_tipos = {1:"author",2:"name",3:"time"}
    lista_de_resultados = []
    tracks_info={}
    for tracks in cd_list['cdlist']:
        tracks_info = tracks['tracks']
        for track_name in tracks_info:
            if track_name[dic_tipos[tipo]].upper().find(string_de_referencia.upper())>= 0:
                lista_de_resultados.append(track_name[dic_tipos[tipo]])
    return set(lista_de_resultados)


argumentos = sys.argv[1].split(',')
cd_list = abre_arquivo_json(argumentos[0])
for a in busca(cd_list,argumentos[1],int(argumentos[2])):
    print a
