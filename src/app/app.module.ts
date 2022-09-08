import { ApplicationRef, ChangeDetectorRef, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, NG_VALUE_ACCESSOR } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProfileComponent } from './profile/profile.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
import { BookRoomComponent } from './book-room/book-room.component';
import { OrderFoodComponent } from './order-food/order-food.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { IntercepterService } from './http-interceptor';
import { ReportsComponent } from './reports/reports.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { TourPackageComponent } from './tour-package/tour-package.component';
import { ChatbotUnregisterComponent } from './chatbot-unregister/chatbot-unregister.component';
import { RoomListComponent } from './room-list/room-list.component';
import { NotificationsComponent } from './notifications/notifications.component';
import { ToastGlobalComponent } from './toast-global/toast-global.component';
import { VisualizationComponent } from './visualization/visualization.component';
import { FeedbackComponent } from './feedback/feedback.component';
import { BillsComponent } from './bills/bills.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { KitchenInventoryComponent } from './kitchen-inventory/kitchen-inventory.component';

@NgModule({
  declarations: [
    AppComponent,
    ProfileComponent,
    SignInComponent,
    SignUpComponent,
    ChatbotComponent,
    BookRoomComponent,
    OrderFoodComponent,
    ReportsComponent,
    TourPackageComponent,
    ChatbotUnregisterComponent,
    RoomListComponent,
    NotificationsComponent,
    ToastGlobalComponent,
    VisualizationComponent,
    FeedbackComponent,
    BillsComponent,
    LandingPageComponent,
    KitchenInventoryComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: IntercepterService,
      multi: true
    }
  ],
  bootstrap: [
    AppComponent,
  ],
})
export class AppModule {
}
