from flask import Flask, request, render_template, session
import os
from pdf_extract import extract_tables_from_pdf

from llama_index import create_llama_index, query_llama_index  # Updated import

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join('uploads', file.filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)

        # Extract tables from the PDF
        tables = extract_tables_from_pdf(file_path)

        # Create an index from the extracted data
        index = create_llama_index(tables)
        # Store the index in session
        session['index'] = index
        return "File uploaded and processed successfully!", 200
    return "Invalid file type", 400


@app.route('/query', methods=['POST'])
def query_pdf():
    query = request.form['query']
    index = session.get('index')

    if index:
        response = query_llama_index(index, query)
        return response
    else:
        return "No data available for querying", 400


if __name__ == '__main__':
    app.run(debug=True)
