# -*- coding utf-8
import requests
from bs4 import BeautifulSoup
import time


def get_soup( url):
    flag = 0
    while flag <= 2:
        try:
            html = requests.get(url, timeout=30)
            soup = BeautifulSoup(html.text, 'html.parser')
            flag = 4
        except Exception as e:
            time.sleep(10)
            flag = flag + 1
            print(url + ' No responsing...')
            print(str(flag) + ' trying...')
    if flag == 3:
        print(url + ' Finally no responsing')
    return soup


def get_img(path, url):
    flag = 0
    while flag <= 2:
        try:
            name = url.split('/')[-1]
            content = requests.get(url).content
            with open(path + name, 'wb') as f:
                f.write(content)
            flag = 4
        except Exception as e:
            time.sleep(10)
            flag = flag + 1
            print(url + ' No responsing...')
            print(str(flag) + ' trying...')


if __name__ == '__main__':

    homepage = r'http://www.ivsky.com'
    save_path = r'C:\\Users\\gonghaiq\\Desktop\\Cats\\'
    links = []

    for i in range(44):
        url = 'http://www.ivsky.com/tupian/maomi_t178/index_' + str(i+1) +'.html'
        soup = get_soup(url)
        targets = soup.find_all("div", class_="il_img")
        for link in targets:
            address = homepage + link.a.get('href')
            links.append(address)

    jpg_link = []
    for link in links:
        soup = get_soup(link)
        targets = soup.find('img', id='imgis')
        jpg_link.append(targets.get('src'))

    for img in jpg_link:
        get_img(save_path, img)