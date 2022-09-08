import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { CognitoService } from './cognito.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {

  isAuthenticated: boolean;
  useremail!: string | null;

  constructor(private router: Router,
    private cognitoService: CognitoService, private cd: ChangeDetectorRef) {
    this.isAuthenticated = false;
  }

  public ngOnInit(): void {
    this.useremail = sessionStorage.getItem("Email")
    if (this.useremail) {
      this.isAuthenticated = true
      this.cd.detectChanges()
    }
  }

  public signOut(): void {
    this.cognitoService.signOut()
      .then(() => {
        this.router.navigate(['/signIn']);
        window.location.reload()
      });
  }
}
