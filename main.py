from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import LoginForm, RegisterForm, CreatePostForm, CommentForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("#")


@app.route('/logout')
def logout():
    logout_user()
    return redirect('#')


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    return render_template("#")


@app.route("/about")
def about():
    return render_template("#")


@app.route("/contact")
def contact():
    return render_template("#")


if __name__ == "__main__":
    app.run(debug=True)