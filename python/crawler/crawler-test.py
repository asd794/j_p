import urllib.request as req

url="https://www.ptt.cc/bbs/Gossiping/index.html"
request=req.Request(url,headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

# --------------內文
url2="https://www.ptt.cc/bbs/Gossiping/M.1685010062.A.D31.html"
request2=req.Request(url2,headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})
with req.urlopen(request2) as response:
    data2=response.read().decode("utf-8")
# --------------內文

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
# print(root)
author=root.find_all("div",class_="author")
date=root.find_all("div",class_="date")
titles=root.find_all("div",class_="title") 
array=[]
x=0
# print(date)
for i in date:
    array.append(i.string)
    # print(array[x])
    x+=1
y=0
for i in author:
    array[y]=array[y]+" "+i.string
    # print(array[y])
    y+=1
z=0
for i in titles:
    array[z]=array[z]+" "+i.a.string
    print(array[z])
    z+=1

# --------------內文
root2=bs4.BeautifulSoup(data2,"html.parser")
