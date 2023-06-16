from flask import *
from flask_cors import CORS
import numpy as np

app=Flask(__name__)

@app.route('/')
def index():
    return 'Good morning .'

@app.route('/predict' ,methods=['POST'])
def postInput():
    inserValues = request.get_json()
    x1=inserValues['sepalLengthCm']
    x2=inserValues['sepalWidthCm']
    x3=inserValues['petalLengthCm']
    x4=inserValues['petalWidthCm']
    input=np.array([[x1,x2,x3,x4]])
    print(input)
    return jsonify({'return':'ok!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80 ,debug=True)