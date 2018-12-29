import requests
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url)
    return html.text


def save_img(url):
    data = requests.get(url).content
    name = url.split("/")[-1]
    path = "C:\\Users\\gonghaiq\\Desktop\\豆瓣\\" + name
    with open(path, 'wb') as f:
        f.write(data)


if __name__ == '__main__':
    j = 0
    for i in range(10):
        url = r'https://movie.douban.com/top250?start=' + str(25*i) + '&filter='
        data = get_html(url)
        soup = BeautifulSoup(data, 'html.parser')
        # targets1 = soup.find_all('div', class_='hd')
        # targets2 = soup.find_all('span', class_='rating_num')
        # for j in range(len(targets2)):
        #     print(targets1[j].a.span.text, targets2[j].text)
        '''save img'''
        targets3 = soup.find_all('div', class_='pic')
        for link in targets3:
            save_img(link.a.img.get('src'))
        #     j += 1
        #     print(j)