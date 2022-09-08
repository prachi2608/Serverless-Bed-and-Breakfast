import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BillsComponent } from './bills/bills.component';
import { BookRoomComponent } from './book-room/book-room.component';
import { ChatbotUnregisterComponent } from './chatbot-unregister/chatbot-unregister.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
import { FeedbackComponent } from './feedback/feedback.component';
import { KitchenInventoryComponent } from './kitchen-inventory/kitchen-inventory.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { NotificationsComponent } from './notifications/notifications.component';
import { OrderFoodComponent } from './order-food/order-food.component';
import { ProfileComponent } from './profile/profile.component';
import { ReportsComponent } from './reports/reports.component';
import { RoomListComponent } from './room-list/room-list.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { TourPackageComponent } from './tour-package/tour-package.component';
import { VisualizationComponent } from './visualization/visualization.component';

const routes: Routes = [
  {
    path: 'home',
    component: LandingPageComponent,
  },
  {
    path: 'signIn',
    component: SignInComponent,
  },
  {
    path: 'signUp',
    component: SignUpComponent,
  },
  {
    path: 'chat-bot',
    component: ChatbotComponent,
  },
  {
    path: 'order-food',
    component: OrderFoodComponent,
  },
  {
    path: 'reports',
    component: ReportsComponent,
  },
  {
    path: 'room-list',
    component: RoomListComponent,
  },
  {
    path: 'book-room',
    component: BookRoomComponent,
  },
  {
    path: 'notifications',
    component: NotificationsComponent,
  },
  {
    path: 'tour',
    component: TourPackageComponent,
  },
  {
    path: 'statistics',
    component: VisualizationComponent,
  },
  {
    path: 'feedback',
    component: FeedbackComponent,
  },
  {
    path: 'bill',
    component: BillsComponent,
  },
  {
    path: 'kitchenInventory',
    component: KitchenInventoryComponent,
  },
  {
    path: 'chat-bot-unregistered',
    component: ChatbotUnregisterComponent,

  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [
    RouterModule,
  ],
})
export class AppRoutingModule {
}
