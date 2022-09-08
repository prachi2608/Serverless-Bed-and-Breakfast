import json
import requests
import urllib3
import json
import boto3
client = boto3.client('dynamodb')
result = {}
intent=""
numberOfBeds=""
available_rooms = []
food_items = []

def lambda_handler(event, context):
   intent_name = event['currentIntent']['name']
   response = None
   if intent_name == 'Food':
       return findMenus(event)
   if intent_name == 'Rooms':
       return findRooms(event)
   raise Exception('Intent with name ' + intent_name + ' not supported')
   return response


def getRoomAvailability(bed_number):
    payload = {
        "numberOfBeds": int(bed_number)
    }
    data = json.dumps(payload)
    print(data)
    url = 'https://ucv7nfndg4.execute-api.us-east-1.amazonaws.com/dev/getavailablerooms'
    response = requests.post(url,data=data)
    response_txt=json.loads(response.text.encode('utf8'))
    
    available_rooms = response_txt["numberOfRoomsAvailable"]
    return len(available_rooms)
    
def findRooms(intent_request):
    session_attributes = get_session_attributes(intent_request)
    bed_number = get_slot(intent_request, 'BedNumber')

    if not bed_number:
        return elicit_slot(intent_request, session_attributes, 'BedNumber', "How many beds do you want?")

    available_rooms =  getRoomAvailability(bed_number)
    print("yaaass")
    print (available_rooms)

    if available_rooms != 0:
        message = "We have {} room(s) available with {} bed(s). Please login to book a room".format(available_rooms, bed_number)
    else:
        message = "Sorry, we have no rooms available with {} bed(s)".format(bed_number)
    return close(intent_request, session_attributes, "Fulfilled", message)

    
def getMenuItems():
    url = 'https://ucv7nfndg4.execute-api.us-east-1.amazonaws.com/dev/getfooditems'
    response = requests.get(url)
    response_txt=json.loads(response.text.encode('utf8'))
    print (response_txt)
    
    food_items = response_txt["foodItems"]
    food_items_string = ", ".join(food_items)
    print (food_items_string)
    return food_items_string



def close(intent_request, session_attributes, fulfillment_state, message):

   return {
    'dialogAction': {
            'type': 'Close',
            'fulfillmentState': "Fulfilled",
            'message': {
                'contentType': 'PlainText',
                'content': message
            }
        }
   }

def get_session_attributes(intent_request):
   session_state = intent_request['sessionAttributes']
   return session_state

def get_slot(intent_request, slot_name):
   slots = get_slots(intent_request)
   if slots is not None and slot_name in slots and slots[slot_name] is not None:
       return slots[slot_name]
   else:
       return None

 
def get_slots(intent_request):
   return intent_request['currentIntent']['slots']


def elicit_slot(intent_request, session_attributes, slot_to_elicit, message):
   return {
       
        'dialogAction': {
            'type': 'ElicitSlot',
            'slotToElicit': slot_to_elicit,
    
            'intentName': intent_request['currentIntent']['name'],
            'message': {
                'contentType': 'PlainText',
                'content': message
            },
            "slots": intent_request['currentIntent']['slots']
        }
   }


    
def findMenus(intent_request):
    session_attributes = get_session_attributes(intent_request)
    food_items = getMenuItems()
    
    return close(intent_request, session_attributes, "Fulfilled","We have these items: {}. Please login to order. ".format(food_items))


