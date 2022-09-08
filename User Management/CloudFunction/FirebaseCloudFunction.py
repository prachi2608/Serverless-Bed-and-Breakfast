/**
 * Responds to any HTTP request.
 *
 * @param {!express:Request} req HTTP request context.
 * @param {!express:Response} res HTTP response context.
 */

const fs = require('firebase-admin');
const serviceAccount = require(__dirname+"/serviceAccountkey.json");

exports.helloWorld = async (req, response) => {
  // Firebase Database

  console.log(req.body);
if (!fs.apps.length) {
   fs.initializeApp({
      credential: fs.credential.cert(serviceAccount)
  });
}else {
   fs.app(); // if already initialized, use that one
}


  const firestore_db = fs.firestore();
  const jsonData ={
    'email' : req.body.username,
    'key' : req.body.key
  }

  const user = firestore_db.collection("registration_data").doc(req.body.username).set(jsonData);

  
  console.log(req.body);
  response.setHeader( 'Access-Control-Allow-Origin','*');
  response.setHeader('Access-Control-Allow-Methods', 'GET,POST');
  response.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  response.setHeader('Access-Control-Max-Age', '3600');

  response.status(200).send(req.body) 
   
};


