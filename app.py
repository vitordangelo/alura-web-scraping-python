from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'http://alura-site-scraping.herokuapp.com'
# url = 'https://alura.com.br'
headers = {'User-Agent': 'Chrome/76.0.3809.100'}

req = Request(url, headers=headers)
response = urlopen(req)

html = response.read()
html = html.decode('utf-8')

anuncio = BeautifulSoup(html, 'html.parser')

card = {}

# content = soup.find('h1', id="hello-world").get_text()
# content = soup.find('h1', {'class': 'sub-header'}).get_text()
# print(content)


# def trata_html(html):
#   return " ".join(html.split()).replace('> <', '><')


infos = anuncio.find("div", {'class': 'body-card'}).findAll('p')

for info in infos:
    card[info.get('class')[0].split('-')[-1]] = info.get_text()

print(card)