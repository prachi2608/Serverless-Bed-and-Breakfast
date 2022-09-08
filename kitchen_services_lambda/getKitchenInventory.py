import json
import boto3

DYNAMODB = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    
    result = DYNAMODB.scan(TableName='KitchenInventory')
    print(result["Items"])
    
    foodItems = []
    
    for item in result["Items"]:
        foodItem = {}
        foodItem["name"] = item["name"]["S"]
        foodItem["quantity"] = item["quantity"]["N"]
        foodItems.append(foodItem)
    
    return {
        'statusCode': 200,
        'body': json.dumps(foodItems)
    }
