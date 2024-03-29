from bs4 import BeautifulSoup
from urllib.request import urlopen
from urls import url
def inner_html(url):
    return str(urlopen(url).read(), 'utf-8')


def get_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', {'class': 'apphub_AppName'})
    price = soup.find('div', {'class': 'discount_original_price'})
    if price is None:
        price = soup.find('div', class_='game_purchase_price price')
    price.string.replace_with('Цена в Steam: ' + price.string)
    title_text = title.get_text()
    price_text = price.get_text()
    return {'title': title_text, 'price': price_text}


def parse(url):
    return get_link(inner_html(url))

