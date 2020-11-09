from bs4 import BeautifulSoup
import requests
#读取html
def getText(url):
    try:
        header={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
        r=requests.get(url,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
#从html中读取名称和价格
def getmessage(html):
    infodict={}
    soup=BeautifulSoup(html,'html.parser')
    for i in range(20):
        info=soup.find_all('div',attrs={'class':"gl-i-wrap"})[i]
        info_price=info.find("div",attrs={'class':'p-price'})
        info_name=info.find("div",attrs={'class':'p-name p-name-type-2'})
        valuelist=info_price.find('i')
        keylist=info_name.find('em')
        key=keylist.text.split()
        key_1=''.join(key)
        val=valuelist.text
        infodict[key_1]=val
    return infodict
#输出读取的名称和价格
def printt(infodict):
    tplt = "{:4}\t{:10}\t{:<40}\t"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in infodict:
        count=count+1
        print(tplt.format(count,infodict[g],g))



url='https://search.jd.com/Search?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&wq=&pvid=1919fd329c004cffa29cb405894dd929'
html=getText(url)
dict1=getmessage(html)
printt(dict1)



