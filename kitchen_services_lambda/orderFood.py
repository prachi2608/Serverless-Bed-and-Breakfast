import json
import boto3 as boto3
from datetime import datetime
import uuid

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('FoodOrders')

def lambda_handler(event, context):
    
    # create and configure dynamodb
    body = json.loads(event['body'])
    dataToUpload = body["foodItems"]
    print(dataToUpload)
    foodItemsTable = dynamodb.Table('FoodItems')
    allFoodItemsInOrder = ""
    totalPreptime = 0
    totalPrice = 0
    allIngredientsInOrder = ""
    for i in dataToUpload:
        allFoodItemsInOrder += i['foodItem'] + ","
        foodItem = foodItemsTable.get_item(Key={'name': i['foodItem']})
        totalPrice += int(foodItem['Item']['price']) * int(i['quantity'])
        totalPreptime += int(foodItem['Item']['preptime_min'])
        allIngredientsInOrder += foodItem['Item']['ingredients']


    res = table.put_item(Item={
        'foodItems': allFoodItemsInOrder,
        'preptime_min': int(totalPreptime),
        'price': int(totalPrice),
        'id': str(uuid.uuid4()),
        'userid': body["email"],
        'date':datetime.today().strftime('%Y-%m-%d')
        })
    
    kitchenInventoryTable = dynamodb.Table('KitchenInventory')
    allIngredients = allIngredientsInOrder.replace(", ", ",").replace(" ,", ",").split(",")
    print(allIngredients)
    for item in allIngredients:
        if len(item)==0:
            continue;
        else:
            res1 = kitchenInventoryTable.update_item(
                Key={
                    'name': item
                },
                UpdateExpression='SET #FIELD = #FIELD - :value',
                ExpressionAttributeNames={
                    '#FIELD': 'quantity',
                },
                ExpressionAttributeValues={
                    ':value': 1
                },
                ReturnValues='UPDATED_NEW'
            )
            
            
            
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
