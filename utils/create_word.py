from docx import Document
import os

def create_word(response):
    # Caminho para salvar os arquivos DOCX
    output_directory = "output_docs"

    # Verifica se o diretório de saída existe, senão, cria-o
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    # Cria um documento do Word
    doc = Document()

    # Adiciona o texto ao documento do Word
    doc.add_paragraph(response)

    # Salva o documento em um arquivo
    docx_filename = os.path.join(output_directory, "document.docx")
    doc.save(docx_filename)