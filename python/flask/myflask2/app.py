from flask import Flask #載入flask
#建立Application物件
app=Flask(
    __name__,
    static_folder="a556"
    # static_url_path=""    
    ) 

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 處理的函式
    return "Hello Flask" # 回傳網站首頁的內容

# 建立路徑 /data 對應的處理函釋
@app.route('/data')
def handledata():
    return 'Hello , Data'

# 動態路由:建立路徑 /user/<使用者名稱> 對應的處理函式
@app.route("/user/<username>")
def userlogin(username):
    if username=='jay':
        return '你好啊,weichih'
    return "Hello,"+username

# 啟動網站伺服器
app.run(port=3000)
