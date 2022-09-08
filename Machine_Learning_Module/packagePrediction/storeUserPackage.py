from datetime import date
import firebase_admin
from firebase_admin import firestore
from google.cloud import storage
import csv
from google.cloud import storage
from flask_cors import cross_origin

fileName="_packageSheet.csv"
bucketName="userpackagestorage"
projectId="csci-5410-s22-353221"

# Refence: https://firebase.google.com/docs/firestore/manage-data/add-data#python_4.


if not firebase_admin._apps:
    
    default_app = firebase_admin.initialize_app()

db = firestore.client()


@cross_origin(allowed_methods=['POST'])
def storePackage(request):
    
    request_data = request.get_json()
    email = request_data["userEmail"]
    package = request_data["Package"]
    price= request_data["PackagePrice"]
    
    db.collection(u'userSelectedPackage').document(email).set({
        "Package_Price":price,
        "Email":email,
        "Selected_Package":package
    })
    client = storage.Client(project="csci-5410-s22-353221")
    bucket = client.get_bucket(bucketName)#get bucket name
    blob_object = bucket.blob(fileName)#get blob object
    list = (storeP(request_data))
    fileExists = blob_object.exists()
    print("Exists======",fileExists)
    if(fileExists):
        blob_object.download_to_filename('/tmp/_packageSheet.csv')
        f = open('/tmp/packageSheet.csv', 'a', newline="")
        writer = csv.writer(f)
        for i in range(len(list)-3):
            writer.writerow([list[i], list[i+1],list[i+2],list[i+3]])
            f.close()
            blob_object.upload_from_filename('/tmp/_packageSheet.csv')
             
        else:
           
            f = open('/tmp/_packageSheet.csv', 'a', newline="")
            headers = ['EmailId', 'Package', 'Package_Price','Booking_Date']
            writer = csv.writer(f)
            writer.writerow(headers)
            for i in range(len(list)-3):
                writer.writerow(
                [list[i], list[i+1],list[i+2],list[i+3]])
            f.close()
            blob_object.upload_from_filename('/tmp/_packageSheet.csv')
    return "Tour Booked Successfully"

def storeP(userData):
    email=userData["userEmail"]
    package=userData["Package"]
    price=userData["PackagePrice"]
    content=[]
    content.append(email)
    content.append(package)
    content.append(price)
    content.append(date.today())
    return content


    