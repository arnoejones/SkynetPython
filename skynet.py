from flask import Flask, render_template, url_for, flash, redirect
from SkynetSqlConnect import getData

app = Flask(__name__)

results = getData()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=results)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
