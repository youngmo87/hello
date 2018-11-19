from bs4 import BeautifulSoup
import requests

url="https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

card_list = soup.select('div.card-list')

print(">>>>>>", len(card_list), card_list[0].get('class'))
for i in card_list:
    cards = i.select('.card')
    for c in cards:
        print(">>>", c.get('class'), c.select('a.title')[0].text)