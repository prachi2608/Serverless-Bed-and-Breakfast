import { Component, OnInit } from '@angular/core';
import { CognitoService } from '../cognito.service';

@Component({
  selector: 'app-feedback',
  templateUrl: './feedback.component.html',
  styleUrls: ['./feedback.component.scss']
})
export class FeedbackComponent implements OnInit {
  service: string = ""
  feedback: string = ""
  constructor(private cognitoService: CognitoService) { }

  ngOnInit(): void {
  }

  sendFeedback(service: string, feedback: string) {
    this.cognitoService.addFeedback(this.service, this.feedback).then((res) => {
      alert(res.error.text)
    })
  }

}
