from flask import Flask, request, render_template, redirect, url_for, send_file

from utils.ai import return_doc
from utils.create_word import create_word

import os

app = Flask(__name__, static_folder='./css')

# Rota para a raiz da API
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a raiz da API
@app.route('/',methods=['POST'])
def create_juridic_doc():
    text = request.data
    doc = return_doc(text)
    create_word(doc)
    return redirect(url_for('download'))

# Rota para download do arquivo
@app.route('/download', methods=['GET'])
def download():
    # Substitua 'caminho/para/seu/arquivo/arquivo_a_ser_baixado.txt' pelo caminho do arquivo que você deseja enviar
    file_path = os.path.join(app.root_path, 'output_docs', 'document.docx') 

    # Envie o arquivo para o cliente para download
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)