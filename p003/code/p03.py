from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

import requests
import json
from jsonpath import jsonpath


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://jzsc.mohurd.gov.cn/data/company",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accessToken": "jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLXMO9t1XclQODlSCTx3sixlhpUUKvcMtoMqfGfwdLCb8g==",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^128^^, ^\\^Not;A=Brand^^;v=^\\^24^^, ^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^^",
    "timeout": "30000",
    "v": "231012"
}
cookies = {
    "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1726629503,1727074326",
    "HMACCOUNT": "B5676A9F620DE626",
    "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1727074779"
}
url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"
params = {
    "pg": "3",
    "pgsz": "15",
    "total": "450"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

# print(response.text)
# print(response)

data = response.text
with open('p03返回AES.js', encoding='utf-8') as f:
    js_code = f.read()

compile_obj = execjs.compile(js_code)
result1 = compile_obj.call("b", data)  # 调用方法，依次传递参数
# print(result1)  # 得到返回值, 并带入参数
res_list = jsonpath(json.loads(result1), "$..list")[0]
for res in res_list:
    item = dict()
    item['QY_NAME'] = res['QY_NAME']
    item['QY_FR_NAME'] = res['QY_FR_NAME']
    item['QY_REGION'] = res['QY_REGION']
    print(item)

