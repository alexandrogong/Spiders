import time
from selenium import webdriver


def get_cookie(user_name, password):
    driver = webdriver.Chrome()
    time.sleep(3)
    driver.get("https://weibo.com/login/")
    elem_user = driver.find_element_by_xpath('//input[@id="loginname"]')
    elem_user.send_keys(user_name)  # 浏览器版本不匹配的时候这里可能报错
    elem_pwd = driver.find_element_by_xpath('//input[@type="password"]')
    elem_pwd.send_keys(password)
    commit = driver.find_element_by_xpath('//span[@node-type="submitStates"]')
    commit.click()
    time.sleep(3)
    cookies = []
    cookie = {}
    if "微博-随时随地发现新鲜事" in driver.title:
        for elem in driver.get_cookies():
            cookie[elem["name"]] = elem["value"]
        if len(cookie) > 0:
            print("Get Cookie Successful: %s" % user_name)
            cookies.append(cookie)
    else:
        print("Get Cookie Failed: %s!" % user_name)
    driver.close()
    driver.quit()
    return cookies


if __name__ == '__main__':
    # user_name = '**********'
    # password = '***********'
    # cookies = get_cookie(user_name, password)
    # print(cookies)

    '''log in '''
    cookies = {'login_sid_t': '36a5da973bdf9e272a760547a5f42cd6', 'cross_origin_proto': 'SSL', 'ULV': '1540796385803:1:1:1:359950412832.14844.1540796385790:', 'TC-Ugrow-G0': 'e66b2e50a7e7f417f6cc12eec600f517', 'TC-V5-G0': 'c427b4f7dad4c026ba2b0431d93d839e', '_s_tentry': '-', 'WBStorage': 'e8781eb7dee3fd7f|undefined', 'SINAGLOBAL': '359950412832.14844.1540796385790', 'Apache': '359950412832.14844.1540796385790', 'wb_view_log': '1536*8641.25', 'SCF': 'Au6Sits5v-i7hWUS2VT1yOFlh-YNbLd4zgu0BH966iVEVGLp8S8HVLjTL0xJye7jDFbV-wAOX8wP0LsVEgDyMAA.', 'SUB': '_2A2520sDDDeRhGeRM71US9CjJzDmIHXVVqbULrDV8PUNbmtBeLVnCkW9NU_UPZnJaf3qP-q0-rUHWNLWvg9uairY-', 'SUHB': '0S7DbNozd1V5GG', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhBmmRnBaxNeiBH4gDbigTY5JpX5K2hUgL.FozEShM0ShqfS0-2dJLoI7_zBHigxHLkxXv1x7tt', 'ALF': '1572332556', 'SSOLoginState': '1540796563', 'un': '766842290@qq.com', 'wvr': '6', 'TC-Page-G0': '1ac1bd7677fc7b61611a0c3a9b6aa0b4', 'wb_view_log_2247346575': '1536*8641.25'}
    driver = webdriver.Chrome()
    time.sleep(3)
    driver.get("https://weibo.com/login/")
    for k in cookies:
        cookie = {}
        cookie.update(name=k)
        cookie.update(value=cookies[k])
        driver.add_cookie(cookie)
    driver.refresh()

    '''open comment box'''
    commit = driver.find_element_by_xpath('//span[@node-type="comment_btn_text"]')
    commit.click()
    time.sleep(3)

    '''write comment'''
    cmt_area = driver.find_element_by_xpath('//div[@class="p_input"]/textarea')
    time.sleep(1)
    cmt_area.send_keys("hello from alexandro's robot")

    '''submit comment'''
    comment = driver.find_element_by_xpath('//a[@node-type="btnText"]')
    comment.click()

    driver.close()
    driver.quit()
    print("comment successful")
