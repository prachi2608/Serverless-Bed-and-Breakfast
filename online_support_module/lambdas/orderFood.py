import json
import boto3
from datetime import date
import uuid

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
    food_item = payload['foodItem']
    quantity = payload['quantity']
    user_id = payload['user_id']
    # response body
    res_body = {}
    #res_body['x'] =x 
    res_body ['order_id'] = order_food(user_id,food_item,int(quantity))
    
    
    # http response
    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'application/json'
    http_res['body'] = json.dumps(res_body)
    print(http_res)
    return http_res
    
def order_food(user_id,food_item,quantity):
    print(quantity)
    print("yyaa")
    
    table = dynamodb.Table('FoodOrders')
    table_items = table.scan()
    # max = 0;
    # for i in table_items['Items']:
    #     if i['id'] >= max:
    #         max = i['id']
    order_id = str(uuid.uuid4())
    table.put_item(Item={
            'userid': user_id,
            'foodItems': food_item,
            'id':order_id,
            'preptime_min':20,
            'price': 12,
            'date': str(date.today())
        })
    return order_id
    



