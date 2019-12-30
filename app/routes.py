from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Miguel"}
    posts = [
        {
            'author' : {'username': 'John'},
            'body': 'A beautiful day in Portland, OR'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
