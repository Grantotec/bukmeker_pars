from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get('https://1xstavka.ru/line/football')
# result = driver.find_element(By.CLASS_NAME, 'liga_menu')

page = requests.get('https://1xstavka.ru/line/football')
soup = BeautifulSoup(page.text, 'html.parser')

champs = soup.find_all('a', ['link link--labled',
                                 'imp link link--labled'])
games_count = list(map(lambda x: x.find('span', 'link-title__count').contents, champs))

print(games_count)
