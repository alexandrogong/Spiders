import requests
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver


def get_links(content):
    soup = BeautifulSoup(content, 'html.parser')
    targets = soup.find_all('div', class_='docListing')
    links = []
    for element in targets:
        links.append(element.a.get("onclick"))
    return links


def get_link(content):
    soup = BeautifulSoup(content, 'html.parser')
    targets = soup.find('div', class_='col-sm-2')
    link = targets.a.get("href")
    return link


if __name__ == "__main__":

    # # 获取cookies 保存到cookies文件夹。
    # driver = webdriver.Chrome()
    # driver.get(m_url)
    # d_cookies = driver.get_cookies()
    # json_cookies = json.dumps(d_cookies)
    # with open('.\cookies\eknowledge_cookies.txt', 'w') as f:
    #     f.write(json_cookies)
    # driver.close()
    # driver.quit()


    # 打开 Teradyne TUG主页
    m_path = r"C:\\Users\\gonghaiq\\Desktop\\Tug paper\\"

    m_url = r"https://eknowledge.teradyne.com/wps/myportal/eknowledge/my/semiconductor_test" \
              r"/stdglobalsearch/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi3Q0M3D0s_A183J2dnQ0cP" \
              r"SwtTAIMggwNjIz0w1EVGJiGGho4hrqa-buHOhm4e5voR5Gk398lwMXA0TUoxNHRzNXQN9SIOP0GOICjAYn" \
              r"2YyqIwm98uH4UqhVYQgBVARYvErKkIDc0NDTCINPTUVERABwYwbc!/dz/d5/L2dBISEvZ0FBIS9nQSE" \
              r"h/?searchGlobal_scope=TUGSecCollection&SortBy=date"

    # load cookies
    with open('.\cookies\eknowledge_cookies.txt', 'r') as f:
        list_cookies = json.loads(f.read())

    # 打开teradyne TUG 主页=====================================================================
    # 设置选项 不弹窗，下载默认地址为指定地址 禁用pdf viewer
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Users\\gonghaiq\\Desktop\\Tug paper\\TUG_PY',
             "profile.default_content_settings.pdf_documents": 1}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='C:\\Users\\gonghaiq\\AppData\\Local\\Programs\\Python\\Python36-32\\chromedriver.exe', chrome_options=options)

    driver.get("https://eknowledge.teradyne.com")
    for cookie in list_cookies:
        driver.add_cookie({'name': cookie['name'],
                           'value': cookie['value'],
                           'expires': None})
    driver.get(m_url)
    time.sleep(5)

    # 选择ultraFlexFamily
    ultraFlexFamily = driver.find_element_by_xpath("//input[@value='Product Type$UltraFLEX Family']")
    ultraFlexFamily.click()
    time.sleep(5)


    # 获取每页link并将link全部要写入文件==================================================================================
    # html_text = driver.page_source
    # m_links = get_links(html_text)

    # with open('.\TUG\paper_links.txt', 'w') as f:
    #     # 写入第一次的30个links
    #     for link in m_links:
    #         f.write(link+'\n')
    #     # 点击下一页, 获取下一页的内容(total 80 pages)
    #     i = 0
    #     for i in range(80):
    #         next_page = driver.find_element_by_xpath("//a[@onclick='nextRecords()']")
    #         next_page.click()
    #         time.sleep(1)
    #         html_text = driver.page_source
    #         m_links = get_links(html_text)
    #         for link in m_links:
    #             f.write(link + '\n')
    #         time.sleep(5)
    #         print("成功下载" + str(i) + "次")
    #         i += 1


    # 下载文件中的所有链接===============================================================================================
    i = 0
    with open('.\TUG\paper_links.txt', 'r') as f, open('.\TUG\paper_index.txt', 'w') as f1:
        link = f.readline()
        while link:
            # 重新给cookie, 打开网页
            # driver.get(m_url)
            for cookie in list_cookies:
                driver.add_cookie({'name': cookie['name'],
                                   'value': cookie['value'],
                                   'expires': None})
            driver.get(link.split("\"")[1])
            download = driver.find_element_by_xpath("//div[@class='col-sm-2']/a[@class='btn btn-primary wcm-download-button-width']")
            download.click()
            pdf_name = driver.find_element_by_xpath("//div[@class='col-sm-10 padding-filename-text']/span[@id='wcmFile1Name']").text
            paper_name = driver.find_element_by_xpath("//div[@class='panel-heading']/h3[@class='panel-title']").text

            time.sleep(10)
            link = f.readline()

            f1.write(paper_name + "_" + pdf_name + "\n")

            print("成功下载" + str(i))
            i += 1

    print("finish download...")









    # # 下载每一个Link中的TUG paper
    # i = 0
    # for element in m_links:
    #     link = element.split("\"")[1]
    #
    #     # driver.get(link)
    #     for cookie in list_cookies:
    #         driver.add_cookie({'name': cookie['name'],
    #                            'value': cookie['value'],
    #                            'expires': None})
    #
    #     driver.get(link)
    #     download = driver.find_element_by_xpath("//div[@class='col-sm-2']/a[@class='btn btn-primary wcm-download-button-width']")
    #     download.click()
    #     time.sleep(10)
    #     print("成功下载" + str(i))
    #     i += 1













