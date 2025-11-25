#BIBLIOTECA BEATUFIULSOUP, FOCADA EM WEBSCRAPING

import requests
from bs4 import BeautifulSoup

# Pegar o conteúdo de uma página
url = "https://www.python.org/"
resposta = requests.get(url)

# Criar o objeto BeautifulSoup
sopa = BeautifulSoup(resposta.text, "html.parser")

# Extrair o título da página
titulo = sopa.title.string

print("Título da página:", titulo)