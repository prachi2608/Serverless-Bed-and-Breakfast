import { Component, OnInit } from '@angular/core';
import axios from "axios";
import { OrderFood } from './order-food.model';
import { CognitoService } from '.././cognito.service'
import { ToastService } from '../toast-service';
@Component({
  selector: 'app-order-food',
  templateUrl: './order-food.component.html',
  styleUrls: ['./order-food.component.scss']
})
export class OrderFoodComponent implements OnInit {
  foodOrder!: OrderFood
  foodItems: {
    "foodItem": string,
    "quantity": string
  }[] = []
  foodItem: string = ""
  quantity: number = 0
  loading: boolean = false;
  menuItems: any;
  constructor(private CognitoService: CognitoService, public toastService: ToastService) { }

  async ngOnInit() {
    this.foodOrder = new OrderFood()
    this.menuItems = await this.CognitoService.getFoodItems()
    console.log(this.menuItems)
  }
  addFoodItemInOrder(foodItem: string, quantity: number) {
    if (this.foodItems.find(ele => ele.foodItem == foodItem)) {
      this.foodItems = this.foodItems.filter(ele => ele.foodItem == foodItem)
    }
    this.foodItems.push({
      "foodItem": foodItem,
      "quantity": quantity.toString()
    })
    this.foodItem = ""
    this.quantity = 0
  }

  removeItem(foodItem: string) {
    this.foodItems = this.foodItems.filter(ele => ele.foodItem != foodItem)
  }

  orderFood() {
    this.CognitoService.orderFood(this.foodItems)
      .then((res: any) => {
        if (res.ResponseMetadata.HTTPStatusCode == 200) {
          this.foodItems = []
          this.foodItem = ""
          this.quantity = 0
        }
        this.CognitoService.getRoomNotification().then((res) => {
          alert("Your item is ordered successfully!!")
        })
      }).catch(() => {
        this.loading = false;
      });
  }
}
