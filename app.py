from flask import Flask
from flask import render_template
from script import extract_text

app = Flask(__name__)

texts = extract_text()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',text=texts)

if __name__ == '__main__':
    app.run(debug=True)

