import { ApplicationRef, ChangeDetectorRef, Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import Amplify, { Auth } from 'aws-amplify';
import { environment } from '../environments/environment';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

export interface IUser {
  email: string;
  password: string;
  showPassword: boolean;
  code: string;
  name: string;
}

@Injectable({
  providedIn: 'root',
})
export class CognitoService {

  private authenticationSubject: BehaviorSubject<any>;

  constructor(private http: HttpClient, private ap: ApplicationRef) {
    Amplify.configure({
      Auth: environment.cognito,
    });

    this.authenticationSubject = new BehaviorSubject<boolean>(false);
  }
  async visual1() {
    return new Promise((resolve, reject) => {
      this.http.get('https://us-central1-csci5410-a3-pb.cloudfunctions.net/food-order').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }
  async getKitchenInventory() {
    return new Promise((resolve, reject) => {
      this.http.get('https://gjcip6henoahncdvsks47impte0zddjy.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }
  async getOrderNotification() {
    return new Promise((resolve, reject) => {
      this.http.get('https://us-central1-csci-5410-352923.cloudfunctions.net/ordercloud').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }
  async getTourNotification() {
    return new Promise((resolve, reject) => {
      this.http.get('https://us-central1-csci-5410-352923.cloudfunctions.net/tourcloud').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }
  async getRoomNotification() {
    return new Promise((resolve, reject) => {
      this.http.get('https://us-central1-csci-5410-352923.cloudfunctions.net/roomcloud').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }
  async getAllNotification() {
    return new Promise((resolve, reject) => {
      this.http.get('https://us-central1-csci-5410-352923.cloudfunctions.net/fetchroomdata').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }
  async getLoggedOutUsers() {
    return new Promise((resolve, reject) => {
      this.http.get('https://2n766wobmmi2iyafmrssw5wvqy0coyfs.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  getVerifiedUsers() {
    return new Promise((resolve, reject) => {
      this.http.get('https://7d3lruuaviobhsn62y7t2owifq0vwshs.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  getUnVerifiedUsers() {
    return new Promise((resolve, reject) => {
      this.http.get('https://cj7bsxhhcn4vbrs3aipwfldeje0axans.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  getEnabledUsers() {
    return new Promise((resolve, reject) => {
      this.http.get('https://msbggfkueh2yai2ut7kiixk5n40pnrtp.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  getDisabledUsers() {
    return new Promise((resolve, reject) => {
      this.http.get('https://q7xibc3gpwcevncwfjya32xwwq0cnokq.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  getRooms() {
    return new Promise((resolve, reject) => {
      this.http.get('https://v5ufcaweepcbujuwuoclhxagjy0gdvwj.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  getFoodItems() {
    return new Promise((resolve, reject) => {
      this.http.get('https://3teq5tb7wfiztxi7lhzulxqmsi0vlfgh.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  getLoggedInUsersItems() {
    return new Promise((resolve, reject) => {
      this.http.get(' https://7wseizhozmrdq6mos2pck6uvle0cdbdr.lambda-url.us-east-1.on.aws/').pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  orderFood(foodItems: {
    "foodItem": string,
    "quantity": string
  }[]) {
    return new Promise((resolve, reject) => {
      this.http.post('https://wefp4ndxcm6oi442nohezihu4a0urekt.lambda-url.us-east-1.on.aws/', {
        "email": sessionStorage.getItem("Email"),
        "foodItems": foodItems
      }).pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  public async signUp(username: any, password: any, answer1: any, answer2: any, answer3: any, key: any): Promise<any> {
    let use1r = await Auth.signUp(username, password)
    return new Promise((resolve, reject) => {
      this.http.post('https://k4f2hm57csxygy7s4manwbiwtu0vgndg.lambda-url.us-east-1.on.aws/', {
        username: username,
        password: password,
        answer1: answer1,
        answer2: answer2,
        answer3: answer3,
        key: key
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(true);
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  public async generateTourPackage(adults: string, child: string, stayDuration: string): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://us-central1-csci-5410-s22-353221.cloudfunctions.net/generateTourPackage', {
        'Adults': adults,
        'Child': child,
        'stayDuration': stayDuration
      }).pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }
  public async storeUserPackage(Package: string): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://us-east1-csci-5410-s22-353221.cloudfunctions.net/storeUserPackage', {
        'userEmail': sessionStorage.getItem("Email"),
        'Package': Package,
        'PackagePrice': "120"
      }).pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }

  public async bookRoom(roomNumber: any, numberOfDays: any, startDate: any, endDate: any): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://k4f2hm57csxygy7s4manwbiwtu0vgndg.lambda-url.us-east-1.on.aws/', {
        roomNumber: roomNumber,
        numberOfDays: numberOfDays,
        startDate: startDate,
        endDate: endDate,
      }).pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  public async getNotification(): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://us-central1-csci-5410-352923.cloudfunctions.net/roombookapinotif', {}).pipe(
        map(res => res))
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  public confirmSignUp(user: IUser): Promise<any> {
    return Auth.confirmSignUp(user.email, user.code);
  }

  async signIn(user: IUser, validationData: any): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://5ch3haxuunvqrkq42wrr424aj40bhbif.lambda-url.us-east-1.on.aws/', {
        "username": user.email,
        "password": user.password
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(true);
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  async addFeedback(service: string, feedback: string): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://us-central1-csci-5410-s22-353221.cloudfunctions.net/extractFeedback', {
        "EmailId": sessionStorage.getItem("Email"),
        "Feedback": feedback,
        "Service": service
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(false);
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }

  async generateBills(): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://i6jwkoyohcscpxtqiffjqn7d2m0vtxof.lambda-url.us-east-1.on.aws/', {
        "email": sessionStorage.getItem("Email")
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(false);
          resolve(res);
        }, (err) => {
          resolve(err);
        });
    });
  }

  async securityVerification(user: IUser, validationData: any): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://frh5fdqbocpf4ykukbna5esgvm0pvawc.lambda-url.us-east-1.on.aws/', {
        "username": user.email,
        "securityQuestionNumber": validationData.securityQuestionNumber,
        "securityAnswer": validationData.securityAnswer
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(false);
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  async cipherVerification(user: IUser, validationData: any): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://us-east1-csci5410-353200.cloudfunctions.net/cipherVerification/', {
        "email": user.email,
        "cipherQuestion": validationData.cipherQuestion,
        "cipherAnswer": validationData.cipherAnswer
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(false);
          resolve(res);
        }, (err) => {
          resolve("Done");
        });
    });
  }


  async storeSession(email: string): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://zf4w52ufr2nnfwwsdjkmhwgeoi0fydav.lambda-url.us-east-1.on.aws/', {
        "username": email
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(false);
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  public async signOut(): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post('https://x3ybpkdpmmhplnxro7pbfzdr440olopo.lambda-url.us-east-1.on.aws/', {
        username: sessionStorage.getItem("Email")
      }).pipe(
        map(res => res))
        .subscribe(res => {
          this.authenticationSubject.next(false);
          sessionStorage.removeItem('Email')
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  public isAuthenticated(): Promise<boolean> {
    if (sessionStorage.getItem('Email')) {
      return Promise.resolve(true);
    } else {
      return Promise.resolve(false);
    }
  }

  public getUser(): Promise<any> {
    return Auth.currentUserInfo();
  }

  public updateUser(user: IUser): Promise<any> {
    return Auth.currentUserPoolUser()
      .then((cognitoUser: any) => {
        return Auth.updateUserAttributes(cognitoUser, user);
      });
  }
}
