import { Component, OnInit } from '@angular/core';
import { CognitoService } from '../cognito.service';

@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.scss']
})
export class ReportsComponent implements OnInit {
  loggedOutUsers: any;
  unverifiedUsers: any;
  verifiedUsers: any;
  disabledUsers: any;
  enabledUsers: any;
  loggedInUsers: any

  constructor(private cognitoService: CognitoService) { }

  async ngOnInit() {
    this.loggedOutUsers = await this.cognitoService.getLoggedOutUsers()
    this.loggedInUsers = await this.cognitoService.getLoggedInUsersItems()
    this.unverifiedUsers = await this.cognitoService.getUnVerifiedUsers()
    this.verifiedUsers = await this.cognitoService.getVerifiedUsers()
    this.disabledUsers = await this.cognitoService.getDisabledUsers()
    this.enabledUsers = await this.cognitoService.getEnabledUsers()
  }
}
