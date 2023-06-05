from flask import Flask #載入flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template #載入render_template函式
import json
#建立Application物件
app=Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱，原本預設為static，使用者參數後就會變成他
    static_url_path="/" # 靜態檔案對應的網址路徑    
    ) 
# 所有在static資料夾底下的檔案，都對應到網址路徑 /檔案名稱

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 處理的函式
    print("請求方法",request.method)
    print("通訊名稱",request.scheme)
    print("主機名稱",request.host)
    print("路徑",request.path)
    print("完整的網址",request.url)
    print("瀏覽器和作業系統",request.headers.get("user-agent"))
    print("語言偏好",request.headers.get("accept-language"))
    print("引薦網址",request.headers.get("ref"))
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en")
    elif lang.startswith("zh-TW"):
        return redirect("zh")
    else:
        return "Hello Flask" # 回傳網站首頁的內容

@app.route('/en')
def index_en():
    return json.dumps({
        "status":"ok",
        "text":"Hi,English user"
    })
@app.route('/zh')
def index_zh():
    return json.dumps({
        "status":"ok",
        "text":"Hi,繁體中文用戶"
    },ensure_ascii=False) # 指示不用 ASCII編碼 處理中文

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

# 利用要求字串(Query Sting)提供彈性: /getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum():
    minNumber=int(request.args.get("min",1))
    maxNumber=int(request.args.get("max",0))
    result=0
    print("min最小數字=",minNumber)
    print("max最大數字=",maxNumber)
    for i in range (minNumber, maxNumber+1):
        result+=i
    return str(minNumber)+"+...+"+str(maxNumber)+"= "+str(result)

# 可以導向路徑或是網址
@app.route('/redirect1')
def redirect1():
    return redirect("/")
@app.route('/redirect2')
def redirect2():
    return redirect("https://www.google.com")

# 建立路徑 /temp 對應的處理函式
@app.route("/temp")
def temp_index():
    return render_template("index.html",name='大壯')

@app.route("/form")
def form():
    name=request.args.get("data","") # 對應index.html <input type="text" name="data"/> 的data
    return '歡迎,'+name


# 啟動網站伺服器
app.run(port=3000)
