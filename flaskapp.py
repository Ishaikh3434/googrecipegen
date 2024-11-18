# main.py (Flask backend)
from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import ssl
import os
from dotenv import load_dotenv
from googgen import recipeWriter
import uuid
load_dotenv()

app = Flask(__name__)
writer=recipeWriter()
app.secret_key=os.environ["SESSION_KEY"]
print(app.secret_key)
# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.json.get('inputText')
    session['inputText'] = input_text
    output_text = writer.generate(input_text)
    session['outputText']=output_text
    return jsonify({'outputText': session['outputText']})

if __name__ == '__main__':
    context = ('certificate.crt', 'private.key')  # Path to your SSL certificate and key
    app.run(host='0.0.0.0', port=8080, ssl_context=context)