# -*- coding: cp1252 -*-
import BaseHTTPServer
import queryparser
htmlpage = """
<html><head><title>Inf 515 - Aplicacões Distribuídas</title></head>
  <body>
      <h2>Exemplo de Servidor Web em Python</h2>
      [parms]
  </body>
</html>"""

notfound = "File not found"

# monta uma sequencia de linhas com os parâmetros passados na url
# como parte de um texto HTML
def getParms(path):
    parms = queryparser.parse(path)
    res = '<h3> Parâmetros:</h3>\n'
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
        self.wfile.write("<HTML><body>Operação POST não permitida.<BR><BR></body></HTML>");


# criação do servidor            
httpserver = BaseHTTPServer.HTTPServer(("",8000), ServidorExemplo)

# rodar até ...
httpserver.serve_forever()

# testar com: http://localhost:8080//?vulcao=Eyjafallajokull&evento=erupcao&dia=0&hora=0&op=ca
