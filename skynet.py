from flask import Flask, render_template, url_for, flash, redirect
from SkynetSqlConnect import getData

app = Flask(__name__)

# simulate a db call
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Arno Jones',
        'title': 'Blog Post 2',
        'content': 'My first post content',
        'date_posted': 'April 21, 2018'
    },
]

results = getData()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=results)
    # print(posts)
@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
