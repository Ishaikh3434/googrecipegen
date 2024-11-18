# main.py (Flask backend)
from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import ssl
import os
from dotenv import load_dotenv
from googgen import recipeWriter
import uuid
load_dotenv()
hostdata={'certificate':'certificate.crt',
            'key':'private.key',
            'host':os.environ["HOST_IP"],
            'port':os.environ["HOST_PORT"]}
hostname=f"https://{hostdata['host']}:{hostdata['port']}/generate"
app = Flask(__name__)
writer=recipeWriter()
app.secret_key=os.environ["SESSION_KEY"]
# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html',path=hostname)

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.json.get('inputText')
    session['inputText'] = input_text
    output_text = writer.generate(input_text)
    session['outputText']=output_text
    return jsonify({'outputText': session['outputText']})

if __name__ == '__main__':
    context = ('certificate.crt', 'private.key')  # Path to your SSL certificate and key

    context=(hostdata['certificate'],hostdata['key'])
    app.run(host=hostdata['host'],port=hostdata['port'], ssl_context=context)