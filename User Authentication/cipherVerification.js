const express = require("express");
const app = express();
const cors = require("cors");
const fs = require('firebase-admin');
const serviceAccount = require(__dirname+"/csci5308-firebase-adminsdk-c4bz3-40b9d4f025.json");

app.use(cors());

fs.initializeApp({
    credential: fs.credential.cert(serviceAccount)
});

app.post("/", (req, res) => {
  const email = req.body.email;
  const cipherQuestion = req.body.cipherQuestion;
  const cipherAnswer = req.body.cipherAnswer;
  var encryptedText = "";

  const firestore_db = fs.firestore();

  firestore_db.collection("registration_data").doc(email).get().then((user) => {
    var key = parseInt(user.data().key);
    for (let i=0;i<cipherQuestion.length;i++){
      if(cipherQuestion[i].charCodeAt(0)>=65 && cipherQuestion[i].charCodeAt(0)<=90){
    		let ch = String.fromCharCode((cipherQuestion[i].charCodeAt(0) + key-65) % 26 + 65);
        console.log(ch);
        encryptedText = encryptedText + ch;
      }else{
    		let ch = String.fromCharCode((cipherQuestion[i].charCodeAt(0) + key-97) % 26 + 97);
        console.log(ch);
        encryptedText = encryptedText + ch;
      }
    }

    if(encryptedText == cipherAnswer){
      res.send('Authentication Success');
    }else{
      res.send('Authentication Failed');
    }

  });
});


exports.app = app;