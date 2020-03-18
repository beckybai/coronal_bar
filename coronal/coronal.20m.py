#!/usr/bin/env PYTHONIOENCODING=UTF-8  /Users/kebai/anaconda3/bin//python
# -*-coding:utf-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup
url = 'https://www.dealmoon.com/guide/934164' # 数据地址,从浏览器copy
header = {
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate, sdch',
     'Accept-Language': 'zh-CN,zh;q=0.8',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.  2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400'
 }
timeout = random.choice(range(80, 180)) # 超时时间
req = requests.get(url, headers=header, timeout=timeout)
req.encoding = 'utf-8' # 防止中文乱码
code = req.status_code # 返回状态,200代表OK
soup = BeautifulSoup(req.text, 'html.parser')
data = soup.find_all('td')[:2]
number = []
for x in data:
    number.append(re.search(r'(?<=>)(.*)(?=<\/td>)', str(x)).group(0))

label = 'Total:{} New:{}'.format(number[0],number[1])
# print(code)
print(label)

