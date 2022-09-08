import json
import boto3

COGNITO = boto3.client('cognito-idp')


def lambda_handler(event, context):
    # TODO implement
    cog_response = COGNITO.list_users(
        UserPoolId='us-east-1_g8pPHdEzU',
        Filter="status= 'Disabled'"
    )

    users = cog_response["Users"]

    response = []

    for user in users:
        user_json = {}
        user_json["username"] = user["Attributes"][2]["Value"]
        user_json["user_created_on"] = user["UserCreateDate"].isoformat()
        user_json["user_modified_on"] = user["UserLastModifiedDate"].isoformat()
        response.append(user_json)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
