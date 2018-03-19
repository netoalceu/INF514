import urllib

def getData(url):
    u =urllib.urlopen(url)
    data = u.read()
    return data

print getData ('http://www.ic.unicamp.br/~vanini')