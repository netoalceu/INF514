# -*- coding: cp1252 -*-
import BaseHTTPServer
import queryparser
from JsonBasico import *

htmlpage = """
<html><head><title>INF-0514 PROGRAMAÇÃO BÁSICA EM REDES DE COMPUTADORES (2018)</title></head>
  <body>
      <h2>Exemplo de Servidor Web em Python</h2>
      [parms]
  </body>
</html>"""

notfound = "File not found"


# o servidor
class ServidorExemplo(BaseHTTPServer.BaseHTTPRequestHandler):
    # tratamento de uma requisicao GET
    j = JsonBasico()

    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(htmlpage.replace('[parms]', j.getParms(self.path)))

    # tratamento de uma requisicao POST
    def do_POST(self):
        self.wfile.write("<HTML><body>Operação POST não permitida.<BR><BR></body></HTML>");


# criação do servidor
httpserver = BaseHTTPServer.HTTPServer(("", 8080), ServidorExemplo)

# rodar até ...
httpserver.serve_forever()

# testar com: ? http://localhost:8080/?nome=Jose&ra=2123
