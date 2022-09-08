import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { IUser, CognitoService } from '../cognito.service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss'],
})
export class SignUpComponent {

  loading: boolean;
  isConfirm: boolean;
  user: IUser;
  username!: string;
  password!: string;
  answer1!: string;
  answer2!: string;
  answer3!: string;
  key!: number;
  constructor(private router: Router,
    private cognitoService: CognitoService) {
    this.loading = false;
    this.isConfirm = false;
    this.user = {} as IUser;
  }

  public signUp(): void {
    this.loading = true;
    if (this.username != null && this.password != null)
      this.cognitoService.signUp(this.username, this.password, this.answer1, this.answer2, this.answer3, this.key.toString()).then((res) => {
        alert("Your booking id is " + res)
        this.router.navigate(['/home']);
      })
    else {
      alert("Please fill all required (marked *) fields")
    }
  }
}
