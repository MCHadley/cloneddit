import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

users_table = dynamodb.Table('users')
subreddits_table = dynamodb.Table('subreddits')
posts_table = dynamodb.Table('posts')
comments_table = dynamodb.Table('comments')

# print(users_table.scan())