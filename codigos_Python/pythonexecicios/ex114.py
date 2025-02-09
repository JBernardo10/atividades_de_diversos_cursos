import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except Exception as erro:
    print(f"deu erro: {erro}")
else:
    print("ta tudo ok")
    print(site.read())