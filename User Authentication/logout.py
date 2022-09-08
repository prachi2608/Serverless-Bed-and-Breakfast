import json
import boto3
import datetime

DYNAMODB = boto3.client('dynamodb')


def lambda_handler(event, context):
    # TODO implement

    jsonBody = json.loads(event['body'])
    email = jsonBody["username"]
    userExists = check_if_item_exist(email)
    if(userExists):
        DYNAMODB.update_item(
            TableName='UserLoginStatistics',
            Key={
                'username': {'S': email}
            },
            UpdateExpression="set logout = :l, userStatus = :t",
            ExpressionAttributeValues={
                ':l': {'S': datetime.datetime.utcnow().isoformat()},
                ':t': {'BOOL': False}
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def check_if_item_exist(username):
    response = DYNAMODB.get_item(
        TableName='UserLoginStatistics',
        Key={
            'username': {'S': username},
        }
    )
    if 'Item' in response:
        return True
    else:
        return False
