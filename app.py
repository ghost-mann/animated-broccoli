from flask import render_template, Flask, request, redirect, url_for,flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from dotenv import load_dotenv
from models import User,db
import os


load_dotenv()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title ='Malkia Seductions')

if __name__ == '__main__':
    app.run(debug=True)