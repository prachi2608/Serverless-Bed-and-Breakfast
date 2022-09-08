import json
import boto3
client = boto3.client('dynamodb')
dynamodb =  boto3.resource('dynamodb')
result = []
intent=""
food_items=""
def lambda_handler(event, context):
    #get query from string param inputs
    #x = event['queryStringParameters']['x']
    

    # response body
    res_body = {}
    #res_body['x'] =x 
    res_body ['foodItems'] = room(food_items)
    
    # http response
    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'application/json'
    http_res['body'] = json.dumps(res_body)
    print(http_res)
    return http_res
    
def room(no_of_beds):
    result = []
    count = 0
    table =  dynamodb.Table('MenuItems').scan()
    for i in table['Items']:
            result.append(str(i['name']))
    print("result:" )
    print(result)
    return result
    



