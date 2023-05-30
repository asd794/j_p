from flask import Flask
app=Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/test2")
@app.route("/") # 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def home():
    return "Hello Flask"

@app.route("/test")
def test():
    return "test"

if __name__=="__main__": # 如果以主程式執行
    app.run() # 立即啟動伺服器

