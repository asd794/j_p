from flask import Flask, render_template, url_for, redirect, request
app=Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/test2")
@app.route("/",methods=['POST','GET']) # 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def index():
    if request.method == 'POST':
        if request.values['send'] == '送出阿':
            return render_template('index.html',name=request.values['user'])
    return render_template("index.html",name='')

@app.route("/test")
def test():
    return render_template("test.html")

@app.route('/url_for')
def url_f():
    return redirect(url_for('index'))

@app.route('/ng')
def ng():
    return render_template('navigation.html')

if __name__=="__main__": # 如果以主程式執行
    app.run(host='0.0.0.0', port='5555', debug=True) # 立即啟動伺服器，debug=True 網站執行中修改檔案，會自動重新啟動網站

