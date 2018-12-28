import requests
import time
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
    login_id = "****"
    password = "****@1"
    path = r"C:\\Users\\gonghaiq\\Desktop\\Tug paper\\"
    m_url = r"https://eknowledge.teradyne.com/wps/myportal/eknowledge/my/semiconductor_test" \
              r"/stdglobalsearch/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi3Q0M3D0s_A183J2dnQ0cP" \
              r"SwtTAIMggwNjIz0w1EVGJiGGho4hrqa-buHOhm4e5voR5Gk398lwMXA0TUoxNHRzNXQN9SIOP0GOICjAYn" \
              r"2YyqIwm98uH4UqhVYQgBVARYvErKkIDc0NDTCINPTUVERABwYwbc!/dz/d5/L2dBISEvZ0FBIS9nQSE" \
              r"h/?searchGlobal_scope=TUGSecCollection&SortBy=date"

    c_cookies = r"__utmz=71283093.1513142159.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;" \
                r" hubspotutk=ea66bb46e05b359f4edd43fbc52fb76b; __hs_opt_out=no; __hstc=267904273" \
                r".ea66bb46e05b359f4edd43fbc52fb76b.1512720983557.1542766727749.1542853357073.49; " \
                r"__utma=71283093.1786325429.1512720983.1545725175.1545794471.55; __utmc=71283093; __" \
                r"hssrc=1; __unam=eca3cfc-160353264b1-20968ad5-259; LtpaToken2=0ZmdYdYh7qUUhk5xu/cWI+C" \
                r"lqyvmK51hhBDCVAgtnrEhjKV7/dBGMyXL+EgGbQpP1ZO6NcF4BCuCqCkk7jVq/jsjzohgamoSQIxylGABNCCa+" \
                r"8hwDLKEzHdpX6eMXBzKXJXv52GycnTKqS/lWclAyOv6eg5cZYGb0IstOzs+8nCnxF0pm8e0N00O0tJBYFQiQFEU" \
                r"HHt1SvZXrIy7BdELoEttJ8bVU9Qek/bq/IM9Zka+AiCC3IOOwn1W9CmuJMKNhLpzyS2vboehTHnylsIDduJMKngmr" \
                r"6F3qn0ar3j4NFmEUf7I055d1mjAtfwSltUZDuex+Nbq3Xdr7x+Orm/AaGTw9cNicvTaH8x13NknbCWAxHtquR9mgEi0jF" \
                r"t3ZlCs; portal=1293444483.1.1409054128.3707520480; JSESSIONID=0000hxnZz4hKsr6GG2t9gLAvUFU:19vb00" \
                r"odv; PD-H-SESSION-ID=1_aytbbBOYTOOsdR6lYNzNpi8Y++UVOgbCU4sQasyPgIIrQO3RfrQ=_AAAAAwA=_oX38BIIxdWk" \
                r"DW99tYuhl/FN1RCI=; _pk_id.11.3ab8=1835ce7f460dd574.1512721124.76.1545884671.1545883624."

    d_cookies ={}
    for line in c_cookies.split(";"):
        key, value = line.split("=", 1)
        d_cookies[key] = value

    d_headers = {'User-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/71.0.3578.98 Safari/537.36"}

    # 打开 Teradyne TUG主页
    driver = webdriver.Chrome()
    driver.get(m_url)
    time.sleep(1)

    # 选择ultraFlexFamily
    ultraFlexFamily = driver.find_element_by_xpath("//input[@value='Product Type$UltraFLEX Family']")
    ultraFlexFamily.click()
    time.sleep(1)

    # 获取每页link
    html_text = driver.page_source
    m_links = get_links(html_text)

    # 下载每一个Link中的TUG paper
    i = 0
    for element in m_links:
        link = element.split("\"")[1]
        driver.get(link)
        download = driver.find_element_by_xpath("//div[@class='col-sm-2']/a[@class='btn btn-primary wcm-download-button-width']")
        download.click()
        time.sleep(10)
        print("成功下载" + str(i))
        i += 1

    # 点击下一页, 获取下一页的内容(total 80 pages)
    # for i in range(2):
    #     next_page = driver.find_element_by_xpath("//a[@onclick='nextRecords()']")
    #     next_page.click()
    #     time.sleep(1)
    #     html_text = driver.page_source
    #     m_links.extend(get_links(html_text))











