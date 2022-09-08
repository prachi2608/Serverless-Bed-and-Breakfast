
from importlib.resources import Package
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
from flask import jsonify
import firebase_admin
from flask_cors import cross_origin
from firebase_admin import credentials, firestore
if not firebase_admin._apps:

    default_app = firebase_admin.initialize_app()

#Reference: https://github.com/googleapis/python-aiplatform/blob/main/samples/snippets/prediction_service/predict_tabular_classification_sample.py.


db = firestore.client()

@cross_origin(allowed_methods=['POST'])
def generateTour(request):

 
    request_json = request.get_json()
    global classesList
    global classList
    
    if request_json:
         dict={
             "Adults":request_json["Adults"],
             "Child":request_json["Child"],
             "stayDuration":request_json["stayDuration"],
             }
  
    predictionResponse=predict_tabular_classification_sample(project= "csci-5410-s22-353221",
    endpoint_id="6522399732990476288",
    instance_dict= dict,
    location= "us-central1",
    api_endpoint="us-central1-aiplatform.googleapis.com")
    maxResponse=max(zip(predictionResponse.values(), predictionResponse.keys()))[1]#.returning key of maximum confidence
    doc_ref = db.collection(u'userPackage').document(maxResponse)
    doc = doc_ref.get()
    if doc.exists:
        print(f'Document data=================: {doc.to_dict()}')
        return doc.to_dict()
    else:
        print(u'No such document!')
        return "Package Not Exist in Database"


def predict_tabular_classification_sample(
    project= "csci-5410-s22-353221",
    endpoint_id="6522399732990476288",
    instance_dict= dict,
    location= "us-central1",
    api_endpoint="us-central1-aiplatform.googleapis.com",
):
    aiplatform.init(project=project, location=location)#initialize platform
    final_response={}
    client_options = {"api_endpoint": api_endpoint}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    instance = json_format.ParseDict(instance_dict, Value())
    instances = [instance]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())#converting to json format
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    final_response={}
    predictions = response.predictions
    for prediction in predictions:
        
        predictionResponse=dict(prediction)
        keyValue=list(predictionResponse.keys())[0]
        if(keyValue=="classes"):
            classesList=predictionResponse["classes"]#getting class list
            scoreList=predictionResponse["scores"]#getting score list
            combineDictionary=zip(classesList,scoreList)
        
            return dict(combineDictionary)
        else:
            scoreList=predictionResponse["scores"]
            classList=predictionResponse["classes"]   
            combineDictionary=zip(classList,scoreList)
            return dict(combineDictionary)#returning the dictionary

    
# [END aiplatform_predict_tabular_classification_sample]