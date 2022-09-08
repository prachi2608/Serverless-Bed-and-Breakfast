import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CognitoService } from '../cognito.service';

@Component({
  selector: 'app-room-list',
  templateUrl: './room-list.component.html',
  styleUrls: ['./room-list.component.scss']
})
export class RoomListComponent implements OnInit {
  rooms: any;

  constructor(private cognitoService: CognitoService, private router: Router) { }

  async ngOnInit() {
    this.rooms = await this.cognitoService.getRooms()
  }
  bookRoom(roomNo: { toString: () => string; }) {
    sessionStorage.setItem('RoomNo', roomNo.toString())
    this.router.navigate(['/book-room']);
  }
}
