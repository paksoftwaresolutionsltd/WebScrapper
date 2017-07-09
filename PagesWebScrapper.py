import requests
from bs4 import BeautifulSoup

def page_web_scrapper(max_pages):
    url = 'http://www.yifysubtitles.com/browse/page-'
    page = 1
    while page <= max_pages:
        new_url = url + str(page)
        source_code = requests.get(new_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a'):
            href = 'http://www.yifysubtitles.com' + link.get('href')
            print(href)
        page = page + 1

page_web_scrapper(2)
