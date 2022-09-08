import json
import boto3
import requests
import random

DYNAMODB = boto3.client('dynamodb')

def lambda_handler(event, context):
    
    # TODO implement
    print(event)
    r1 = random.randint(1,1000000)
    print(r1)
    print("Type=====",type(r1))
    print("prachi")
    jsonData = json.loads(event["body"])
    print(jsonData)
    r = requests.post("https://us-central1-csci5410-a3-pb.cloudfunctions.net/register", json = jsonData)
    statusCode = r.status_code
    
    DYNAMODB.put_item(TableName='registration', Item={'id':{'S': jsonData["username"]},'answer1':{'S': jsonData["answer1"]},'answer2':{'S': jsonData["answer2"]},'answer3':{'S': jsonData["answer3"]},'UID':{'S': str(r1) }})
    
    response = {
        'statusCode': 200,
        'body': json.dumps(r1),
    #     'headers': {
    #     'Content-Type': 'application/json',
    #     'Access-Control-Allow-Origin': '*'
    #   },
    }
    
    return response