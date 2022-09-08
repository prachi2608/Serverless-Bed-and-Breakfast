import { ApplicationRef, Component, ChangeDetectorRef } from '@angular/core';
import { Router } from '@angular/router';
import { IUser, CognitoService } from '../cognito.service';
@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.scss'],
})
export class SignInComponent {
  securityQuestions = ['What is your nickname?', 'What is your birth city?', `What is you mother's maiden name?`];
  randomQuestionNumber = 2;//Math.floor(Math.random() * (3 - 1 + 1) + 1);
  securityQuestion = this.securityQuestions[this.randomQuestionNumber];
  validationData = {
    securityAnswer: '',
    securityQuestionNumber: this.randomQuestionNumber.toString(),
    cipherAnswer: '',
    cipherQuestion: this.randomString(6)
  };
  loading: boolean;
  user: IUser;
  loginStage1: boolean = true
  loginStage2: boolean = false
  loginStage3: boolean = false

  constructor(private router: Router,
    private cognitoService: CognitoService, private ap: ApplicationRef, private cd: ChangeDetectorRef) {
    this.loading = false;
    this.user = {} as IUser;
  }
  ngOnInit() {

  }

  public signIn(): void {
    this.loading = true;
    if (this.loginStage1) {
      this.cognitoService.signIn(this.user, this.validationData)
        .then((res) => {
          if (res == "Authentication Failed") {
            this.ngOnInit()
            alert("Authentication Failed")
          }
          else {
            this.loginStage1 = false
            this.loginStage2 = true
          }
        }).catch(() => {
          this.loading = false;
        });
    }
    if (this.loginStage2) {
      this.cognitoService.securityVerification(this.user, this.validationData)
        .then((res) => {
          if (res == "Authentication Failed") {
            this.ngOnInit()
            alert("Authentication Failed")
          }
          else {
            this.loginStage2 = false
            this.loginStage3 = true
          }
        }).catch(() => {
          this.loading = false;
        });
    }
    if (this.loginStage3) {
      this.cognitoService.cipherVerification(this.user, this.validationData)
        .then((res) => {
          if (res == "Authentication Failed") {
            this.ngOnInit()
            alert("Authentication Failed")
          }
          else {
            this.cognitoService.storeSession(this.user.email).then((res) => {
              sessionStorage.setItem('Email', this.user.email)
              this.router.navigate(['/home']).then(() => {
                window.location.reload();
              });
            })
          }
        })
    }
  }


  randomString(length: number) {
    var randomChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    var result = '';
    for (var i = 0; i < length; i++) {
      result += randomChars.charAt(Math.floor(Math.random() * randomChars.length));
    }
    return result;
  }
}
