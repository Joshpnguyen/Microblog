from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Stephanie'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Mission Viejo!',
            'date': '04-04-2022'
        },
        {
            'author': {'username': 'Billy'},
            'body': 'The Avengers movie was so good!!',
            'date': '04-06-2022'
        }
    ]
    return render_template('index.html', title='', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


app.run()
