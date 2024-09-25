from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import requests
from urllib.parse import urlparse
import json
from jsonpath import jsonpath

url = "https://www.kanzhun.com/api_to/ranklist/company_list_search.json"
e = {
    "data": {
        "bannerTypeCodes": "2802",  # 不同的企业类型是不同的代码  可以调整
        "pageNum": 20,  # 页码数  可以调整
        "provinceCodes": ""
    },
    "url": urlparse(url).path,  # 网址
    "method": "get"
}
with open('p05.js', encoding='utf-8') as f:
    js_code = f.read()

compile_obj = execjs.compile(js_code)
params_aes = compile_obj.call("a", e)  # 调用方法
# print(res)

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded;charset=utf-8",
    "cookie": "wd_guid=037dd866-a054-49bc-bedf-00d6ce0c541d; historyState=state; __c=1727226962; __g=-; __l=l=%2Fwww.kanzhun.com%2Frank_l%2Fa2813%2F%3Fka%3Dindex_list_detail_click&r=; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1727106338,1727226962; HMACCOUNT=B5676A9F620DE626; __a=20501149.1727106339.1727106339.1727226962.13.2.8.13; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1727228889",
    "href": "https://www.kanzhun.com/rank_l/a2801/",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.kanzhun.com/rank_l/a2801/",
    "reqsource": "fe",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceid": "F-786f1cc3Gerc45Oa",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

params = params_aes
# print(params)
response = requests.get(url, headers=headers, params=params)
# print(response.text)
# print(response)
encrypt_data = response.text
res = compile_obj.call("c", encrypt_data, params_aes['kiv'])  # 调用方法
# print(res)  # 得到返回值
result_list = jsonpath(json.loads(res), "$..dataList")[0]
for temp in result_list:
    item = dict()
    item["companyName"] = temp["companyName"]
    item["encCompanyId"] = temp["encCompanyId"]
    item["logo"] = temp["logo"]
    print(item)
