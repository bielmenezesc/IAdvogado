from flask import Flask, request, render_template, redirect, url_for, send_file

from ai import return_doc
from create_word import download_document

app = Flask(__name__)

# Rota para a raiz da API
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a raiz da API
@app.route('/',methods=['POST'])
def create_juridic_doc():
    text = request.data
    doc = return_doc(text)
    download_document(doc)
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)