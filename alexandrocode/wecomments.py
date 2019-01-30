# -*- coding: utf-8 -*-
import requests
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import random
import pandas as pd
import numpy as np
import win32gui
import win32api
import win32con


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

    # 浏览专用
    # recommend food
    # click_rec = driver.find_element_by_xpath("//a[@class='block-link']")
    # click_rec.click()


    # 评论专用
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

    # select service
    click_rio = driver.find_element_by_xpath("//div[@id='J_review-s4']/div/ul/li/a")
    click_rio.click()

    # input comment
    comments =np.loadtxt(open('.\links\comments.txt',"rb"),encoding="UTF-8",dtype=np.str)
    rowlist = []
    collist = []
    while(len(rowlist)!=12):
        a = random.randint(0,11)
        if a not in rowlist:
            rowlist.append(a)

    while(len(collist)!=15):
        b = random.randint(1,15)
        collist.append(b)

    comment = ''
    for i in range(11):
        comment = comment + "," + comments[collist[i],rowlist[i]]

    cmt_area = driver.find_element_by_xpath('//div[@class="reply-wrapper"]/textarea')
    cmt_area.send_keys(comment)
    time.sleep(3)

    # upload pic=====================================================================
    picindex = random.randint(2,7)
    pic1name = r'C:\Users\gonghaiq\Desktop\Python\Projects\Spiders\alexandrocode\imags'+'\\' +str(picindex)+'.jpg'
    pic2name = r'C:\Users\gonghaiq\Desktop\Python\Projects\Spiders\alexandrocode\imags'+'\\' +str(picindex-2)+'.jpg'
    pic3name = r'C:\Users\gonghaiq\Desktop\Python\Projects\Spiders\alexandrocode\imags'+'\\' +str(picindex+2)+'.jpg'

    # open upload window
    driver.find_element_by_xpath("//div[@id='J_swfuploader']").click()
    time.sleep(0.5)
    dialog = win32gui.FindWindow('#32770', 'open')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, pic1name)  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button    driver.find_element_by_xpath("//div[@id='J_swfuploader']").click()
    time.sleep(1)

    driver.find_element_by_xpath("//div[@id='J_swfuploader']").click()
    time.sleep(0.5)
    dialog = win32gui.FindWindow('#32770', 'open')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, pic2name)  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    time.sleep(1)

    driver.find_element_by_xpath("//div[@id='J_swfuploader']").click()
    time.sleep(0.5)
    dialog = win32gui.FindWindow('#32770', 'open')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, pic3name)  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    time.sleep(1)

    # submit
    sub_area = driver.find_element_by_xpath('//strong[@class="btn-type-b"]/input')
    sub_area.click()

    time.sleep(3)
    driver.close()
    driver.quit()






