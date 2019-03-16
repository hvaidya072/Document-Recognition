from flask import Flask, request
from flask import render_template
from script import extract_text
from werkzeug import secure_filename
from pdf_decode import pdf_to_text

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

@app.route('/upload')
def upload():
    return render_template('upload_file.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('data/' + secure_filename(f.filename))
      pdf_to_text(f.filename)
      return 'file uploaded and converted successfully'


if __name__ == '__main__':
    app.run(debug=True)

