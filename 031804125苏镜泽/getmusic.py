import requests
import re

headers = {
    'authority': 's.taobao.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't=b21c97129d993a82ac8cfcf501e00317; v=0; _tb_token_=f7e5e89603581; _m_h5_tk=16267b384e83df934237bf2a8253f456_1600610541104; _m_h5_tk_enc=2b7ca35e36e2ceb6e2a11b205e340a55; cna=kIzXFxb5DwcCAWp6TqatlOPm; xlly_s=1; _samesite_flag_=true; cookie2=1a755ab33292b77f9496de1dc6a5b2cf; sgcookie=E100xunr7Tw75y59WPI27PduQ%2BuG9O%2Fue6nKmgM7IZHqqhRncTa8XEtaPkEdkyVLjWJ4THy7yJ5X1T5N8gP0scXzZg%3D%3D; unb=3978611290; uc3=lg2=URm48syIIVrSKA%3D%3D&nk2=F5RBzL9uq%2FMwu3M%3D&vt3=F8dCufeJMxOMW0noC70%3D&id2=UNkweIKfiNxKdQ%3D%3D; csg=6eaf7f71; lgc=tb492891376; cookie17=UNkweIKfiNxKdQ%3D%3D; dnk=tb492891376; skt=07c21c435a7c4544; existShop=MTYwMDYwMjIwMQ%3D%3D; uc4=id4=0%40Ug46tyRDnc9OByWbtuTI6V1BgCL6&nk4=0%40FY4KqaBnM9Wj44QWsrqJuO4E3dvbXQ%3D%3D; tracknick=tb492891376; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=604; _nk_=tb492891376; cookie1=BxVQAf1PouLoMHV%2FUpPeBu1XDN8kgpjJbQjQKkngdWs%3D; enc=RhU4JzsN4VDWhG9v7aU8xgomDiQxZdI05GZ%2F8ELHQd6eoMsvpamANrxfzonN5sADPORzGw51MZuGX7%2F1szRLAA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; mt=ci=11_1; uc1=cookie21=VT5L2FSpccLuJBreK%2BBd&pas=0&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie14=Uoe0bU5UvUbxjw%3D%3D; JSESSIONID=87FEC60EE5C1E4486FB50E39D7497D0B; isg=BPDwLlowW5T6ageQ2mVCswK7wb5COdSD8760aupBkMsepZFPkkmkE6DU-a3FNYxb; l=eBIxmmtqOFtnhSSYBOfZlurza77TRIRfguPzaNbMiOCPOk5p5AJGWZroSh89CnGVHs_pR3z9IwceBeDMqyCSnxv9-3k_J_0-3wC..; tfstk=cZZ1BFGyMCA1-ib2bR6EgWISNGnfaHxIKHcUCPNM0BW2xglS9sjH4bNwtAOCwuHC.',
}
def readInfo(result,html):
	#通过正则表达式直接获取商品的名称与价格
	prices = re.findall(r'"view_price":"[\d.]*"', html)
	titles = re.findall(r'"raw_title":".*?"', html)
	for i in range(0,len(prices)):
		#获取商品的名称与价格的值,并且去除引号
		price = prices[i].split(':')[1].replace('"','')
		title = titles[i].split(':')[1].replace('"','')
		result.append([price , title])

def writeInfo(result):
	#打印商品信息
	for i in range(0,len(result)):
		info = result[i]
		print("{0:^5}{1:^10}{2:^15}".format(i+1, info[0],info[1]))   

keyword = '书包'	#设置搜索关键词
result = []
print("{0:^5}{1:^5}{2:^15}".format('序号','价格','商品名称'))
for i in range(0,3):	#获取三页的商品信息
	url = 'https://s.taobao.com/search?q='+keyword+'&imgfile=&js=1&stats_click=search_radio_tmall%3A1' \
              '&initiative_id=staobaoz_20190508&tab=mall&ie=utf8&sort=sale-desc&filter=reserve_price%5B%2C200%5D' \
              '&bcoffset=0&p4ppushleft=%2C44&s=' + str(44*i)
	r = requests.get(url,headers = headers)
	r.encoding = "utf-8"
	html = r.text
	readInfo(result, html)
writeInfo(result)
