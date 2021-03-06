# -*- coding: cp1252 -*-
import queryparser
import json

class JsonBasico():
    lista_de_parms = []

    def createList(self,path):
        parms = queryparser.parse(path)
        self.lista_de_parms.append(parms)
        return self.lista_de_parms


    def createJson(self,list):
        json_codificado = json.dumps(list,indent=4)
        return json_codificado


    def generateParms(self, json_codificado):
        res = '<h3> Parāmetros:</h3>\n'
        lista_json = json_codificado.split("\n")
        for j in lista_json:
            res += '<p>' + j + '"\n'
        return res

    def getParms(self, path):
        lista = self.createList(path)
        json = self.createJson(lista)
        parms = self.generateParms(json)
        return parms

#/?nome=Jose&ra=2123

if __name__ == "__main__":
    j = JsonBasico()
    j.createList("/?nome=Jose&ra=2123")
    j.createList("/?nome=antonio&ra=3456")
    j.createList("/?nome=migue&ra=6789")
    print(j.getParms("/?nome=migue&ra=6789"))
