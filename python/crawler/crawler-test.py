import urllib.request as req

url="https://www.ptt.cc/bbs/Gossiping/index.html"
request=req.Request(url,headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
# print(root.prettify())
author=root.find_all("div",class_="author") # 抓作者
date=root.find_all("div",class_="date") # 抓日期
titles=root.find_all("div",class_="title")  # 抓標題
# href=root.find("a",string='[協尋] 發錢 陳橘「胖橘貓」大安區龍安加油站')
ppt_url='https://www.ptt.cc'
date_array=[]
author_array=[]
titles_array=[]
ppt_article_url_array=[]

x=0
for i in date:
    date_array.append(i.string) # class裡面的String值加入date_array陣列
    # print(date_array[x])
    x+=1
y=0
for i in author:
    author_array.append(i.string) # class裡面的String值加入author_array陣列
    # print(author_array[y])
    y+=1
z=0
for i in titles:
    titles_array.append(i.a.string) # class裡面的String值加入1titles_array陣列
    href_url=root.find("a",string=i.a.string)   # 用文章標題(i.a.string)去搜尋對應的class元素
    ppt_article_url_array.append(ppt_url+href_url['href'])   # href_url['href'] 加上['href']搜尋底下的href
    # print(titles_array[z])
    z+=1

xx=0
for i in ppt_article_url_array:
    print(date_array[xx],author_array[xx],titles_array[xx],i)
    xx+=1

print("----------------")
# --------------內文
url2="https://www.ptt.cc/bbs/Gossiping/M.1685093096.A.D51.html"
request2=req.Request(url2,headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})
with req.urlopen(request2) as response:
    data2=response.read().decode("utf-8")
root2=bs4.BeautifulSoup(data2,"html.parser")
maincontent=root2.find("div",id="main-content") # 主要內容main-content

fromptt=root2.find("span",class_="f2")
fromptt2=root2.find_all("span",class_="article-meta-value")


print(len(str(fromptt2[3])+"</div>")) # 前面文字的長度
print(str(maincontent).find(str(fromptt2[3])+"</div>")) # 前面文字的位置
# print(fromptt)
# print(article_meta_value)

# if "※ 發信站: 批踢踢實業坊(ptt.cc)" in str(fromptt):
#     print("有")
# else:
#     print("無")

# ttest="Hi , I am Jay. 你好阿"
# print(ttest.find("Hi"))

print(len(str(maincontent))) # main-content總長度

# print(str(maincontent).find('<div class="article-metaline"><span class="article-meta-tag">時間</span><span class="article-meta-value">Fri May 26 17:24:54 2023</span></div>'))  # 先找文章前面的文字位置
print(str(maincontent).find('<span class="f2">※ 發信站: 批踢踢實業坊(ptt.cc),'))    # 先找文章後面的'<span class="f2">※ 發信站: 批踢踢實業坊(ptt.cc),'在main-content的位置  <-- 固定的字串
print(str(maincontent)[526+70:655-1])
