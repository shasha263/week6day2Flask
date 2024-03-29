from flask import Blueprint
from flask.templating import render_template

auth=Blueprint('auth',__name__, template_folder='auth.templates',url_prefix='/auth')

@auth.route('/signin')
def signin():
    return render_template('signin.html')


@auth.route('/register')
def signup():
    return render_template('signup.html')