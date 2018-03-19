# -*- coding: cp1252 -*-
import BaseHTTPServer
import queryparser

htmlpage = """
<html><head><title>INF-0514 PROGRAMA��O B�SICA EM REDES DE COMPUTADORES (2018)</title></head>
  <body>
      <h2>Exemplo de Servidor Web em Python</h2>
      [parms]
  </body>
</html>"""

notfound = "File not found"

# monta uma sequencia de linhas com os par�metros passados na url
# como parte de um texto HTML

def getParms(path):
    parms = queryparser.parse(path)
    res = '<h3> Par�metros:</h3>\n'
    for k in parms.keys():
        res += '<p>'+k+'="'+parms[k]+'"\n'
    return res

# o servidor
class ServidorExemplo(BaseHTTPServer.BaseHTTPRequestHandler):
    # tratamento de uma requisicao GET
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(htmlpage.replace('[parms]',getParms(self.path)))

    # tratamento de uma requisicao POST
    def do_POST(self):
        self.wfile.write("<HTML><body>Opera��o POST n�o permitida.<BR><BR></body></HTML>");


# cria��o do servidor
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo)

# rodar at� ...
httpserver.serve_forever()

# testar com: ? http://localhost:8080/?nome=Jose&ra=2123
