from flask import Flask, request, Response
from common.subreddits import Subreddit
from common.user import User
from data import db
import jsonify
import uuid
import datetime
import boto3

app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello, you are connected!'

@app.route('/subr/submit', methods=['POST'])
def new_subr():
  body = request.get_json()
  current_time = datetime.datetime.now()
  new_sub = Subreddit(**body, date_created=current_time)
  return {'name': str(new_sub.name), 'date_created': str(new_sub.date_created)}, 200

@app.route('/users/new', methods=['POST'])
def new_user():
   body = request.get_json()
   current_time = str(datetime.datetime.now())
   userid = str(uuid.uuid1())
   new_user = User(**body, uid=userid, date_created=current_time)
   # return {'user': str(new_user.username)}, 200
   response = db.users_table.put_item(
      Item = {
         'uid': new_user.uid,
         'username': new_user.username,
         'pass': new_user.password,
         'date_created': new_user.date_created
      }
   )
   if response:
      return {'name': str(new_user.username), 'uuid': str(new_user.uid)}, 200
   else:
      return('Response did not succeed')