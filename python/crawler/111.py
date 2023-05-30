import urllib.request as req
import bs4
content_array=[]

url2="https://www.ptt.cc/bbs/Gossiping/M.1685429415.A.05F.html"
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


print(content_array[0])
    