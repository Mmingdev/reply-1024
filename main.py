import os
from reply1024 import postreply1024
# from sel_def_logger import MyLog
import calendar
from datetime import datetime, timedelta

# mylogg = MyLog().logger
# mylogg.info("代码开始运行的时间{}".format(datetime.now()))
def handler(event, context):
    reply1024()
    return "Done"

def reply1024():
    HOST = os.getenv('HOST')
    COOKIES = os.getenv('COOKIES')
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')
    USER_ID = os.getenv('USER_ID')
    TEMPLATE_ID = os.getenv('TEMPLATE_ID')
    TARGET_URL = os.getenv('TARGET_URL')

    dict={'HOST':HOST,'COOKIES':COOKIES,'APP_ID':APP_ID,'APP_SECRET':APP_SECRET,'USER_ID':USER_ID,'TEMPLATE_ID':TEMPLATE_ID,'TARGET_URL':TARGET_URL}
    for i in dict:
        if dict[i]=="":
            raise EnvironmentError(f'Environment {i} not found!')

    postreply1024(HOST,COOKIES,APP_ID,APP_SECRET,USER_ID,TEMPLATE_ID,TARGET_URL).run()

if __name__ == '__main__':
    with open('tmp/temp.txt','r',encoding='utf-8') as file:
        text = file.read()
        lastupdate = text.split(":")[1]
    lastupdate = datetime.strptime(lastupdate,'%Y-%m-%d')
    lday = lastupdate.day
    now = datetime.now() + timedelta(hours=8)
    this_month_end = calendar.monthrange(now.year, now.month)[1]
    lastupdate = lastupdate + timedelta(days=1)
    w_content = "lastupdate:" + datetime.strftime(lastupdate,"%Y-%m-%d")
    with open("tmp/temp.txt","w") as file:
        file.write(w_content)
    if lday != this_month_end:
        reply1024()
    else:
        print("已到当月最后一天，明天需要更新")
