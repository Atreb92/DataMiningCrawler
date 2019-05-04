import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.kickstarter.com/projects/wearewao/wao-the-eco-effect-shoes?ref=discovery_category_newest'
response = requests.get(url)

bs4 = BeautifulSoup(response.text, 'html.parser')


#metodo per contare il numero totale di immagini presenti nella pagina
def count_image(soup):
    count_img = 0
    for e in soup.find_all('div', class_='template asset'):
        count_img = count_img + 1
    return count_img

print(count_image(bs4))