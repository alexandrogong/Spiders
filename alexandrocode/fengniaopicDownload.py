import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def error(fun):
    def wrapped(*s, **gs):
        try:
            fun()
        except:
            print('这个函数出错了:%s' % fun.__name__)
        return fun(*s, **gs)
    return wrapped


@error
def get_html(url):
    html = requests.get(url)
    return html.text


@error
def get_html_chrome(url):
    driver = webdriver.Chrome()
    driver.get(url)
    data = driver.page_source
    driver.quit()
    return data


@error
def get_depth(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    targets = soup.find('span', class_='total-num')
    return targets.text


@error
def get_img(url):
    html = get_html_chrome(url)
    soup = BeautifulSoup(html, 'html.parser')
    targets = soup.find('div', class_='pic-box')
    address = targets.img.get("orc_url")
    return address


@error
def save_image(url):
    html = requests.get(url)
    path = r'C:\\Users\\gonghaiq\\Desktop\\Pictures\\'
    name = url.split("/")[-1]
    path = path + name
    with open(path, 'wb') as f:
        f.write(html.content)


if __name__ == '__main__':
    num = 0
    while num <= 1000:
        url = r'http://image.fengniao.com/#p=3'
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        targets = soup.find_all('div', class_='li ll')
        links = []
        for x in targets:
            if x.span.text == '组图':
                links.append(x.a.get('href'))
        for link in links:
            try:
                print(link)
                Depth = get_depth(link)
                for i in range(int(Depth) - 1):
                    url = link + '#p=' + str(i + 1)
                    img_address = get_img(url)
                    save_image(img_address)
                    print("Successfully save image" + img_address.split('/')[-1])
            except:
                pass
            continue
        num = num+1


