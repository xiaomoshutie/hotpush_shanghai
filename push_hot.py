import requests

# ===================== 你的配置 =====================
SERVER_KEY = "SCT153697TKg0PE4GwaENyIfu9ANvinW36"
# ====================================================

# 获取头条热榜
def get_toutiao():
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
        return "【今日头条获取失败】"

# 获取抖音热榜
def get_douyin():
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
        return "\n【抖音获取失败】"

# 获取微信热榜
def get_wechat():
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
        return "\n【微信热榜获取失败】"

# 推送到 Server酱
def push_server(title, content):
    url = f"https://sctapi.ftqq.com/{SERVER_KEY}.send"
    data = {
        "title": title,
        "desp": content
    }
    try:
        requests.post(url, data=data)
    except:
        pass

# 主程序
if __name__ == "__main__":
    t1 = get_toutiao()
    t2 = get_douyin()
    t3 = get_wechat()
    content = t1 + t2 + t3
    push_server("🔥 上海实时热榜（头条+抖音+微信）", content)
    print("推送成功！")