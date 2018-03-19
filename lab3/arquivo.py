import xml.dom.minidom
from xml.dom.minidom import Node

def getText(tag):
    text = ""
    for n in tag.childNodes:
        if n.nodeType == Node.TEXT_NODE:
            text += n.data
    return text

def getTextByTagName(tag,name):
    for n in tag.getElementsByTagName(name):
        return getText(n)

doc = xml.dom.minidom.parse("cds.xml")

albuns = doc.getElementsByTagName("album")
album = doc.getElementsByTagName("tracks")
#for album in albuns:
#    print("Artista: ",album.getAttribute("artist"))

for faixas in album:

    faixa = faixas.getElementsByTagName("track")
    for autor in faixa:
        print (autor.getAttribute("time"))


#print(albuns[0].toxml())
#print(album[0].toxml())
#print(doc.toxml())

#lista = doc.getElementsByTagName("cdlist")
#print(lista)
#for node in lista:
#    author = node.getAttribute("author")
#    print("author=",author)