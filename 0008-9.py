from bs4 import BeautifulSoup
import requests


def findBody(url):
    res = requests.get(url)
    html_doc = str(res.content, 'GBK')
    soup = BeautifulSoup(html_doc, 'lxml')
    for p in soup.findAll('p'):
        print(p.text)


def findUrl(url):
    res = requests.get(url)
    html_doc = str(res.content, 'GBK')
    soup = BeautifulSoup(html_doc, 'lxml')
    for p in soup.findAll('a'):
        print(p.get("href"))


if __name__ == '__main__':
    url = '...'
    findUrl(url)
    findBody(url)
