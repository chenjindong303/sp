from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import time
import datetime
from dateutil.relativedelta import relativedelta
import json
from jsonpath import jsonpath

import requests

_ts = int(time.time() * 1000)
# _ts = datetime.datetime.now()
# _ts_date_EndTime = _ts.strftime("%Y-%m-%d")
# _ts_date_BeginTime = (_ts - relativedelta(months=6)).strftime("%Y-%m-%d")
# print(_ts)
# print(_ts_date_EndTime)
# print(_ts_date_BeginTime)
data ={
    "ts": _ts,
    "pageNo": 6,  # page number
    "pageSize": 20,
    "total": 3644,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",  # 时间的三项要注意
    "BeginTime": "2024-03-23 00:00:00",
    "EndTime": "2024-09-23 23:59:59",
    "createTime": []
}
with open('p04md5-AES.js', encoding='utf-8') as f:
    js_code = f.read()

compile_obj = execjs.compile(js_code)
portal_sign = compile_obj.call("get_portal_sign", data)  # 调用方法
# print(portal_sign)
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://ggzyfw.fj.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://ggzyfw.fj.gov.cn/business/list/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "portal-sign": portal_sign,
    "sec-ch-ua": '"Chromium"";v="128", "Not;A=Brand";v="24", "Google"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
url = "https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo"

response = requests.post(url, headers=headers, data=str(data).encode('unicode_escape'))
# # print(response.text)
# # # print(response)
encrypt_data = json.loads(response.text)['Data']  # 返回的json-string 加密数据  AES加密
# print(encrypt_data)
res = compile_obj.call("get_data", encrypt_data)  # 调用方法
result_list = jsonpath(json.loads(res), "$..Table")[0]
for temp in result_list:
    item = dict()
    item["PLATFORM_NAME"] = temp["PLATFORM_NAME"]
    item["NAME"] = temp["NAME"]
    item["AREANAME"] = temp["AREANAME"]
    print(item)
