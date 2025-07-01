from flask import render_template, Flask, request
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title ='Malkia Seductions')

if __name__ == '__main__':
    app.run(debug=True)