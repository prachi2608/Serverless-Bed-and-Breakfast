import json
import boto3

DYNAMODB = boto3.client('dynamodb')


def lambda_handler(event, context):
    # TODO implement

    result = DYNAMODB.scan(TableName='UserLoginStatistics')
    print(result["Items"])

    users = []

    for item in result["Items"]:
        if(item["userStatus"]["BOOL"]):
            user = {}
            user["login"] = item["login"]["S"]
            user["logout"] = item["logout"]["S"]
            user["username"] = item["username"]["S"]
            users.append(user)

    return {
        'statusCode': 200,
        'body': json.dumps(users)
    }
