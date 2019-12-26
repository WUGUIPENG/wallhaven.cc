import requests
import re
import os
from bs4 import BeautifulSoup

#创建文件
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + "创建成功")
        return True
    else:
        print(path + "目录存在")
        return False


def test(start, path, a):
    for n in range(start):
        n = n+1

        path1 = path + a + "{}".format(n)
        mkdir(path1)

        
        center_1 = requests.get('https://wallhaven.cc/{}?page={}'.format(a, n))
        center_1.encoding = 'utf-8'
        soup_1 = BeautifulSoup(center_1.text, 'lxml')
        link_1 = soup_1.find_all(name='a',attrs={"href":re.compile(r'^https://wallhaven.cc/w')})
        print('正在爬取{}第{}页的图片'.format(a, n))

        for index, i in enumerate(link_1):
            center_2 = requests.get(i.get('href'))
            center_2.encoding = "utf-8"
            soup_2 = BeautifulSoup(center_2.content, 'lxml')
            link_2 = soup_2.find_all(name='img',attrs={"src":re.compile(r'^https://w.wallhaven.cc/full')})

            for each in link_2:
                url2 = each.get('src')
                html = requests.get(url2)
                img_name = path1 + "/" + url2[31:]
                print(img_name)

                with open(img_name, 'wb') as file:
                    file.write(html.content)
                    file.flush()
                file.close()
                index += 1
                print('第%d张图片下载完成' % (index))

if __name__ == "__main__":
    lt = ['latest', 'toplist']
    print(lt)
    a = lt[int(input("输入对应索引下载对应图片(索引从0开始):"))]
    start = int(input("输入需要下载的页数(一页=24张图片):"))
    path = "/home/tortoise/Image/"
    test(start, path, a)
