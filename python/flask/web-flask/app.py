from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://weichih:wtVDTbr4azrGa46E@cluster0.9qo8cqy.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

from flask import *

app=Flask(
    __name__,
    # static_folder="public",
    # static_url_path="/"
)
app.secret_key="secret key for flask test"

# 首頁
@app.route("/")
def index():
    return render_template("index.html")

# 會員頁面
@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html",nickname=session['nickname'])
    else:
        return redirect("/")

# 錯誤頁面 /error?msg=錯誤訊息
@app.route("/error")
def error():
    message=request.args.get("msg","發生錯誤請聯繫客服")
    return render_template("error.html",message=message)

# 處理會員註冊
@app.route("/signup" ,methods=["POST"])
def signup():
    # 從前端接收資料
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    #
    if nickname=="" or email=="" or password=="":
        return "三個欄位都是必填，請重新註冊"
    # 根據接收的資料與資料庫互動
    db=client.myweb
    collection=db.users
    if collection.find_one({"email":email})==None: # 檢查email是否空值None,是空值就新增到資料庫
        collection.insert_one({
            "nickname":nickname,
            "email":email,
            "password":password
        })
        return redirect("/")
    else: # 不是空值傳Query String到error.html報錯
        return redirect("/error?msg=信箱已經被註冊")
        # return render_template("error.html",msg="信箱已經被註冊了")

# 處理會員登入
@app.route("/signin" ,methods=["post"])
def signin():
    email=request.form["email"]
    passowrd=request.form["password"]
    db=client.myweb
    collection=db.users
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":passowrd}
        ]
    })
    if result==None:
        return redirect("/error?msg=帳密輸入錯誤")
    else:
        session['nickname']=result['nickname']
        session['email']=email
        # print(session['nickname'])
        return redirect("/member")
    
# 會員登出
@app.route("/signout")
def signout():
    del session["nickname"]
    session.clear()
    print(session)
    return redirect("/")
if __name__=='__main__':
    app.run(host='0.0.0.0',port=80)
