import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CognitoService } from '../cognito.service';
import { TourPackage } from './tour-package.model';

@Component({
  selector: 'app-tour-package',
  templateUrl: './tour-package.component.html',
  styleUrls: ['./tour-package.component.scss']
})
export class TourPackageComponent implements OnInit {
  adults!: number
  child!: number
  stayDuration!: number
  tourPackages = [
    {
      Name: 'Package 1',
      TourHours: '3 hr',
      TourType: 'cityTour',
      Details: "This tour includes the water bottle only you need to pay for activities."
    },
    {
      Name: 'Package 2',
      TourHours: '5 hr',
      TourType: 'cityTour, Palace',
      Details: "This tour includes the water bottle and entrance ticket to the palace, only you need to pay for activities."
    },
    {
      Name: 'Package 3',
      TourHours: '8 hr',
      TourType: 'cityTour, External Sight seeing',
      Details: "This tour includes the water bottle, snacks for the meal,ticket to the museum, only you need to pay for activities."
    },
    {
      Name: 'Package 4',
      TourHours: '12 hr',
      TourType: 'explore the tariling',
      Details: "This tour includes the water bottle ,snacks for the meal,entrance to the parks, only you need to pay for snow activities."
    }
  ]

  tourPackage = new TourPackage()
  generatedPackage: any;
  showPackage: boolean = false;

  constructor(private cognitoService: CognitoService, private cd: ChangeDetectorRef, private router: Router) { }

  ngOnInit(): void {
  }

  checkTourPackage() {
    this.cognitoService.generateTourPackage(this.adults.toString(), this.child.toString(), this.stayDuration.toString()).then((res) => {
      this.generatedPackage = res
      alert("Package generated successfully!!!")
      this.showPackage = true
    })
  }

  bookTour() {
    this.cognitoService.storeUserPackage(this.generatedPackage.PackageName).then((res) => {
      this.cognitoService.getRoomNotification().then((res) => {
        alert("Your tour is booked successfully!!")
        this.showPackage = false
        this.tourPackage = new TourPackage()
        this.router.navigate(['/home'])
      })
    })
  }

  backToPackageSelection() {
    this.showPackage = false
    this.tourPackage = new TourPackage()
    this.cd.detectChanges()
  }
}
