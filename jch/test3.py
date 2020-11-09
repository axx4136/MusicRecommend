from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import urllib.parse
import time
#start_time=time.clock()
start_url="http://www.weather.com.cn/weather/101280601.shtml"
headers={
    "User-Agent":"Mozilla/5.0(Windows NT 6.0 x64;en-US;rv:1.9pre)Gecko/2"
}
def imageSpider(start_url):
    try:
        urls=[]
        req=urllib.request.Request(start_url,headers=headers)
        data=urllib.request.urlopen(req)
        data =data.read()
        dammit=UnicodeDammit(data,["utf-8","gbk"])
        data=dammit.unicode_markup
        soup=BeautifulSoup(data,"lxml")
        images=soup.select("img")
        for image in images:
            try:
                src=image["src"]
                url=urllib.parse.urljoin(start_url,src)
                if url not in urls:
                    urls.append(url)
                    print(url)
                    download(url)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)

def download(url):
    global count
    try:
        count=count+1
        if(url[len(url)-4]=='.'):
            ext=url[len(url)-4:]
        else:
            ext=''
        req=urllib.request.Request(url,headers=headers)
        data=urllib.request.urlopen(req,timeout=100)
        data=data.read()
        fobj=open("images\\"+str(count)+ext,"wb")
        fobj.write(data)
        fobj.close()
        print("download"+str(count)+ext)
    except Exception as err:
        print(err)
count=0
imageSpider(start_url)
#end_time=time.clock()
#print("耗时：",end_time-start_time)