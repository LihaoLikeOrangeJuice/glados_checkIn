import json
import logging
import os

import requests


def checkin():
    cookie = os.environ.get('cookie')

    checkin_url = "https://glados.one/api/user/checkin"

    headers = {
        "user-agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
        "cookie": cookie
    }

    data = {"token": "glados.network"}

    response = requests.post(checkin_url, headers=headers, data=data).text
    dict_response = json.loads(response)

    if dict_response['message'] in [
            "Checkin! Get 1 Day", "Please Try Tomorrow"
    ]:
        title = content = "GLADOS打卡成功"

        logging.info("GLADOS打卡成功")

    else:
        content = dict_response['message']
        title = "GLADOS打卡失败"

        logging.error("GLADOS打卡失败\n" + response)

    token = os.environ.get('token')

    push_data = {"token": token, "title": title, "content": content}

    push_url = "http://www.pushplus.plus/send/"

    requests.post(push_url, data=push_data)


def start(event=0, context=0):
    logging.basicConfig(
        format='%(name)s - %(levelname)s - %(module)s: %(message)s')

    checkin()
