from flask import render_template, Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from models import User,db
import os
from auth import auth

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///malkia.db'

# initialize db using sqlalchemy
db.init_app(app)

# initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# mounts auth routes to the app
app.register_blueprint(auth)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html', title ='Malkia Seductions')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)