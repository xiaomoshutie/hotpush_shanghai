
import requests
import json

# 这里换成你自己的4个信息
CORP_ID = "ww2c237235fd708e8a"
CORP_SECRET = "MiAbYhw2az0bJIt85PwKKs7V7DPAl3Xjys7uWqGDjRY"
AGENT_ID = 1000003  # 你的AgentId
TO_USER = "ChenYiDa"  # 你的账号

def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={CORP_SECRET}"
    return requests.get(url).json()["access_token"]

def send_test():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}"
    data = {
        "touser": TO_USER,
        "msgtype": "text",
        "agentid": AGENT_ID,
        "text": {
            "content": "测试成功！企业微信正常啦"
        }
    }
    requests.post(url, data=json.dumps(data, ensure_ascii=False))

send_test()