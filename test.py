from time import sleep
import os
from reply1024 import postreply1024
# import time
from datetime import datetime, timedelta

APP_ID = os.getenv('APP_ID')
APP_SECRET = os.getenv('APP_SECRET')
USER_ID = os.getenv('USER_ID')
TEMPLATE_ID = os.getenv('TEMPLATE_ID')
time1 = datetime.now() + timedelta(hours=8)
# time1 = time1.strftime("%Y-%m-%d %H:%M:%S")
time2=datetime(time1.year,time1.month,time1.day,16,40,0,0)
n=(time2-time1).seconds
print(f'time1={time1},type={type(time1)}')
print(f'time2={time2},type={type(time2)}')
print(f"time2-time1={n}")
sleep(n)
time3 = datetime.now() + timedelta(hours=8)
cl1 = postreply1024('', '', APP_ID, APP_SECRET, USER_ID, TEMPLATE_ID, '')
msg=f'{time1}~{time2}~{time3}'
cl1._send_to_mp(msg)