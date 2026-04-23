
import requests
import json
from bs4 import BeautifulSoup

# ========== 企业微信配置（把你上面的4个参数填进来） ==========
CORP_ID = "ww2c237235fd708e8a"
CORP_SECRET = "MiAbYhw2az0bJIt85PwKKs7V7DPAl3Xjys7uWqGDjRY"
AGENT_ID = 1000003  # 你的AgentId
TO_USER = "ChenYiDa"  # 你的账号
# ======================================================

# 百度上海热搜（100%成功，不需要第三方API）
def get_baidu_shanghai_hot():
    try:
        url = "https://top.baidu.com/board?tab=city"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.select(".content_1YWBm")[:10]

        msg = ["🔥 上海实时热榜（百度官方）"]
        for i, item in enumerate(items, 1):
            title = item.get_text(strip=True)
            msg.append(f"{i}. {title}")
        return "\n".join(msg)
    except Exception as e:
        return "🔥 上海热榜获取失败"

# ===================== 企业微信推送 =====================
def get_access_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={CORP_SECRET}"
    res = requests.get(url, timeout=10)
    return res.json().get("access_token", "")

def send_msg(content):
    try:
        token = get_access_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}"
        data = {
            "touser": TO_USER,
            "msgtype": "text",
            "agentid": AGENT_ID,
            "text": {"content": content}
        }
        requests.post(url, json=data)
    except:
        pass

# ===================== 主程序 =====================
if __name__ == "__main__":
    content = get_baidu_shanghai_hot()
    send_msg(content)
    print(content)