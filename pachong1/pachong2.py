import requests
import re
import os
import threading
import multiprocessing



def down(url):
    try:

        r = requests.get(url, timeout=50)
        r.raise_for_status()
        r.encoding = r.raise_for_status()
        print(r.text)
        return r.text
    except:
        pass


def gethtml():
    while True:
        if not q_request1.empty():
            new_request_thread1 = threading.Thread(target=gethtml_thread1)
            new_request_thread1.start()
        if not q_request2.empty():
            new_request_thread2 = threading.Thread(target=gethtml_thread2)
            new_request_thread2.start()


def save():
    i = 1
    while True:
        if not q_picture.empty():
            new_save_thread = threading.Thread(target=save_thread,args = (i,))
            new_save_thread.start()
            i +=1


def gethtml_thread1():
    try:
        a_request = q_request1.get()
        page1_request = down(a_request)
        d = re.findall(r'https://alpha.wallhaven.cc/wallpaper/\d+', page1_request)
        for i in d:
            q_request2.put(i)
    except:
        print('未找到1')


def gethtml_thread2():
    b_request = q_request2.get()
    page2_request = down(b_request)
    picture_url = re.findall(r'src="//wallpapers.*?\d.jpg', page2_request)
    for j in picture_url:
        price = 'https:' + j.split('"')[1]
        q_picture.put(price)
        print(price)


def save_thread(i):

    g = q_picture.get()
    path =  '/home/python/Desktop/picture/'  # 存储目录
    pathh = path + str(i) + '.jpg'
    if not os.path.exists(path):
        os.makedirs(path)
    o = requests.get(g)
    with open(pathh, 'wb') as f:
        f.write(o.content)


if __name__ == '__main__':
    goods = input('请输入搜索关键字：')  # 搜素关键字
    num =  input('请输入分辨率：') # 分辨率
    p =   int(input('请输入图片个数：'))//24# *24=图片个数
    q_request1 = multiprocessing.Queue(10)
    q_request2 = multiprocessing.Queue(10)
    q_picture = multiprocessing.Queue(10)
    for page in range(p):
        u = 'https://alpha.wallhaven.cc/search?q=' + str(goods) + '&categories=111&purity=' \
         '100&atleast=' + str(num) + '&sorting=relevance&order=desc&page=' + str(page + 1)
        q_request1.put(u)
    get_process = multiprocessing.Process(target=gethtml)
    get_process.start()
    save_process = multiprocessing.Process(target=save)
    save_process.start()