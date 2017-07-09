import requests
from bs4 import BeautifulSoup

def class_web_scrapper(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for post_text in soup.findAll('h3', {'class': 'media-heading'}):
        content = post_text.string
        print (content)

class_web_scrapper('http://www.yifysubtitles.com/browse/page-1')
