import requests
import json

# ========== 企业微信配置（把你上面的4个参数填进来） ==========
CORP_ID = "ww2c237235fd708e8a"
CORP_SECRET = "MiAbYhw2az0bJIt85PwKKs7V7DPAl3Xjys7uWqGDjRY"
AGENT_ID = 1000003  # 你的AgentId
TO_USER = "ChenYiDa"  # 你的账号

# ========== 热榜抓取 ==========
def get_toutiao():
    try:
        url = "https://www.topbiz360.cn/api/open/hot/list?code=toutiao"
        res = requests.get(url, timeout=10)
        data = res.json()
        items = data.get("data", [])[:8]
        lines = ["【今日头条热榜】"]
        for i, item in enumerate(items, 1):
            lines.append(f"{i}. {item.get('title', '')}")
        return "\n".join(lines)
    except:
        return "头条热榜获取失败"

def get_douyin():
    try:
        url = "https://www.topbiz360.cn/api/open/hot/list?code=douyin"
        res = requests.get(url, timeout=10)
        data = res.json()
        items = data.get("data", [])[:8]
        lines = ["\n【抖音热榜】"]
        for i, item in enumerate(items, 1):
            lines.append(f"{i}. {item.get('title', '')}")
        return "\n".join(lines)
    except:
        return "\n抖音热榜获取失败"

def get_wechat():
    try:
        url = "https://www.topbiz360.cn/api/open/hot/list?code=wechat"
        res = requests.get(url, timeout=10)
        data = res.json()
        items = data.get("data", [])[:8]
        lines = ["\n【微信热榜】"]
        for i, item in enumerate(items, 1):
            lines.append(f"{i}. {item.get('title', '')}")
        return "\n".join(lines)
    except:
        return "\n微信热榜获取失败"

# ========== 企业微信推送核心代码 ==========
def get_access_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={CORP_SECRET}"
    res = requests.get(url)
    return res.json()["access_token"]

def send_wechat_message(content):
    try:
        token = get_access_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}"
        msg = {
            "touser": TO_USER,
            "msgtype": "text",
            "agentid": AGENT_ID,
            "text": {"content": content},
            "safe": 0
        }
        res = requests.post(url, data=json.dumps(msg, ensure_ascii=False))
        print(res.json())
    except Exception as e:
        print("推送失败", e)

# ========== 主程序 ==========
if __name__ == "__main__":
    content = get_toutiao() + get_douyin() + get_wechat()
    send_wechat_message(content)
    print("推送完成")