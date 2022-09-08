import json
import boto3
client = boto3.client('dynamodb')
dynamodb =  boto3.resource('dynamodb')
result = []
intent=""
no_of_beds=""
def lambda_handler(event, context):
    #get query from string param inputs
    #x = event['queryStringParameters']['x']
    
    payload= json.loads(event['body'])
    print(payload)
    no_of_beds = payload['numberOfBeds']
    # response body
    res_body = {}
    #res_body['x'] =x 
    res_body ['numberOfRoomsAvailable'] = room(no_of_beds)
    
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
    table =  dynamodb.Table('room').scan()
    print(table)
    for i in table['Items']:
        if  ('occupied' in i and not i['occupied'] and i['no_of_beds'] == no_of_beds):
                print (i['room_no'])
                result.append(str(i['room_no']))
    print("result:" )
    print(result)
    return result
    



