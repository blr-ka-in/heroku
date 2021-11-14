#from types import MethodDescriptorType
from flask import Flask, render_template, request
#from flask.wrappers import Request
import joblib

app = Flask(__name__)

loaded_model = joblib.load('dib_78.pkl')

@app.route('/')   #decorator
def index():
    return "hello world"

# @app.route('/homepage')     #decorator
# def homepage():
#     return 'Welcome Home page'

@app.route('/homepage')     #decorator
def homepage():
     return render_template('homepage.html')

@app.route('/predict', methods=['POST'])     #decorator
def predict():
    fname = request.form.get('firstname')
    sname = request.form.get('lastname')
    mobile = request.form.get('phonenumber')
    email = request.form.get('mail')
    print (fname, sname,    mobile, email)
    return render_template('homepage.html')

@app.route('/predict2', methods=['POST'])     #decorator
def predict2():
    val1 = int(request.form.get('val1'))
    val2 = int(request.form.get('val2'))
    val3 = int(request.form.get('val3'))
    val4 = int(request.form.get('val4'))
    val5 = int(request.form.get('val5'))
    val6 = int(request.form.get('val6'))
    val7 = int(request.form.get('val7'))
    val8 = int(request.form.get('val8'))
    #'preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'
    print (val1, val2, val3, val4, val5, val6, val7, val8)
    pred = loaded_model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    val = ''
    if pred[0] == 1:
        val  = 'diabetic'
    else:
        val = 'not diabetic'
    return render_template('result.html', value=val)

@app.route('/login')
def login():
    return 'welcome to login page'

@app.route('/gallary')
def gallary():
    return 'wecome to gallary page'

@app.route('/contact')
def contact():
    return render_template('contact.html')



#app.run()   # need to start server again -n-again after changes
if __name__=='__main__':
    app.run(debug=True)