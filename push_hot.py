import requests
import json
import time

# ========== 企业微信配置（把你上面的4个参数填进来） ==========
CORP_ID = "ww2c237235fd708e8a"
CORP_SECRET = "MiAbYhw2az0bJIt85PwKKs7V7DPAl3Xjys7uWqGDjRY"
AGENT_ID = 1000003  # 你的AgentId
TO_USER = "ChenYiDa"  # 你的账号
# ======================================================

# 稳定头条热榜
def get_toutiao():
    try:
        url = "https://api.vvhan.com/api/hotlist/toutiao"
        res = requests.get(url, timeout=15)
        data = res.json()
        lines = ["【今日头条热榜】"]
        for i, item in enumerate(data.get("data", [])[:7], 1):
            lines.append(f"{i}. {item.get('title', '无标题')}")
        return "\n".join(lines)
    except Exception as e:
        return "【今日头条热榜：获取失败】"

# 稳定抖音热榜
def get_douyin():
    try:
        url = "https://api.vvhan.com/api/hotlist/douyin"
        res = requests.get(url, timeout=15)
        data = res.json()
        lines = ["\n【抖音热榜】"]
        for i, item in enumerate(data.get("data", [])[:7], 1):
            lines.append(f"{i}. {item.get('title', '无标题')}")
        return "\n".join(lines)
    except:
        return "\n【抖音热榜：获取失败】"

# 稳定微信热榜
def get_wechat():
    try:
        url = "https://api.vvhan.com/api/hotlist/wechat"
        res = requests.get(url, timeout=15)
        data = res.json()
        lines = ["\n【微信公众号热榜】"]
        for i, item in enumerate(data.get("data", [])[:7], 1):
            lines.append(f"{i}. {item.get('title', '无标题')}")
        return "\n".join(lines)
    except:
        return "\n【微信热榜：获取失败】"

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
        requests.post(url, json=data, timeout=10)
    except:
        pass

# ===================== 主程序 =====================
if __name__ == "__main__":
    content = get_toutiao() + get_douyin() + get_wechat()
    send_msg(content)
    print("推送完成：", content)