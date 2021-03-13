from flask import Flask, request, Response
from common.subreddits import Subreddit
import jsonify
import datetime
import boto3

app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello, you are connected!'

@app.route('/subreddits/submit', methods=['POST'])
def new_subr():
  body = request.get_json()
  current_time = datetime.datetime.now()
  new_sub = Subreddit(**body, date_created=current_time)
  return {'name': str(new_sub.name),
  'date_created': str(new_sub.date_created)
  }, 200