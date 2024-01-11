from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    v = float(request.form.get('Annual average wind speed'))
    ra = int(request.form.get('Total rainy days during the year'))
    ts = int(request.form.get('Total stormy days throughout the year'))

    result = model.predict(np.array([v,ra,ts]).reshape(1,3))

    if result[0]==1:
        result =  'GOOD Air Quality'
    else:
        result =  "BAD Air Quality"

    return render_template('index.html',result =result)

if __name__=='__main__':
    app.run(debug=True)
