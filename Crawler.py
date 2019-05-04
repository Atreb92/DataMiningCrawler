import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.kickstarter.com/projects/wearewao/wao-the-eco-effect-shoes?ref=discovery_category_newest'
response = requests.get(url)

bs4 = BeautifulSoup(response.text, 'html.parser')



#metodo per il conteggio dei caratteri presenti nella descrizione
def description_len(soup):
    text_total=0
    for p in soup.find('div', class_="full-description js-full-description responsive-media formatted-lists").find_all('p'):
        text_total += len(p.get_text())
    return text_total

#metodo per contare il numero totale di immagini presenti nella pagina
def count_image(soup):
    count_img = 0
    for e in soup.find_all('div', class_='template asset'):
        count_img += 1
    return count_img
