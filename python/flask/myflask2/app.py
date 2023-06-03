from flask import Flask #載入flask
app=Flask(__name__) #建立Application物件

# 建立網站首頁的回應方式
@app.route("/")
def index(): # 用來回應網站首頁的函式
    return "Hello Flask" # 回傳網站首頁的內容

# 啟動網站伺服器
app.run(port=3000)
