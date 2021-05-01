import joblib

def predict_tran(wrist,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z):
    model = joblib.load('walkrun.pkl')
    prediction = model.predict([[wrist,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z]])
    
    if prediction == 0:
        return 'WALKING'
    
    elif prediction == 1:
        return 'RUNNING'


import flask
from flask import render_template, request
from flask_cors import CORS

app = flask.Flask(__name__,)
CORS(app)

@app.route('/',methods=['GET'])
def default():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    #extract data from post request
    wrist = float(request.form['wrist'])
    acc_x = float(request.form['acc_x'])
    acc_y = float(request.form['acc_y'])
    acc_z = float(request.form['acc_z'])
    gyro_x = float(request.form['gyro_x'])
    gyro_y = float(request.form['gyro_y'])
    gyro_z = float(request.form['gyro_z'])
    print (wrist,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z)
    prediction = predict_tran(wrist,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z)
    return render_template('predict.html', transaction=prediction)

if __name__ == '__main__':
    app.run()
