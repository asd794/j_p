# 抓取PTT原始碼HTML資料
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index9509.html"
# 建立一個Request物件 ,附加Request Headers的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

# 使用第三方套件BeautifulSoup 解析原始碼 ,取得文章標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")  # 尋找所有class="title"的div的標籤
# print(titles.a.string)
# print(titles)
for i in titles:
    if i != None:
        print(i.a.string)