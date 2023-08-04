import requests
import json
import time
import schedule
import os

def JueJin():
    cookie = os.environ["JUEJIN_COOKIE"];
    SENDKEY = os.environ["JUEJIN_SENDKEY"];
    data = os.environ["JUEJIN_DATA"];
    print("cookie: " + cookie);
    print("data: " + data);
    print("sendkey: " + SENDKEY);
    return _request(cookie, data, SENDKEY);


def _request(cookie, data, SENDKEY):
    msg = "";
    # 签到接口
    check_in = requests.post("https://api.juejin.cn/growth_api/v1/check_in", headers={"cookie": cookie}, data=data);
    
    if check_in.json()["err_no"] == 0:
        # 抽奖接口
        draw = requests.post("https://api.juejin.cn/growth_api/v1/lottery/draw", headers={"cookie": cookie}, params=data);

        if draw.json()["err_no"] == 0:
            data = draw.json()["data"];
            msg = "掘金签到成功！免费一次抽奖结果为 【" + data["lottery_name"] + "】";
        else:
            msg = draw.json()["err_msg"];
    else:
        msg = "掘金签到失败！原因：" + check_in.json()["err_msg"];

    try:
        # 获取围观列表接口
        watcherList = requests.post("https://api.juejin.cn/growth_api/v1/lottery_history/global_big", headers={"cookie": cookie}, params=data,data={
            "page_no":1,
            "page_size":5
        });
        history = watcherList.json()["data"]["lotteries"][0];
        print("围观用户日志:"+history)
        # 沾喜气接口
        joyful = requests.post("https://api.juejin.cn/growth_api/v1/lottery_lucky/dip_lucky", headers={"cookie": cookie}, params=data,data={
            "history_id":history["history_id"]
        });
        res = joyful.json();
        print("沾喜气日志:"+res)
        if res["err_no"] == 0:
            if not res["data"]["has_dip"]:
                user_name = history["user_name"]
                msg += f"你沾了一下 {user_name} 的喜气，幸运值增加了 10 点，下次抽奖说不定能抽中";
            else:
                msg += "今天你已经沾过喜气，明天再来吧！据说坚持不懈的姿势，持续访问稀土掘金，抽中大奖几率更高噢～";
        else:
            msg += res["err_msg"];
    except Exception as e:
       msg += "沾喜气失败！";

    requests.get("https://sctapi.ftqq.com/" + SENDKEY + ".send", params={"title": "python掘金签到", "desp": msg});
    
    return msg;

if __name__ == "__main__":
    print("掘金签到： " + JueJin());
    # 每天8点执行一次
    # schedule.every().day.at("08:00").do(WuChunTaoJueJin);
    # schedule.every().day.at("08:00").do(DmJueJin);
    # while True:
    #     schedule.run_pending();
    #     time.sleep(1);
