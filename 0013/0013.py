import re
import requests
import os


def spiderJPG(url):
    html = requests.get(url).text
    pattern = re.compile(r'src="(.*?\.jpg)" bdwater=')
    imglist = re.findall(pattern, html)

    for count, i in enumerate(imglist):
        with open('C:\\Users\\11018\\projects\\py25\\0013\\pic\\%d.jpg' % count, 'wb') as f:
            f.write(requests.get(i).content)
    print("it's ok")


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    spiderJPG(url)
