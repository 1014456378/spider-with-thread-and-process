import requests
import re
import os
import threading
import multiprocessing
import time


def gethtml(url):
        try:

            r = requests.get(url, timeout=50)
            r.raise_for_status()
            r.encoding = r.raise_for_status()
            print(r.text)
            return r.text
        except:
            pass

def fenxi(s,c):
        try:
            d = re.findall(r'https://alpha.wallhaven.cc/wallpaper/\d+', s)
            for i in range(len(d)):
                # h = gethtml(d[i])
                h = po1.map(gethtml, (d[i],))[0]
                print(h,type(h))
                e = re.findall(r'src="//wallpapers.*?\d.jpg', h)

                for j in range(len(e)):
                    price = 'https:' + e[j].split('"')[1]
                    if price not in c:
                        c.append(price)
                        url_Q.put(price)
                        print(c)
        except:
            print('1')

def save(v2):
        # try:
            i = 1
            while True:
                if not url_Q.empty():
                    g = url_Q.get()
                    path = v2  # 存储目录
                    pathh = path + str(i) + '.jpg'
                    if not os.path.exists(path):
                        os.makedirs(path)
                    o = requests.get(g)
                    with open(pathh, 'wb') as f:
                        f.write(o.content)
                        i+=1
                time.sleep(1)
        # except:
        #     pass
url_Q = multiprocessing.Queue()
po1 = multiprocessing.Pool(10)
# goods = input('请输入关键字')  # 搜素关键字
# num = input('请输入分辨率')  # 分辨率
# p = int(input('请输入图片个数'))//24  # *24=图片个数
# path = input('请输入存储目录')
path = '/home/python/Desktop/picture/'

b = []
# po2 = multiprocessing.Pool(10)

# for page in range(1):
# u = 'https://alpha.wallhaven.cc/search?q=' + str(goods) + '&categories=111&purity=' \
#  '100&atleast=' + str(num) + '&sorting=relevance&order=desc&page=' + str(page + 1)
u = 'https://alpha.wallhaven.cc/search?q=' + 'girl'+ '&categories=111&purity=' \
 '100&atleast=' + '1920x1089' + '&sorting=relevance&order=desc&page=' + '1'
a = po1.map(gethtml, (u,))[0]
print(a)
# a = gethtml(u)
fenxi(a,b)

save(path)



# def firs(vvv1, vvv2, vvv3,vvv4):
#         goods = vvv1  # 搜素关键字
#         num = vvv3  # 分辨率
#         p = vvv4  # *24=图片个数
#         b = []
#         for page in range(p):
#             u = 'https://alpha.wallhaven.cc/search?q=' + str(goods) + '&categories=111&purity=' \
#              '100&atleast=' + str(num) + '&sorting=relevance&order=desc&page=' + str(page + 1)
#             a = gethtml(u)
#             fenxi(a, b)
#         save(b, vvv2)


