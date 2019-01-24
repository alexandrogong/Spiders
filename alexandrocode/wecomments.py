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


def save_img(url, name):
    data = requests.get(url).content
    path = './imags/' + str(name)+'.jpg'
    with open(path, 'wb') as f:
        f.write(data)


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

    # select a random link
    driver = webdriver.Chrome()
    links =pd.read_csv('.\links\shop_links.txt',delimiter="/n")
    link = np.array(links)
    index = random.randint(0,len(link))
    shoplink = link[index]

    # open drviver
    driver.get("http://www.dianping.com/shanghai/ch10")

    # log in
    with open('.\cookies\wecomments_cookies.txt', 'r') as f:
        list_cookies = json.loads(f.read())

    for cookie in list_cookies:
        driver.add_cookie({'name': cookie['name'],
                           'value': cookie['value'],
                           'expires': None})

    driver.get(shoplink[0])

    # click like
    click_like = driver.find_element_by_xpath("//a[@class='item J-praise ']")
    click_like.click()

    # get pictures
    i=0
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    targets = soup.find_all('a', class_='item J-photo')
    for target in targets:
        piclink = target.img.get('data-big')
        save_img(piclink, i)
        i += 1
        if i==10:
            break

    # click comment
    click_cmt = driver.find_element_by_xpath("//span[@id='dpReviewBtn']")
    click_cmt.click()

    # switch to comment window
    handles = driver.window_handles
    driver.switch_to_window(handles[1])

    # select general
    click_gen = driver.find_element_by_xpath("//div[@class='rating-wrap-big']/ul/li/a")
    click_gen.click()

    # select taste
    click_taste = driver.find_element_by_xpath("//div[@id='J_review-s1']/div/ul/li/a")
    click_taste.click()

    # select environment
    click_env = driver.find_element_by_xpath("//div[@id='J_review-s2']/div/ul/li/a")
    click_env.click()

    # select service
    click_ser = driver.find_element_by_xpath("//div[@id='J_review-s3']/div/ul/li/a")
    click_ser.click()

    # input comment
    comments =pd.read_csv('.\links\comments.txt',delimiter="/n")
    index = random.randint(0,len(comments)-1)
    comment =  np.array(comments)[index]
    cmt_area = driver.find_element_by_xpath('//div[@class="reply-wrapper"]/textarea')
    cmt_area.send_keys(comment)

    # update pic
    name = random.randint(0,9)
    cname = "./imags/"+str(name)+'.jpg'
    driver.find_element_by_xpath("//div[@id='J_swfuploader']").click()
    driver.find_element_by_css_selector(".upload-pic").send_keys(cname)






    # submit
    sub_area = driver.find_element_by_xpath('//strong[@class="btn-type-b"]/input')
    sub_area.click()

    time.sleep(5)
    driver.close()





