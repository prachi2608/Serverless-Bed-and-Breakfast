import { Component, OnInit } from '@angular/core';
import { LexRuntime } from 'aws-sdk';
import { Message } from '../chatbot/message.model';

@Component({
  selector: 'app-chatbot-unregister',
  templateUrl: './chatbot-unregister.component.html',
  styleUrls: ['./chatbot-unregister.component.scss']
})
export class ChatbotUnregisterComponent implements OnInit {

  lexRuntime = new LexRuntime();
  userInput: string = '';
  chatMsg: Message[] = [];
  initState: string | undefined = 'Hi, How Can I help you';
  messages: any;
  constructor() { }

  ngOnInit(): void {
    this.messages.push(new Message(this.initState?.toString(), 'Bot'));
  }

  postMessage() {
    var params = {
      botAlias: 'betaunreg',
      botName: 'BandBunregistered',
      inputText: 'flowers',
      userId: 'user1986318',
    };

    this.lexRuntime = new LexRuntime({
      accessKeyId: 'ASIAVMP3EBDRX5R67AFM',
      secretAccessKey: 'tVOS8Y2RhYRPvcbIF9POyjaQHZfR9A9WpoFE6cTm',
      sessionToken: 'FwoGZXIvYXdzEFwaDC2xFtyPXoz60+W/UiLAAYn172C+DF/yUc1X3n6NlsdG8BVQV9IwUUAd9As9Ab2EYtnx4G7mpYsQ7g/kPPR6eiT0xxkg/pUjJ7efL0YgjYtorAYKLJ8eI4lRz4Q4cWrIhFG6hcSKIglXpoPYOL6VKx72uhw8JIQM9Y/WA9t3f3Dfg708GkAOckfLD+8L7v3uE8YOWRJiHo04Kti9piVHM4+4cFTzevZto4vad1+h9K85sTszKHQyVz1AW1sLMj8lZBPldci2jnpWeb+sgD2inSi6lPaWBjIt40UueJc7Lpvn3WGNaGnoM5Ubrjp/JkUOnRVIDRpH0qArymGdTcib/jLlerdh',
      region: 'us-east-1'
    });
    params.inputText = this.userInput;
    this.lexRuntime.postText(params, (err, data) => {
      if (err) {
        console.log(err, err.stack); // an error occurred
      }
      else {
        this.initState = data.message;
      }
      this.chatMsg.push(new Message(this.userInput, 'You'));
      this.userInput = "";
      this.chatMsg.push(new Message(this.initState, 'Bot'));
    }
    );
  }
}
