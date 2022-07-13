import requests
import urllib.request
import urllib
url = 'http://www.pudim.com.br/??'

if requests.get(url).status_code == 200:
    print('O site do pudim está disponível.')
else:
    print('O site do pudim não está disponível.')
    
try:
    
    site = urllib.request.urlopen(url)
    print('Consegui acessar com urllib')
except:
    print('Não consegui acessar com urllib')
    