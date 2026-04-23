import requests
import json

# ========== 把你自己的4个信息填对 ==========
CORP_ID = "ww2c237235fd708e8a"
CORP_SECRET = "MiAbYhw2az0bJIt85PwKKs7V7DPAl3Xjys7uWqGDjRY"
AGENT_ID = 1000003  # 你的AgentId
TO_USER = "ChenYiDa"  # 你的账号
# ==========================================

def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={CORP_SECRET}"
    res = requests.get(url)
    print("gettoken 返回:", res.json())
    return res.json().get("access_token", "")

def send_test():
    token = get_token()
    if not token:
        print("拿不到 token，ID 或 Secret 错了")
        return

    url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}"
    data = {
        "touser": TO_USER,
        "msgtype": "text",
        "agentid": AGENT_ID,
        "text": {
            "content": "测试消息，收到回我！"
        }
    }
    res = requests.post(url, data=json.dumps(data, ensure_ascii=False))
    print("发送返回:", res.json())

send_test()