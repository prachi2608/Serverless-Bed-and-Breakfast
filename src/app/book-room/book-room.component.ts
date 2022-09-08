import { Component, OnInit } from '@angular/core';
import { CognitoService } from '../cognito.service';

@Component({
  selector: 'app-book-room',
  templateUrl: './book-room.component.html',
  styleUrls: ['./book-room.component.scss']
})
export class BookRoomComponent implements OnInit {
  numberOfDays!: number
  startDate: any
  endDate: any
  constructor(private cognitoService: CognitoService) { }

  ngOnInit(): void {
  }
  bookRoom() {
    this.cognitoService.bookRoom(sessionStorage.getItem('RoomNo'), this.numberOfDays, this.startDate, this.endDate).then((res) => {
      this.cognitoService.getRoomNotification().then((res) => {
        alert("Your room is booked successfully!!")
      })
    })
  }

}
