from time import sleep

from reply1024 import postreply1024
# import time
from datetime import datetime, timedelta

time1 = datetime.now() + timedelta(hours=8)
# time1 = time1.strftime("%Y-%m-%d %H:%M:%S")
time2=datetime(time1.year,time1.month,time1.day,14,50,0,0)
n=(time2-time1).seconds
print(f'time1={time1},type={type(time1)}')
print(f'time2={time2},type={type(time2)}')
print(f"time2-time1={n}")
sleep(n)
time3 = datetime.now() + timedelta(hours=8)
cl1=postreply1024('','','','','','','')
msg=f'{time1}~{time2}~{time3}'
cl1._send_to_mp(msg)