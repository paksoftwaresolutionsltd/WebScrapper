import requests
from bs4 import BeautifulSoup

def class_page_web_scrapper(max_pages):
    url = 'http://www.yifysubtitles.com/browse/page-'
    page = 1
    while page <= max_pages:
        new_url = url + str(page)
        source_code = requests.get(new_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for item in soup.findAll('h3', {'class': 'media-heading'}):
            print(item.string)
        page = page + 1

class_page_web_scrapper(2)
