from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user


# WSGI Application
app = Flask(__name__)

@app.route('/')
def auction():
    return render_template('index.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)
