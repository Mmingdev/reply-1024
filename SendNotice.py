from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
from datetime import datetime, timedelta
import random


def _get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)
def _send_to_mp(_app_id,_app_secret,_user_id,_template_id,msg: str):
    tday = datetime.now() + timedelta(hours=8)
    tday = tday.strftime("%Y-%m-%d %H:%M:%S")
    client = WeChatClient(_app_id, _app_secret)
    wm = WeChatMessage(client)
    data = {
        "date": {"value": format(tday), "color": _get_random_color()},
        "re": {"value": msg, "color": _get_random_color()},
    }
    res = wm.send_template(_user_id, _template_id, data)

if __name__ == '__main__':
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')
    USER_ID = os.getenv('USER_ID')
    TEMPLATE_ID = os.getenv('TEMPLATE_ID')
    data = "已到1号，记得更新。"
    _send_to_mp(APP_ID,APP_SECRET,USER_ID,TEMPLATE_ID,data)