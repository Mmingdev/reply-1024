import os
import random
import traceback

from reply1024 import postreply1024
from sel_def_logger import MyLog
from time import sleep
from datetime import datetime, timedelta

mylogg = MyLog().logger
def handler(context):
    random_reply()
    return "Done"


def random_reply():
    HOST = os.getenv('HOST')
    COOKIES = os.getenv('COOKIES')
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')
    USER_ID = os.getenv('USER_ID')
    TEMPLATE_ID = os.getenv('TEMPLATE_ID')

    dict = {'HOST': HOST, 'COOKIES': COOKIES, 'APP_ID': APP_ID, 'APP_SECRET': APP_SECRET, 'USER_ID': USER_ID,
            'TEMPLATE_ID': TEMPLATE_ID}
    for i in dict:
        if dict[i] == "":
            raise EnvironmentError(f'Environment {i} not found!')

    cl1 = postreply1024(HOST, COOKIES, APP_ID, APP_SECRET, USER_ID, TEMPLATE_ID, '')
    res1 = cl1._getlist()
    if res1.text.find("普通主題") == -1:
        cl1._send_to_mp("获取列表失败")
        return

    res1 = res1.select('#tbody tr.tr3.t_one.tac td.tal h3 a')
    num = len(res1)
    post_s = 0
    wordlist = ['忽忘提肛，感谢分享',
                '感谢楼主辛苦分享',
                '不管怎么说先冲为敬',
                '感谢分享',
                '大佬辛苦，感谢分享',
                '看看大佬的分享',
                '精彩帖子，感谢楼主']
    if num >= 10:
        randlist = random.sample(range(num), 10)
        wordlist_new = cl1._getword(wordlist, 10)
    else:
        randlist = range(num)
        wordlist_new = cl1._getword(wordlist, num)

    # loop post
    for randn in randlist:
        tidurl = res1[randn].get("href")
        tid = res1[randn].get("id")[1:]
        atc_title = res1[randn].text
        atc_content = wordlist_new[post_s]
        if res1[randn].find('font', color="orange") != None or atc_title == "":
            continue
        # if ('求片求助貼' in atc_title) or ('[活动]' in atc_title) or ('[领奖帖]' in atc_title) or atc_title == "":
        #     continue

        wait = int(random.uniform(5, 10) * 1000) / 1000
        sleep(wait)
        res2 = cl1._visitthread(tidurl)
        if res2.text.find("快速回帖") == -1:
            print("前置帖子访问失败！")
            mylogg.error(f'前置帖子{tid}访问失败！')
        #     cl1._send_to_mp("前置帖子访问失败！")

        if post_s % 5 == 0 and post_s != 0:
            wait = int(random.uniform(300, 600) * 1000) / 1000
        else:
            wait = int(random.uniform(20, 60) * 1000) / 1000
        sleep(wait)
        replyres1 = cl1._postreply(atc_title, atc_content, tidurl, tid)
        if replyres1.text.find("發貼完畢點擊進入主題列表") != -1:
            post_s += 1

    tday = datetime.now() + timedelta(hours=8)
    if tday.hour < 20:
        with open("./tmp/test.txt", "r+") as f:
            n = f.read()
            f.seek(0)
            f.truncate()
            f.write(f"{int(n) + post_s}")
    else:
        with open("./tmp/test.txt", "r+") as f:
            n = f.read()
            f.seek(0)
            f.truncate()
            cl1._send_to_mp(f"今天成功回复 {post_s + int(n)} 个帖子")
            f.write("0")
    tday = tday.strftime("%Y-%m-%d %H:%M:%S")
    with open("./logs/runtime.log", "a+") as f:
        f.write(f"{tday} 成功回复{post_s}次\n")


if __name__ == '__main__':
    cltem = postreply1024('', '', '', '', '', '', '')
    try:
        random_reply()
    except BaseException:
        cltem._send_to_mp(traceback.format_exc())
