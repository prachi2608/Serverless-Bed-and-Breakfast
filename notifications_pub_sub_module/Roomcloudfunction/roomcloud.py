import json
from google.cloud import pubsub_v1 as pub
from flask_cors import cross_origin
from pkg_resources import Requirement

project_id = "csci-5410-352923"
topic_id = "roombooked"

@cross_origin(allowed_methods=['POST'])
def gcp_handler(request):
    dataBuffer = ("Your room is booked successfully!!")
    publisher = pub.PublisherClient()

    topic_path = publisher.topic_path(project_id, topic_id)
    publisher.publish(topic_path, dataBuffer.encode("utf-8"))

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
        },
    }

    print("Message published")
    return response