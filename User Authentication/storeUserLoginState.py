import json
import boto3
import datetime

DYNAMODB = boto3.client('dynamodb')


def lambda_handler(event, context):
    # TODO implement

    creds = json.loads(event["body"])
    email = creds['username']

    userExists = check_if_item_exist_login_statistics(email)
    if(userExists):
        DYNAMODB.update_item(
            TableName='UserLoginStatistics',
            Key={
                'username': {'S': email}
            },
            UpdateExpression="set login = :l, userStatus = :t",
            ExpressionAttributeValues={
                ':l': {'S': datetime.datetime.utcnow().isoformat()},
                ':t': {'BOOL': True}
            }
        )
    else:
        DYNAMODB.put_item(TableName='UserLoginStatistics', Item={'username': {'S': email}, 'login': {
                          'S': datetime.datetime.utcnow().isoformat()}, 'logout': {'S': ''}, 'userStatus': {'BOOL': True}})

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def check_if_item_exist_login_statistics(username):
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
