# import sys
# sys.path.append("/home/ubuntu/.local/lib/python3.10/site-packages") # AWS機器

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://asd123753951:q9BsyWYDLiZXjCYh@cluster0.azvuikv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
from flask import *
from flask_bcrypt import Bcrypt #匯入flask-bcrypt 套件
bcrypt=Bcrypt() # 建立Bcrypt實體並指定給變數bcrypt



app=Flask(
    __name__,
    static_folder="public",
    # static_url_path="/"
)
app.secret_key="secret key for flask test"

# 登入首頁
@app.route("/")
def index():
    return render_template("login.html")
# 註冊頁面
@app.route("/register")
def register():
    return render_template("register.html")


# 會員頁面
@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html",account=session['account'],email=session['email'])
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
    email=request.form["email"]
    account=request.form["account"]
    password=request.form["password"]
    #
    if account=="" or email=="" or password=="":
        return "三個欄位都是必填，請重新註冊"
    # 根據接收的資料與資料庫互動
    db=client.myweb
    collection=db.users
    hashed_password=bcrypt.generate_password_hash(password=password) # 雜湊函數加密密碼
    if collection.find_one({"email":email})==None: # 檢查email是否空值None,是空值就新增到資料庫
        collection.insert_one({
            "email":email,
            "account":account,
            "password":hashed_password
        })
        return redirect("/")
    else: # 不是空值傳Query String到error.html報錯
        return redirect("/error?msg=信箱已經被註冊")
        # return render_template("error.html",msg="信箱已經被註冊了")

# 處理會員登入 MongoDB
@app.route("/signin" ,methods=["post"])
def signin():
    account=request.form["account"]
    passowrd=request.form["password"]
    db=client.myweb
    collection=db.users
    db_check=collection.find_one({"account":account}) 
    print(db_check)
    print(db_check['email'])
    print(account)
    if db_check != None:
        check_password=bcrypt.check_password_hash(db_check['password'],passowrd) # 雜湊密碼比對
        if check_password ==True:
            session['email']=db_check['email']
            session['account']=account
            return redirect("/member")
            # return session['email']+session['account']
        else:
            return redirect("/error?msg=帳密輸入錯誤")
    else:
        return redirect("/error?msg=帳密輸入錯誤")
    
    # result=collection.find_one({
    #     "$and":[
    #         {"email":email},
    #         {"password":passowrd}
    #     ]
    # })
    # print(result)
    # if result==None:
    #     return redirect("/error?msg=帳密輸入錯誤")
    # else:
    #     session['nickname']=result['nickname']
    #     session['email']=email
    #     # print(session['nickname'])
    #     return redirect("/member")
    
# 會員登出 清除session
@app.route("/signout")
def signout():
    del session["email"]
    del session["account"]
    session.clear()
    print(session)
    return redirect("/")

@app.route('/kvb')
def kvb():
    return redirect("https://tw.google.com")

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80)
