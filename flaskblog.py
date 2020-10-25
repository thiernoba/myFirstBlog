### this is my first application using Flask ####
#first of all we need to install some packages

from flask import Flask, render_template, url_for
from flask_restful import Resource, Api, reqparse, fields, marshal_with
import requests
from form import RegistrationForm, LoginForm
import form
#######

app = Flask(__name__)

# creat a secret key for login with a good cookie
app.config['SECRET_KEY'] = 'f1de88b7d35eb44b'
# creation a list 

posts = [
    {
        'author':'thierno bah',
        'title': 'blog Post 1',
        'content':'First Post Content',
        'date_posted':'25 oct 2020'

    },
    {
        'author':'Salimatou Sall',
        'title': 'blog Post 2',
        'content':'Second Post Content',
        'date_posted':'24 oct 2020'

    }
]

#creating a route

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', auteurs=posts)


### a new route for the About page

#route for About Page
@app.route("/About")
def about():
    return render_template('About.html', info=posts, title="blog thierno")

# route for register Page
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

#route for the login page 
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
