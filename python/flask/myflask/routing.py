from flask import Flask

@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageNyName(name):
    print("type(name) : ",type(name))
    return 'String => {}'.format(name)

# queryDataMessageNyName('Jay')