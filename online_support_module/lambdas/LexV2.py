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
   intent_name = event['sessionState']['intent']['name']
   response = None
   if intent_name == 'BookRoom':
       return bookRoomIntent(event)
   if intent_name == 'OrderFood':
       return orderFoodintent(event)
   if intent_name == 'AvailableRooms':
       return checkAvailableRooms(event)
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
    
def checkAvailableRooms(intent_request):
    session_attributes = get_session_attributes(intent_request)
    bed_number = get_slot(intent_request, 'BedNumber')

    if not bed_number:
        return elicit_slot(intent_request, session_attributes, 'BedNumber', "How many beds do you want?")

    available_rooms =  getRoomAvailability(bed_number)
    print("yaaass")
    print (available_rooms)

    if available_rooms != 0:
        message = "We have {} room(s) available with {} bed(s).".format(available_rooms, bed_number)
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

def placeOrder(food_item,quantity):
    payload = {
        "foodItem": food_item,
        "quantity": int(quantity)
    }
    data = json.dumps(payload)
    print(data)
    url = 'https://ucv7nfndg4.execute-api.us-east-1.amazonaws.com/dev/orderfood'
    response = requests.post(url,data=data)
    response_txt=json.loads(response.text.encode('utf8'))
    order_id = response_txt["order_id"]
    return order_id
    
def orderFoodintent(intent_request):
    session_attributes = get_session_attributes(intent_request)
    food_items = getMenuItems()
    food = get_slot(intent_request, 'Food')
    quantity = get_slot(intent_request, 'Quantity')
    complete = get_slot(intent_request, 'complete')

    if not food:
               return elicit_slot(intent_request, session_attributes, 'Food', "We have these items: {}. What do you want to order?".format(food_items))

    if not quantity:
               return elicit_slot(intent_request, session_attributes, 'Quantity', "How many {} do you want?".format(food))
    
    if not complete:
              return elicit_slot(intent_request, session_attributes, 'complete', "You have requested for {} of {}. Can I place this order?"
                                  .format(quantity,
                                          food))
                                          
    if complete.lower() == 'yes':
        order_id = placeOrder(food,quantity)
        return close(intent_request, session_attributes, "Fulfilled", "Your order for {} quantities of {} has been placed with order id {}.".format(quantity,food,order_id) )
    elif complete.lower() == 'no':
        return close(intent_request, session_attributes, "Fulfilled", "Your request has been cancelled!")
    else:
        return elicit_slot(intent_request, session_attributes, 'complete',
                          'Enter valid option (yes or no)')

def bookRoomIntent(intent_request):
    session_attributes = get_session_attributes(intent_request)
    bed_number = get_slot(intent_request, 'BedNumber')
    checkin_date = get_slot(intent_request, 'CheckinDate')
    no_of_nights = get_slot(intent_request, 'NumberOfNights')
    complete = get_slot(intent_request, 'complete')

    if not bed_number:
               return elicit_slot(intent_request, session_attributes, 'BedNumber', "How many number of beds do you want in the room?")

    if not checkin_date:
               return elicit_slot(intent_request, session_attributes, 'CheckinDate', "What is your check in date?")
    
    if not no_of_nights:
               return elicit_slot(intent_request, session_attributes, 'NumberOfNights', "How many nights do you want to stay?")

    if not complete:
              return elicit_slot(intent_request, session_attributes, 'complete', "You have requested for {}-bed(s) room for {} nights and the checkin date is {}. Can I place this order?"
                                  .format(bed_number,
                                          no_of_nights,
                                          checkin_date))
                                          
    if complete.lower() == 'yes':
        booked_room = bookRoom(bed_number,no_of_nights,checkin_date)
        return close(intent_request, session_attributes, "Fulfilled", "Your request has been placed successfully. We have booked room no {} for you.".format(booked_room))
    elif complete.lower() == 'no':
        return close(intent_request, session_attributes, "Fulfilled", "Your request has been cancelled!")
    else:
        return elicit_slot(intent_request, session_attributes, 'complete',
                          'Enter valid option (yes or no)')

    # return close(intent_request, session_attributes, "Fulfilled", "Your request has been placed successfully")

def close(intent_request, session_attributes, fulfillment_state, message):
   intent_request['sessionState']['intent']['state'] = fulfillment_state
   return {
       'sessionState': {
           'sessionAttributes': session_attributes,
           'dialogAction': {
               'type': 'Close'
           },
           'intent': intent_request['sessionState']['intent']
       },
       'messages': [{
           'contentType': 'PlainText',
           'content': message
       }],
       'sessionId': intent_request['sessionId'],
       'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in
       intent_request else None
   }

def get_session_attributes(intent_request):
   session_state = intent_request['sessionState']
   if 'sessionAttributes' in session_state:
       return session_state['sessionAttributes']
   return {}

def get_slot(intent_request, slot_name):
   slots = get_slots(intent_request)
   if slots is not None and slot_name in slots and slots[slot_name] is not None:
       return slots[slot_name]['value']['interpretedValue']
   else:
       return None

 
def get_slots(intent_request):
   return intent_request['sessionState']['intent']['slots']


def elicit_slot(intent_request, session_attributes, slot_to_elicit, message):
   return {
       'sessionState': {
           'sessionAttributes': session_attributes,
           'dialogAction': {
               'type': 'ElicitSlot',
               'slotToElicit': slot_to_elicit,
           },
           'intent': intent_request['sessionState']['intent']
       },
       'messages': [{
           'contentType': 'PlainText',
           'content': message
       }],
       'sessionId': intent_request['sessionId'] ,
       'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
   }

def bookRoom(numberOfBeds,numberOfDays,startDate):
    payload = {
        "numberOfBeds": int(numberOfBeds)
    }
    data = json.dumps(payload)
    print(data)
    url = 'https://ucv7nfndg4.execute-api.us-east-1.amazonaws.com/dev/getavailablerooms'
    response = requests.post(url,data=data)
    response_txt=json.loads(response.text.encode('utf8'))
    print (response_txt)
    
    available_rooms = response_txt["numberOfRoomsAvailable"]
    print (available_rooms)
    
    
    if len(available_rooms) != 0:
        url = 'https://ucv7nfndg4.execute-api.us-east-1.amazonaws.com/dev/bookroom'
        payload = {
        "roomNumber":int(available_rooms[0]),
        "numberOfDays":int(numberOfDays),
        "startDate":str(startDate)
        }
        data = json.dumps(payload)
        response = requests.post(url,data=data)
        booked_room = available_rooms[0]
        return booked_room
 