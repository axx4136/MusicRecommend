
import os

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
def imageSpider(start_url):
    try:
        urls=[]
        req = urllib.request.Request(start_url,headers=headers)
        data = urllib.request.urlopen(req)
        data = data.read()
        dammit = UnicodeDammit(data,["utf-8","gbk"])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data,"lxml")
        images = soup.select("img")
        for image in images:
            try:
                src = image["src"]
                url = urllib.request.urljoin(start_url,src)
                if url not in urls:
                    print(url)
                    urls.append(url)
                    download(url)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


def download(url):
    global count
    try:
        if (url[len(url) - 4] == "."):
            ext = url[len(url) - 4:]
        else:
            ext = ""
        count = count + 1
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req,timeout = 100)
        data = data.read()
        fobj = open("D:/data/jpg/"+str(count)+ext,"wb")
        fobj.write(data)
        fobj.close()
    except Exception as err:
        print(err)


start_url = "http://www.weather.com.cn"
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre)Gecko/2008072421 Minefield/3.0.2pre"}
count=0
print("下载的Url信息:")
imageSpider(start_url)

