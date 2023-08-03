import os
from reply1024 import postreply1024
from sel_def_logger import MyLog
from datetime import datetime

mylogg = MyLog().logger
mylogg.info("代码开始运行的时间{}".format(datetime.now()))
def handler(event, context):
    reply1024()
    return "Done"

def reply1024():
    # HOST = os.getenv('HOST')
    HOST = "https://cl.2612x.xyz"
    # COOKIES = os.getenv('COOKIES')
    COOKIES = "227c9_ck_info=%2F%09; 227c9_winduser=UgJVUwoEMVUIAABTW1NVVlddVFcAXQtQDlZWUw4DVlZXVwNSBwdVbVYDAFAAXwtQBlABUgcFBwdRXAQMWwBRXlxTAFZQBARQ; 227c9_groupid=9; 227c9_ipfrom=3162d43e678523a4103b2b64f6529318%09Unknown; 227c9_postReplyLastData=5862455%E6%95%B4%E7%90%86%E8%BE%9B%E8%8B%A6%EF%BC%8C%E7%AD%9B%E9%80%89%E7%9C%8B%E7%9C%8B; 227c9_lastvisit=0%091690971412%09%2Fpersonal.php%3Faction%3Dpost"
    # APP_ID = os.getenv('APP_ID')
    APP_ID='wx9d76a93fb0605d9c'
    # APP_SECRET = os.getenv('APP_SECRET')
    APP_SECRET ='4c4f06b2dd2f6343b39eb51d3817aebf'
    # USER_ID = os.getenv('USER_ID')
    USER_ID ='o9Tf-6kWBMVUijef5sC3na9Q9dZQ'
    # TEMPLATE_ID = os.getenv('TEMPLATE_ID')
    TEMPLATE_ID ='3aljWa0ByVElJHdqq_H3x6bh3UncW5-BZ-j2c8q-HJg'
    # TARGET_URL = os.getenv('TARGET_URL')
    TARGET_URL='htm_data/2308/7/5862277.html'

    dict={'HOST':HOST,'COOKIES':COOKIES,'APP_ID':APP_ID,'APP_SECRET':APP_SECRET,'USER_ID':USER_ID,'TEMPLATE_ID':TEMPLATE_ID,'TARGET_URL':TARGET_URL}
    for i in dict:
        if dict[i]=="":
            raise EnvironmentError(f'Environment {i} not found!')
    # if HOST is None:
    #     raise EnvironmentError('Environment HOST not found!')
    # if COOKIES is None:
    #     raise EnvironmentError('Environment COOKIES not found!')
    postreply1024(HOST,COOKIES,APP_ID,APP_SECRET,USER_ID,TEMPLATE_ID,TARGET_URL).run()

if __name__ == '__main__':
    reply1024()
