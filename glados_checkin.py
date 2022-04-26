import requests
import os
import json


def checkin(cookie):
    checkin_url = "https://glados.one/api/user/checkin"
    
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    "cookie": cookie}

    data = {"token":"glados_network"}

    response = requests.post(checkin_url, headers=headers, data=data).text
    dict_response = json.loads(response)

    if dict_response['message'] in ["Checkin! Get 1 Day", "Please Try Tomorrow"]:
        print('打卡成功！')
    else:
        print('打卡失败！')                    
        print(dict_response['message'])

if __name__ == "__main__":
    cookie =  os.environ.get('cookie')
    checkin(cookie)
