import requests
from bs4 import BeautifulSoup
URL = 'https://gs.amac.org.cn/amac-infodisc/res/pof/fund/2008100848106055.html'
page = requests.get(URL, verify = False)
bs = BeautifulSoup(page.content, 'html.parser')
dict = {}
i = 0
for item in bs.find_all("td"):
    if item.string != None and i < 6:
        if i%2 ==0:
            a = item.string.replace(" ","").replace("\n","")
        if i%2 ==1:
            dict[a] = item.string.replace(" ","").replace("\n","")
        i = i + 1
    elif i>= 6:
        if i%2 ==0:
            a = item.string
        if i%2 ==1:
            dict[a] = item.string
        i = i + 1
    if item.a != None:
        name = item.a.string
dict['基金管理人名称:'] = name
print(dict)

