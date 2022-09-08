import json
import boto3

DYNAMODB = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    
    result = DYNAMODB.scan(TableName='FoodItems')
    print(result["Items"])
    
    foodItems = []
    
    for item in result["Items"]:
        foodItem = {}
        foodItem["name"] = item["name"]["S"]
        foodItem["id"] = item["id"]["N"]
        foodItems.append(foodItem)
    
    return {
        'statusCode': 200,
        'body': json.dumps(foodItems)
    }
