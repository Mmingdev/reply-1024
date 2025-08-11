# from time import sleep
import os
# from reply1024 import postreply1024
# import time
from datetime import datetime, timedelta

APP_ID = os.getenv('APP_ID')
APP_SECRET = os.getenv('APP_SECRET')
USER_ID = os.getenv('USER_ID')
TEMPLATE_ID = os.getenv('TEMPLATE_ID')
x1='##{}'.format(APP_ID)
x2='##{}'.format(APP_SECRET)
x3='##{}'.format(USER_ID)
x4='##{}'.format(TEMPLATE_ID)
print('{},{},{},{}'.format(x1,x2,x3,x4))
# tday = datetime.now()+timedelta(hours = 8)
# print(tday.hour)
# tday.strftime("%Y-%m-%d %H:%M:%S")
# print(tday)
# if os.path.isdir("tmp")==0:
#     os.mkdir("tmp")
#
# with open("./tmp/test.txt","r+") as f:
#     # f.write(f"{tday} 成功添加一行内容\n")
#     con=f.read()
#     a=60
#     f.seek(0)
#     f.truncate()
#     f.write(f"{int(con)+a}")
# # print(f"文件关闭了吗：{f.closed}")
# with open("./tmp/test.txt") as f:
#     con=f.read()
#
# # print(f"文件关闭了吗：{f.closed}")
# print("读取内容：",con)