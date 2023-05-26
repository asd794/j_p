import bs4

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

soup=bs4.BeautifulSoup(html_doc,"html.parser")
# print(soup.prettify()) # 整理排版過後的html

# titles=soup.title.string    # 網頁的標題文字
# print(titles)

a_tags=soup.find_all('a')   # # 所有的超連結
p=soup.find('a')
print(p)
# print(a_tags)
# for i in a_tags:
#     print(i.string,i.get('href'))
print(p['href'])