import requests
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import random
import pandas as pd
import numpy as np


def get_link(content):
    link = []
    soup = BeautifulSoup(content, 'html.parser')
    targets = soup.find('div', class_='nc-items nc-more')
    target = targets.find_all('a')
    for element in target:
        link.append(element.get("href"))
    return link


if __name__ == "__main__":
    # m_url = "http://www.dianping.com/shanghai/food" # https://www.dianping.com/"
    # # 获取cookies 保存到cookies文件夹。
    # driver = webdriver.Chrome()
    # driver.get(m_url)
    # d_cookies = driver.get_cookies()
    # json_cookies = json.dumps(d_cookies)
    # with open('.\cookies\wecomments_cookies.txt', 'w') as f:
    #     f.write(json_cookies)
    # driver.close()
    # driver.quit()

    # load different food link
    links = pd.read_csv('.\links\myfood_links.txt')
    # with open('.\links\myfood_links.txt', 'r') as f:
    #     links = f.read()
    # choose a random link
    index = random.randint(0,len(links)-1)
    link = np.array(links)[index]

    # choose a random page 1-50
    page = random.randint(1,50)
    m_url = link + 'p'+ str(page)

    # load existed cookies
    with open('.\cookies\wecomments_cookies.txt', 'r') as f:
        list_cookies = json.loads(f.read())

    # log in dianping
    driver = webdriver.Chrome()
    driver.get(m_url[0])
    for cookie in list_cookies:
        driver.add_cookie({'name': cookie['name'],
                           'value': cookie['value'],
                           'expires': None})
    driver.get(m_url[0])
    # time.sleep(5)

    # open restaurant homepage
    click_shop = driver.find_element_by_xpath("//div[@class='pic']/a")
    click_shop.click()

    # # click like
    # click_like = driver.find_element_by_xpath("//a[@class='item J-praise']/i[@class='icon i-praise']")
    # click_like.click()

    # click comment
    click_cmt = driver.find_element_by_xpath("//span[@id='dpReviewBtn']")
    click_cmt.click()

    # select general
    click_gen = driver.find_element_by_xpath("//div[@id='J_shop-rating']/div/ul/li/a[@span='four-stars active-star']")
    click_gen.click()

    # select taste
    click_taste = driver.find_element_by_xpath("//div[@class='score-wrap']/a[@class='square-3 active-square']")
    click_taste.click()

    # select environment
    click_env = driver.find_element_by_xpath("//div[@class='score-wrap']/a[@class='square-3 active-square']")
    click_env.click()






    time.sleep(5)



