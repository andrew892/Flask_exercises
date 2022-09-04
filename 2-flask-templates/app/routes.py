from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def home():
    user = {'username': 'andrea'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='titolo', user=user, posts=posts)
