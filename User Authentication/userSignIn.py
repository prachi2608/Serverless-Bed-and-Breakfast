# User Authentication Module
import json
import boto3

COGNITO = boto3.client('cognito-idp')


def lambda_handler(event, context):
    # TODO implement
    print(event)

    creds = json.loads(event["body"])

    try:
        print("In try")
        response = COGNITO.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': creds["username"],
                'PASSWORD': creds["password"]
            },
            ClientId='28kdg20e2ia8omampl92j0nulf'
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Authentication Success')
        }
    except:
        print('In except')
        return {
            'statusCode': 200,
            'body': json.dumps('Authentication Failed')
        }
