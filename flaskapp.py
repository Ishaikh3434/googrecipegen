# main.py (Flask backend)
from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import ssl
import os
import time
from dotenv import load_dotenv
from googgen import recipeWriter
import uuid
load_dotenv()
hostdata={'certificate':'certificate.crt', #SSL certificate path
            'key':'private.key', #SSL private key path
            'host':os.environ["HOST_IP"],
            'port':os.environ["HOST_PORT"]}
hostname=f"https://{hostdata['host']}:{hostdata['port']}/generate" #Composite the path to the server using provided host ip and port
app = Flask(__name__)
writer=recipeWriter() #initialise Gemini recipe generator
app.secret_key=os.environ["SESSION_KEY"] 
# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html',path=hostname) #pass the composited host path to the frontend

@app.route('/generate', methods=['POST'])
def generate():
    print(f"Data recieved!")
    startime=time.time()
    input_text = request.json.get('inputText')
    session['inputText'] = input_text
    output_text = writer.generate(input_text)
    session['outputText']=output_text
    print(f"Data processed in {time.time()-startime}s")
    return jsonify({'outputText': session['outputText']})

if __name__ == '__main__':

    context=(hostdata['certificate'],hostdata['key'])
    app.run(host=hostdata['host'],port=hostdata['port'], ssl_context=context,debug=True)