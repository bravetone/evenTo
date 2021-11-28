import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Message, Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_required, login_manager, logout_user, current_user, login_user

from flask import render_template, redirect, url_for, session, request, flash

from website import routes
from website import form



# upload image
from flask_uploads import UploadSet
from flask_uploads import configure_uploads
from flask_uploads import IMAGES, patch_request_class
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug import secure_filename, FileStorage
# ImportError: cannot import name 'secure_filename'
# pip install -U Werkzeug==0.16.0
# set maximum file size, default is 16MB


# from form import FormContact,Registration,LogForm

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'hard to guess'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///evenTO.db"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# EMAIL config
app.config['MAIL_USERNAME'] = ""  # os.environ['EMAIL_USERNAME']
app.config['MAIL_PASSWORD'] = ""
app.config['MAIL_TLS'] = True
app.config['MAIL_SERVER'] = 'smtp.mail.com'
app.config['MAIL_PORT'] = 587
# Upload Configuration
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + "/static"

db = SQLAlchemy(app)
# MAIL
mail = Mail(app)
bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
login_manager.init_app(app)

# UPLOAD Then define Upload format and file size.
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


from website import routes, model
