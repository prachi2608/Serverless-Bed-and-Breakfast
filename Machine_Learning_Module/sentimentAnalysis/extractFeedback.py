from google.cloud import storage
import csv
from google.cloud import language_v1
from flask_cors import cross_origin


fileName="_feedbacksheet.csv"
bucketName="userfeedbacksheet"

@cross_origin(allowed_methods=['POST'])
def storeFeedback(request):
    
    request_json = request.get_json()
    if request_json:
      userEmail=request_json["EmailId"]
      feedback=request_json["Feedback"]
      service=request_json["Service"]
      print("service=====",service)
      client = storage.Client(project="csci-5410-s22-353221")
      bucket = client.get_bucket(bucketName)
      print("BucketName===",bucket)
      blob_object = bucket.blob(fileName)
      print("FileName===",blob_object)
      list = (getFeedback(request_json))
      fileExists = blob_object.exists()
      print("Exists======",fileExists)
      if(fileExists):
        blob_object.download_to_filename('/tmp/_feedbacksheet.csv')
        f = open('/tmp/_feedbacksheet.csv', 'a', newline="")
        writer = csv.writer(f)
        for i in range(len(list)-3):
            writer.writerow([list[i], list[i+1],list[i+2],list[i+3]])
            f.close()
            blob_object.upload_from_filename('/tmp/_feedbacksheet.csv')#upload data to file
          
             
        else:
            f = open('/tmp/_feedbacksheet.csv', 'a', newline="")
            headers = ['EmailId', 'Feedback', 'Service','UserExpierence']
            writer = csv.writer(f)
            writer.writerow(headers)
            for i in range(len(list)-3):
                writer.writerow(
                [list[i], list[i+1],list[i+2],list[i+3]])
            f.close()
            blob_object.upload_from_filename('/tmp/_feedbacksheet.csv')
      return "Feedback saved successfully!!"
            
def getFeedback(userData):
    userEmail=userData["EmailId"]
    feedback=userData["Feedback"]
    service=userData["Service"]
    expierence=[]
    content=[]
    client1 = language_v1.LanguageServiceClient() #Language Client for sentiment analysis
    document = language_v1.Document(content=feedback, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client1.analyze_sentiment(request={"document": document}).document_sentiment # Getting sentiment
    Sentiment_Score=sentiment.score # Sentiment Score
    if(Sentiment_Score<0):#checking sentiment score
        expierence.append("NEGATIVE")
    elif (Sentiment_Score==0):
        expierence.append("NEUTRAL")
    else :
        expierence.append("POSITIVE")
    content.append(userEmail)
    content.append(feedback)
    content.append(service)
    content.append(expierence[0])#appending first element
    return content



      
