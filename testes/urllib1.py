import urllib

f = urllib.urlopen("http://codare.aurelio.net")
contents = f.read()
f.close()
print contents
