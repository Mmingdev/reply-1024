import os
from reply1024 import postreply1024
# from sel_def_logger import MyLog
# from datetime import datetime

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
    reply1024()
