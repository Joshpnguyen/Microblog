from flask import render_template
from app import app


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


app.run()
