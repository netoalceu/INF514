# -*- coding: cp1252 -*-
import queryparser

class Json_basico():
    lista_de_parms = []

    def createList(self,path):
        parms = queryparser.parse(path)
        self.lista_de_parms.append(parms)
        return self.lista_de_parms


    def getParms(self):
        res = '<h3> Parâmetros:</h3>\n'
        res += '<p>' + "[" + '"\n'
        for parms in self.lista_de_parms:
            res += '<p>' + "    {" + '"\n'
            for k in parms.keys():
                res += '<p>         ' + k + '="' + parms[k] + '"\n'
            res += '<p>' + "    }"+ '"\n'
        res += '<p>' + "]" + '"\n'
        return res

#/?nome=Jose&ra=2123

if __name__ == "__main__":
    json = Json_basico()
    json.createList("/?nome=Jose&ra=2123")
    json.createList("/?nome=Jose&ra=2123")
    json.createList("/?nome=Jose&ra=2123")
    list = json.createList("/?nome=Jose&ra=2123")
    print(json.getParms())