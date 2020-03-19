import requests
import re

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://yi.jingdianzuida.com/ppvod/BB48F51255693A0AF26A511FF5596D33.m3u8' # input('输入m3u8地址：')
url_content = requests.get(url, headers=header).text
# print(url_content)

if '#EXTM3U' not in url_content:
    print('非m3u8正确地址')
    if 'EXT-X-KEY' not in url_content:
        print('这是非加密m3u8')
else:
    pass

url_base1 = url.split('/')[2]
# print(url_base1)
url_base2 = 'http://' + url_base1 + '/'
print(url_base2)

ts_name = re.findall('#EXTINF:(.*),\n(.*)\n', url_content)
ts_list = []
for name in ts_name:
    ts_list.append(name[1])
# print(ts_list)

for i in ts_list:
    filename = i.split('/')[-1]
    url_ts = url_base2 + i
    res = requests.get(url_ts, headers=header).content
    with open('download\\' + filename, 'wb') as f: #需要在同目录下新建download文件夹
        f.write(res)
