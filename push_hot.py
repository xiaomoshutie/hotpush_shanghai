import requests
import json

# ========== 企业微信配置（把你上面的4个参数填进来） ==========
CORP_ID = "ww2c237235fd708e8a"
CORP_SECRET = "MiAbYhw2az0bJIt85PwKKs7V7DPAl3Xjys7uWqGDjRY"
AGENT_ID = 1000003  # 你的AgentId
TO_USER = "ChenYiDa"  # 你的账号
# ======================================================

# 今日头条热榜（稳定接口）
def get_toutiao():
    try:
        url = "https://api.oioweb.cn/api/toutiao/hot"
        res = requests.get(url, timeout=10)
        data = res.json()
        lines = ["【今日头条热榜】"]
        for i, item in enumerate(data.get("data", [])[:8]):
            lines.append(f"{i+1}. {item['title']}")
        return "\n".join(lines)
    except:
        return "【今日头条热榜获取失败】"

# 抖音热榜（稳定接口）
def get_douyin():
    try:
        url = "https://api.oioweb.cn/api/douyin/hot"
        res = requests.get(url, timeout=10)
        data = res.json()
        lines = ["\n【抖音热榜】"]
        for i, item in enumerate(data.get("data", [])[:8]):
            lines.append(f"{i+1}. {item['title']}")
        return "\n".join(lines)
    except:
        return "\n【抖音热榜获取失败】"

# 微信公众号热榜（稳定接口）
def get_wechat():
    try:
        url = "https://api.oioweb.cn/api/wechat/hot"
        res = requests.get(url, timeout=10)
        data = res.json()
        lines = ["\n【微信公众号热榜】"]
        for i, item in enumerate(data.get("data", [])[:8]):
            lines.append(f"{i+1}. {item['title']}")
        return "\n".join(lines)
    except:
        return "\n【微信热榜获取失败】"

# ==================== 企业微信推送 ====================
def get_access_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={CORP_SECRET}"
    res = requests.get(url)
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
        requests.post(url, data=json.dumps(data, ensure_ascii=False))
    except:
        pass

# 主程序
if __name__ == "__main__":
    content = get_toutiao() + get_douyin() + get_wechat()
    send_msg(content)
    print("推送完成")