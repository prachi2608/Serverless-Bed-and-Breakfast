import json
import boto3

DYNAMODB = boto3.client('dynamodb')


def lambda_handler(event, context):
    # TODO implement
    print(event)

    creds = json.loads(event["body"])
    username = creds["username"]
    securityQuestionNumber = creds["securityQuestionNumber"]
    securityAnswer = creds["securityAnswer"]
    answerVerification = False

    response = DYNAMODB.get_item(TableName='registration',
                                 Key={
                                     'id': {'S': username},
                                 })

    item = response["Item"]
    print(item)
    answerNumber = 'answer' + securityQuestionNumber
    print(item[answerNumber]['S'])
    print(securityAnswer)
    if(item[answerNumber]['S'] == securityAnswer):
        answerVerification = True

    if(answerVerification):
        return {
            'statusCode': 200,
            'body': json.dumps('Authentication Success')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('Authentication Failed')
        }
