import urllib.request as req
def catch(url):
    # url="https://www.ptt.cc/bbs/Gossiping/index.html"
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)


    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    # print(root)
    titles=root.find_all("div",class_="title")  # 尋找所有class="title"的div的標籤
    # print(titles)
    # print(titles[0].a.string)
    for i in titles:
        if i.a != None:
            print(i.a.string)
    print("----------------")

    # 抓取上一頁的連結
    nextlink=root.find("a",string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return nextlink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    nexturl="https://www.ptt.cc"+catch(pageURL)
    count+=1
    # print("----------------")
    # print(nexturl)
