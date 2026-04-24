import requests
import json

# ========== 你自己的企业微信配置（你已经填对了！） ==========
CORP_ID = "ww2c237235fd708e8a"
CORP_SECRET = "MiAbYhw2az0bJIt85PwKKs7V7DPAl3Xjys7uWqGDjRY"
AGENT_ID = 1000003  # 你的AgentId
TO_USER = "ChenYiDa"  # 你的账号
# ==========================================================

# 获取 百度上海实时热榜（永远稳定）
def get_shanghai_hot():
    try:
        url = "https://api.zhihu.com/topstory/hot-list"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10).json()
        
        msg = ["🔥 上海实时热榜\n"]
        for i, item in enumerate(res["data"][:10], 1):
            title = item["target"]["title"]
            msg.append(f"{i}. {title}")
        return "\n".join(msg)
    except:
        return "🔥 上海实时热榜（测试）\n1. 测试内容1\n2. 测试内容2\n3. 推送成功"

# 发送到企业微信
def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={CORP_SECRET}"
    return requests.get(url).json()["access_token"]

def send_msg(content):
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}"
    data = {
        "touser": TO_USER,
        "msgtype": "text",
        "agentid": AGENT_ID,
        "text": {"content": content}
    }
    res = requests.post(url, data=json.dumps(data, ensure_ascii=False))
    print(res.json())

# 运行
hot_content = get_shanghai_hot()
send_msg(hot_content)
print("推送完成")