from nturl2path import url2pathname
from os import name
import re
from xmlrpc.server import XMLRPCDocGenerator
import requests
from bs4 import BeautifulSoup





    

def recherche(name_crypto):
    url = 'https://coinmarketcap.com/fr/currencies/'
    response = requests.get(f"{url}{name_crypto}/")
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find('div',{'class' : 'priceValue'}).find('span')
        return(price.text)
    return(None)


recherche('amp')