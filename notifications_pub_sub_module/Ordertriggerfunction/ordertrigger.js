const Firestore = require('@google-cloud/firestore');

const PROJECTID = 'csci-5410-352923';
const COLLECTION_NAME = 'notifications';
  const firestore = new Firestore({
  projectId: PROJECTID,
  timestampsInSnapshots: true
})


exports.helloPubSub = (event, context) => {
  const message = event.data
    ? Buffer.from(event.data, 'base64').toString()
    : 'Hello, World';
  console.log(message);

   return firestore.collection(COLLECTION_NAME).add(
     { message : message,
       type: "order",
       createdAt: Firestore.Timestamp.now() } 
    )
};
