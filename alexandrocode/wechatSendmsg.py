import itchat
import time


def send_msg(nickname, message):
    friend_name = itchat.search_friends(name=nickname)
    name = friend_name[0]['UserName']
    itchat.send_msg(msg=message, toUserName=name)


if __name__ == '__main__':

    itchat.auto_login()
    nickname = ['Alexandro', 'Shawn chen', 'sherry', 'Sunny', 'TianLi', 'Jacob', 'ShiRyan', 'Joyce Zhang', 'Harry Shen', 'Nancy Fei']

    for name in nickname:
        message = 'Hello' + name + "from alexandro's robot"
        send_msg(name, message)
        time.sleep(0.001)

    itchat.logout()