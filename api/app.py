from flask import Flask
import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello, you are connected!'

@app.route('/newpost')
def newpost():
   return None

