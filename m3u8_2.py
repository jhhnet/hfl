import requests
import re
import time
import random
from multiprocessing import Pool

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://yi.jingdianzuida.com/ppvod/BB48F51255693A0AF26A511FF5596D33.m3u8' # input('输入m3u8地址：')
url_content = requests.get(url, headers=header).text
# print(url_content)

url_base1 = url.split('/')[2]
# print(url_base1)
url_base2 = 'http://' + url_base1 + '/'
# print(url_base2)

ts_name = re.findall('#EXTINF:(.*),\n(.*)\n', url_content)
ts_list = []
for name in ts_name:
    ts_list.append(name[1])
# print(ts_list)

ts_new = []
for i in ts_list[0:11]:
    filename = i.split('/')[-1]
    url_ts = url_base2 + i
    ts_new.append(url_ts)
# print(ts_new)


def data_down(res):
    return requests.get(res, headers=header).content


def save_down(res1):
    fn = int(random.randint(1, 15))
    with open('download1\\%s.ts' % fn, 'wb') as f:  # 需要在同目录下新建download文件夹
        f.write(res1)


def down_no():
    time1 = time.time()
    for j in ts_new[0:11]:
        res = requests.get(j, headers=header).content
        with open('download\\%s' % j.split('/')[-1], 'wb') as f:  # 需要在同目录下新建download文件夹
            f.write(res)
    time2 = time.time()
    print('不使用pool耗时：', time2 - time1)


def down_pool():
    pool = Pool(4)
    time3 = time.time()
    p1 = pool.map(data_down, ts_new)
    pool.map(save_down, p1)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    time4 = time.time()
    print("使用pool耗时：", time4 - time3)


if __name__ == '__main__':
    down_no()
    down_pool()
