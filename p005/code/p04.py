from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import time
import requests

_ts = str(int(time.time()*1000))
# print(_ts)

i7b = {
    "rid": "A_PL_0_19723756",
    "threadId": "A_PL_0_19723756",
    "pageNo": "3",
    "pageSize": "20",
    "cursor": _ts,
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}

with open('p04网易云评论.js', encoding='utf-8') as f:
    js_code = f.read()

compile_obj = execjs.compile(js_code)
result1 = compile_obj.call("get_para", i7b)  # 调用方法，依次传递参数
# print(result1)  # 得到返回值, 并带入参数
encText = result1['encText']
encSecKey = result1['encSecKey']
#
# print("encText--->", encText)
# print("encSecKey--->", encSecKey)

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "__root_domain_v=.163.com; _qddaz=QD.706123817838892; NMTID=00OXpDhtI6D08v-VERwpWZIyGvD0oYAAAGRZfd1JQ; _iuqxldmzr_=32; _ntes_nnid=fd7c6554199f19b1c6c36476e6b4a158,1723992599283; _ntes_nuid=fd7c6554199f19b1c6c36476e6b4a158; WEVNSM=1.0.0; WNMCID=mwgirt.1723992599912.01.0; WM_TID=3MQL%2FxpF8t9FRABBBFaGFz02%2Bytr6DoZ; sDeviceId=YD-OrreZ2Y692NAU0EBEFaDRnknvzt%2BulBg; ntes_utid=tid._.uMcfIlInKT5EVgEFAQbXBjwi6ip%252F7kUD._.0; hb_MA-93D5-9AD06EA4329A_source=www.bing.com; JSESSIONID-WYYY=J%5CefSQq%2BvxrO%2FvK8U0BMQMt%2B%2Bd4CR9EjVe%5CnC%2BYJ%5CPBjy0oPy9MJX0MBpT0WdR%5CVf3JcUph%2B7xzFYXpwfwt%2FWl2AveTYrFsTVsiVwBfZrNXRsS%2BMIa%5C2VMURt3thPGCzDZKV3ZgnEwOTTKlOaFmUU8ewd7ifeCZhqEC10KSPtVF91XZk%3A1727579294243; WM_NI=PxNYj4%2B1M27sR3wM%2Ffm4EUc3GVWcYW7AQh8g%2BDr%2BKAf4oJwpqkkiqUJWaRBonLBJfmD%2FYpQAcs1nRDmAvh75f4yzrQ1DlvTpBa%2FM0qbzFBFiHxxDaXLd4prL%2Bedx6j29YUo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed7fc488bbf9ed8fc7b88eb8ea2d85e939a8f82c66093e9ae8ac65988efaf90bb2af0fea7c3b92a94a882bae940e9ef83d3b67992edb9aeae6eafec8bb6e239858a9984dc5df59f9f89bb6de99cbeccca4ba6eca1abf67cb3b5a58af45f8a89afb3c165ae948eabe56788f19791d44ba1adff8fd150af9fba89b63fa6ecb79bf15bf39ca497d77c82bfe1aeb37ba2a68aa3c5638ca8b8a5e45490bcfc91f148e9bbac99b562f2e797b6ee37e2a3",
    "origin": "https://music.163.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://music.163.com/discover/toplist",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
url = "https://music.163.com/weapi/comment/resource/comments/get"
params = {
    "csrf_token": ""
}
data = {
    "params": encText,
    "encSecKey": encSecKey
}
response = requests.post(url, headers=headers, params=params, data=data)

print(response.json())
print(response)
