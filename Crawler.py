import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup

#metodo che prende in argomento un indirizzo url e restituisce un array strutturato nel seguente modo:
#INDEX      VALUE
#0          url del sito analizzato
#1          numero di caratteri nella descrizione
#2          numero di immagini nella pagina
#3          dump json di un array contenente tutti i vari livelli di ricompensa
def get_info(url):
    result = []    
    response = requests.get(url)
    bs4 = BeautifulSoup(response.text, 'html.parser')
    result.append(url)
    result.append(description_len(bs4))
    result.append(count_image(bs4))
    result.append(get_rewards(bs4))
    return result


#metodo che restituisce un JSON relativo ad un array dove son presenti tutti i vari livelli di ricompensa
def get_rewards(soup):
    result = []
    for a in soup.find('div', class_='NS_projects__rewards_list js-project-rewards').find_all('span', class_='money'):
        out = a.get_text()
        result.append(out)#.replace(',', ''))
    return json.dumps(result)


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

