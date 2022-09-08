import { Component, OnInit } from '@angular/core';
import { CognitoService } from '../cognito.service';

@Component({
  selector: 'app-kitchen-inventory',
  templateUrl: './kitchen-inventory.component.html',
  styleUrls: ['./kitchen-inventory.component.scss']
})
export class KitchenInventoryComponent implements OnInit {
  kitchenInventory: any;
  constructor(private cognitoService: CognitoService) { }
  async ngOnInit() {
    this.kitchenInventory = await this.cognitoService.getKitchenInventory()
  }
}
