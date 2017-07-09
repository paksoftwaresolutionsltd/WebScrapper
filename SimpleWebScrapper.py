import requests
from bs4 import BeautifulSoup

def simple_web_scrapper(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a'):
        href = url + link.get('href')
        print(href)


simple_web_scrapper('http://www.yifysubtitles.com')
