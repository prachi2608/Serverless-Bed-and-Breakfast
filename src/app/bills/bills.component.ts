import { Component, OnInit } from '@angular/core';
import { CognitoService } from '../cognito.service';
import * as _ from 'lodash';

@Component({
  selector: 'app-bills',
  templateUrl: './bills.component.html',
  styleUrls: ['./bills.component.scss']
})
export class BillsComponent implements OnInit {
  generatedBills: any;

  constructor(private cognitoService: CognitoService) { }

  ngOnInit(): void {
    this.cognitoService.generateBills().then((res: any) => {
      this.generatedBills = res
      this.generatedBills = this.generatedBills.filter((ele: any) => ele.userid == sessionStorage.getItem('Email'))
      const groupped = _.mapValues(_.groupBy(this.generatedBills, 'date'),
        (clist: any[]) => clist.map((timetable: any) => _.omit(timetable, 'date')));
      this.generatedBills = (Object).entries(groupped)
      console.log(this.generatedBills)
    })
  }
  getFoodTotal(item: any) {
    if (item.food_total > 0)
      return item.food_total
  }
  getRoomTotal(item: any) {
    if (item.room_total > 0)
      return item.room_total
  }
}
