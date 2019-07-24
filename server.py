from flask import Flask, render_template, request, redirect, session, flash
import re
from flask_bcrypt import Bcrypt 
from mysqlconn import connectToMySQL 
app = Flask(__name__)
bcrypt = Bcrypt(app)   
app.secret_key = '194562354'

racquets = ['prince_racquet', 'head_racquet','wilson_racquet', 'babolat_racquet']



@app.route('/')
def index():
    return render_template('index.html', racquets=racquets)






if __name__=="__main__":
    app.run(debug=True)