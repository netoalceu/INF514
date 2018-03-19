#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Alceu Rosa Neto - 26.772.122-5

import xml.dom.minidom
from xml.dom.minidom import Node

def hmsToSec(str_time):
    list_time = str_time.split("'")
    if len(list_time)>2:
        h = int(list_time[0])
        m = int(list_time[1])
        s = int(list_time[2])
    else:
        h = 0
        m = int(list_time[0])
        s = int(list_time[1])
    return 3600*h + 60*m + s

def secToHms(sec):
    h = sec // 3600
    m = (sec % 3600)//60
    s = (sec % 60)
    return str(h) + ":" + str(m) + ":"+ str(s)

def openXML(path):
    return xml.dom.minidom.parse(path)


def autores(xml_doc):
    album = xml_doc.getElementsByTagName("track")
    autores=[]
    for tag_autores in album:
       autores.append(tag_autores.getAttribute("author"))
    return list(set(autores))

def albuns(xml_doc):
    albuns = xml_doc.getElementsByTagName("album")
    lista_de_titulos={}
    for tag_titulos in albuns:
        faixas = tag_titulos.getElementsByTagName("track")
        tempo_do_album = 0
        for faixa in faixas:
            tempo_do_album += hmsToSec(faixa.getAttribute("time"))
        lista_de_titulos[tag_titulos.getAttribute("tittle")] = secToHms(tempo_do_album)

    return lista_de_titulos



xml_doc = openXML("cds.xml")
print(autores(xml_doc))
print(albuns(xml_doc))
