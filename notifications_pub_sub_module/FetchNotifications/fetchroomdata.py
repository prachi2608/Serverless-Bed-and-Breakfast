from pkg_resources import Requirement
import firebase_admin
import json
from flask_cors import cross_origin
from firebase_admin import firestore

if not firebase_admin._apps:
   default_app = firebase_admin.initialize_app()

db = firestore.client()

@cross_origin(allowed_methods=['GET'])
def hello_world(request):
   docs = db.collection(u'notifications').stream()
   lis = []
   for doc in docs:
      lis.append(f'{doc.id} => {doc.to_dict()}')
   
   response = {
      "statusCode": 200,
      "body": json.dumps(lis),
      "headers": {
         "Content-Type": "application/json",
         "Access-Control-Allow-Origin": "*",
         "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
         "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
      },
   }

   return response