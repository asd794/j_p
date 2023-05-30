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
content_array=[]

x=0
for i in date:
    date_array.append(i.string) # class=date裡面的String值加入date_array陣列
    # print(date_array[x])
    x+=1
y=0
for i in author:
    author_array.append(i.string) # class=author裡面的String值加入author_array陣列
    # print(author_array[y])
    y+=1
z=0
for i in titles:
    titles_array.append(i.a.string) # class=titles裡面的String值加入1titles_array陣列
    href_url=root.find("a",string=i.a.string)   # 用文章標題(i.a.string)去搜尋對應的class元素
    if '(本文已被刪除)' in titles:  # 判斷文章是否被刪除
        ppt_article_url_array.append('(本文已被刪除)')
    else:
        ppt_article_url_array.append(ppt_url+href_url['href'])   # href_url['href'] 加上['href']搜尋底下的href
    # print(titles_array[z])
    z+=1

xx=0
for i in ppt_article_url_array:
    print(date_array[xx],author_array[xx],titles_array[xx],i)
    xx+=1

print("----------------")   # --------------------------------內文

yy=0
for i in ppt_article_url_array:

    url2=i
    request2=req.Request(url2,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    })
    with req.urlopen(request2) as response:
        data2=response.read().decode("utf-8")
    root2=bs4.BeautifulSoup(data2,"html.parser")
    maincontent=root2.find("div",id="main-content") # 主要內容main-content
    fromptt=root2.find("span",class_="f2")
    fromptt2=root2.find_all("span",class_="article-meta-value") # 尋找class=article-meta-value 位置放入fromptt2陣列 ,總共有4筆一樣的class

    n1=len(str(fromptt2[3])+"</div>") # 前面文字的長度 ,發文時間在fromptt2第四筆陣列加上</div> ,得以算出長度 
    # print(n1)
    n2=str(maincontent).find(str(fromptt2[3])+"</div>") # 前面文字的位置 ,發文時間在fromptt2第四筆陣列加上</div> ,得以算出位置(結果會是頭的位置)
    # print(n2)
    # n3=len(str(maincontent)) # main-content總長度
    # print(n3)
    n4=str(maincontent).find('<span class="f2">※ 發信站: 批踢踢實業坊(ptt.cc),')    # 先找文章後面的'<span class="f2">※ 發信站: 批踢踢實業坊(ptt.cc),'在main-content的位置  <-- 固定的字串
    # print(n4)
    content=str(maincontent)[n1+n2:n4-1]
    content_array.append(content)
    # print(content)

    # print(content_array[yy])
    yy+=1

print(content_array[13])
    