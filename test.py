# from time import sleep
import os
import base64
from Crypto.Cipher import AES
# from reply1024 import postreply1024
# import time
# from datetime import datetime, timedelta

def add_to_16(value):
    while len(value.encode('utf8')) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# 加密方法
def encrypt_oracle(key, e_text):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(e_text))
    # 用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    encrypted_text = encrypted_text.strip()  # strip， 后面会有一个换行符
    return encrypted_text

# 解密方法
def decrypt_oralce(key, d_text):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(d_text.encode(encoding='utf-8'))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    return decrypted_text


APP_ID = os.getenv('APP_ID')
APP_SECRET = os.getenv('APP_SECRET')
USER_ID = os.getenv('USER_ID')
TEMPLATE_ID = os.getenv('TEMPLATE_ID')

key = '123'
e_id = encrypt_oracle(key,APP_ID)
e_sec = encrypt_oracle(key,APP_SECRET)
e_uid = encrypt_oracle(key,USER_ID)
e_tid = encrypt_oracle(key,TEMPLATE_ID)
print(e_id)
print(e_sec)
print(e_uid)
print(e_tid)
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