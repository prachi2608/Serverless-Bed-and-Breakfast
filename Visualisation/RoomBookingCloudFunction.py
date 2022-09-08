import json
import re
import boto3
import pandas as pd
import simplejson as json
from decimal import Decimal
from google.cloud import storage

def booking_room(request):
    session = boto3.Session(
        aws_access_key_id='ASIAVMP3EBDRX5R67AFM',
        aws_secret_access_key='tVOS8Y2RhYRPvcbIF9POyjaQHZfR9A9WpoFE6cTm',
        aws_session_token='FwoGZXIvYXdzEFwaDC2xFtyPXoz60+W/UiLAAYn172C+DF/yUc1X3n6NlsdG8BVQV9IwUUAd9As9Ab2EYtnx4G7mpYsQ7g/kPPR6eiT0xxkg/pUjJ7efL0YgjYtorAYKLJ8eI4lRz4Q4cWrIhFG6hcSKIglXpoPYOL6VKx72uhw8JIQM9Y/WA9t3f3Dfg708GkAOckfLD+8L7v3uE8YOWRJiHo04Kti9piVHM4+4cFTzevZto4vad1+h9K85sTszKHQyVz1AW1sLMj8lZBPldci2jnpWeb+sgD2inSi6lPaWBjIt40UueJc7Lpvn3WGNaGnoM5Ubrjp/JkUOnRVIDRpH0qArymGdTcib/jLlerdh',
        region_name='us-east-1'
    )
    print('session valid', session)

    storage_client = storage.Client()
    bucket = storage_client.bucket('serverless-visualisation')
    print('got bucket')
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('room')
    table1 = dynamodb.Table('FoodOrders')
    
    response = table.scan()
    print('db res: ', response)
    result = response['Items']
    print('result: ', result)
    df = pd.DataFrame(result)
    occupiedDf = df[df['occupied'] == True]
    grouped = occupiedDf.groupby(df['start_date'])
    resultDf = pd.DataFrame()
    resultDf1= pd.DataFrame()
    resultDf2= pd.DataFrame()

    for name,group in grouped:
      print(name)
      print(len(group))
      row = {'dates': name , 'count': len(group)}
      resultDf = resultDf.append(row, ignore_index = True)
      row1 = {'dates': name , 'total_num_of_beds': group['no_of_beds'].sum()}
      resultDf1 = resultDf1.append(row1, ignore_index = True)
      row2 = {'dates': name , 'total_price': group['price'].sum()}
      resultDf2 = resultDf2.append(row2, ignore_index = True)

  
    bucket.blob('room_booking.csv').upload_from_string(resultDf.to_csv(index=False), 'text/csv')
    bucket.blob('room_booking1.csv').upload_from_string(resultDf1.to_csv(index=False), 'text/csv')
    bucket.blob('room_booking2.csv').upload_from_string(resultDf2.to_csv(index=False), 'text/csv')



    print(result)
    return {
        'statusCode': 200,
        'body': json.dumps(result,use_decimal=True),
        'message': 'csv generated'
    }