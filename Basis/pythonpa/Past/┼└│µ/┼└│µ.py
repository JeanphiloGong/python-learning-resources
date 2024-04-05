import requests
import re
import os
 
image = '表情包'
if not os.path.exists(image):
    os.mkdir(image)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
response = requests.get('https://qq.yh31.com/zjbq/',headers=headers)
response.encoding = 'GBK'
response.encoding = 'utf-8'
print(response.request.headers)
print(response.status_code)
t = '<img src="(.*?)" alt="(.*?)" width="160" height="120">'
result = re.findall(t, response.text)
for img in result:
    print(img)
    res = requests.get(img[0])
    print(res.status_code)
    s = img[0].split('.')[-1]  //截取地址末尾，得到表情包格式，如.jpg .git
    with open(image + '/' + img[1] + '.' + s, mode='wb') as file:
        file.write(res.content)
