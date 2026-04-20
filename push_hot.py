import requests
import time

# ===================== 你的配置 =====================
PUSHPLUS_TOKEN = "223d880dd65a470093c4e541acbcc4b8"
# ====================================================

def get_toutiao_shanghai():
    try:
        url = "https://www.topbiz360.cn/api/open/hot/list?code=toutiao"
        res = requests.get(url, timeout=10)
        data = res.json()
        items = data.get("data", [])[:7]
        lines = ["【今日头条·上海热榜】"]
        for i, item in enumerate(items, 1):
            title = item.get("title", "")
            hot = item.get("hot", "")
            lines.append(f"{i}. {title} {hot}")
        return "\n".join(lines)
    except:
        return "【今日头条热榜获取失败】"

def get_douyin_shanghai():
    try:
        url = "https://www.topbiz360.cn/api/open/hot/list?code=douyin"
        res = requests.get(url, timeout=10)
        data = res.json()
        items = data.get("data", [])[:7]
        lines = ["\n【抖音·上海热榜】"]
        for i, item in enumerate(items, 1):
            title = item.get("title", "")
            lines.append(f"{i}. {title}")
        return "\n".join(lines)
    except:
        return "\n【抖音热榜获取失败】"

def get_wechat_shanghai():
    try:
        url = "https://www.topbiz360.cn/api/open/hot/list?code=wechat"
        res = requests.get(url, timeout=10)
        data = res.json()
        items = data.get("data", [])[:7]
        lines = ["\n【微信公众号·热榜】"]
        for i, item in enumerate(items, 1):
            title = item.get("title", "")
            lines.append(f"{i}. {title}")
        return "\n".join(lines)
    except:
        return "\n【公众号热榜获取失败】"

def push_to_wechat(content):
    url = "http://www.pushplus.plus/send"
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "🔥 上海实时热榜",
        "content": content,
        "template": "txt"
    }
    try:
        requests.post(url, json=data, timeout=10)
    except:
        pass

if __name__ == "__main__":
    t1 = get_toutiao_shanghai()
    t2 = get_douyin_shanghai()
    t3 = get_wechat_shanghai()
    content = t1 + t2 + t3
    push_to_wechat(content)
    print("推送完成")