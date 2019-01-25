import itchat
import requests
import json
import schedule
import time
import threading
from bs4 import BeautifulSoup


# tuling robot
def turing(info):
    appkey = "e37258e7df3547b49fe92534309c3bec"   #"e5ccc9c7c8834ec3b08940e290ff1559"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey, info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer


# wechat auto response
@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', 'Picture'], isGroupChat=False)
def text_reply(msg):
    print("收到一条信息")
    answer = turing(msg['Text'])
    print(answer)
    print(msg['FromUserName'])

    global flag0
    if msg['Text'] == '自动回复':
        flag0 = 1
    elif msg['Text'] == '取消自动回复':
        flag0 = 0

    if flag0 == 1:
        itchat.send_msg(answer, msg['FromUserName']) #"%s  --by alex's robot" %
        itchat.send_msg(answer, 'filehelper')#"%s  --by alex's robot" %
    else:
        itchat.send_msg(answer, 'filehelper')

# group news
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)    #群消息的处理
def print_content(msg):
    if msg.User["NickName"] == '各种喜提聚餐群'or msg.User["NickName"]=='另外一个你希望自动回复群的名字':    #这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字'
        answer = turing(msg['Text'])
        print(msg.User['NickName'] +":"+ msg['Text'])     #打印哪个群给你发了什么消息
        print(answer)                                       #打印机器人回复的消息
        itchat.send_msg(answer, 'filehelper')
        return answer
    else:                                         #其他群聊直接忽略
        pass


def job_joke():
    data = requests.get(r"https://www.qiushibaike.com/").text
    soup = BeautifulSoup(data, 'html.parser')
    targets = soup.find('div', class_='content')
    joke = "开心一刻：" + targets.span.text
    print(joke)
    itchat.send_msg(joke, 'filehelper')


def job_weather():
    itchat.send_msg("job_weather is working", 'filehelper')


def job_words():
    data = requests.get(r"https://www.dailyenglishquote.com/").text
    soup = BeautifulSoup(data, 'html.parser')
    targets = soup.find('strong', style='color: #0b5394;')
    words = "每日一句：" + targets.text
    print(words)
    itchat.send_msg(words, 'filehelper')


def routine_msg():
    schedule.every().day.at("8:00").do(job_weather)
    schedule.every().day.at("8:30").do(job_words)
    schedule.every().day.at("9:00").do(job_joke)
    schedule.every().day.at("10:00").do(job_joke)
    schedule.every().day.at("14:00").do(job_joke)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    '''log in we chat'''
    flag0 = 1
    itchat.auto_login(hotReload=True)
    t1 = threading.Thread(target=routine_msg)
    t1.start()
    itchat.run()

