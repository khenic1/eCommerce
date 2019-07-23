from flask import Flask, render_template, request, redirect, session, flash
import re
from flask_bcrypt import Bcrypt 
from mysqlconn import connectToMySQL 
app = Flask(__name__)
bcrypt = Bcrypt(app)   
app.secret_key = '194562354'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_login():
    return render_template('admin.html')




if __name__=="__main__":
    app.run(debug=True)