'''
    cliente exemplo para a atividade 3
'''

import urllib

def sendReq(nome,ra):
    req = urllib.urlopen('http://localhost:8080?nome='+str(nome)+'&ra='+str(ra))
    return req.read()


                        

