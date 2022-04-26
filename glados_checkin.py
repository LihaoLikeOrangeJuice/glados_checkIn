import requests
import os
import json


def checkin(cookie, token):
    checkin_url = "https://glados.one/api/user/checkin"
    
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    "cookie": cookie}

    data = {"token":"glados_network"}

    response = requests.post(checkin_url, headers=headers, data=data).text
    dict_response = json.loads(response)

    if dict_response['message'] in ["Checkin! Get 1 Day", "Please Try Tomorrow"]:
        content = "GLADOS打卡成功"
        title = "GLADOS打卡成功"
    else:
        content = 'GLADOS打卡失败\n'+dict_response['message']                    
        title = "GLADOS打卡失败"

    push_data = {
    "token":token,
    "title":title,
    "content":content
}

    push_url = "http://www.pushplus.plus/send/"

    response = requests.post(push_url, data=push_data).text

    print(response)
        

def main(event, context):
    token = os.environ.get('token')
    cookie =  os.environ.get('cookie')
    checkin(cookie, token)
