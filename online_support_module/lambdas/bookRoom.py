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
    room_number = payload['roomNumber']
    no_of_days = payload['numberOfDays']
    start_date = payload['startDate']
    email_id =  payload['email_id']
    # response body
    res_body = {}
    #res_body['x'] =x 
    res_body ['updated'] = book_room(room_number,no_of_days,start_date, email_id)
    
    
    # http response
    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'application/json'
    http_res['body'] = json.dumps(res_body)
    print(http_res)
    return http_res
    
def book_room(room_number,no_of_days,start_date, email_id):
    updated = False
    result = []
    table = dynamodb.Table('room')
    response = table.update_item(                                       
        Key={
            'room_no': room_number
        },
        UpdateExpression="set occupied = :o, no_of_days=:n, start_date=:d, email_id=:e,price=:p",
        ExpressionAttributeValues={
          
          # decimal, Converts a finite Decimal instance to a rational number, exactly.
            ':o': True,                           
            ':n': no_of_days,
            ':d': start_date,
            ':e': email_id,
            ':p':50*no_of_days
        },
        ReturnValues="UPDATED_NEW"
    )
    updated = True
    # result = table.get_item(
    #     Key={
    #         'room_no':room_number
    #     })
    return True
    



