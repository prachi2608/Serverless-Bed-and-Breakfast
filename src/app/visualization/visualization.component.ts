import { Component, OnInit } from '@angular/core';
import { CognitoService } from '../cognito.service';

@Component({
  selector: 'app-visualization',
  templateUrl: './visualization.component.html',
  styleUrls: ['./visualization.component.scss']
})
export class VisualizationComponent implements OnInit {

  constructor(private cognitoService: CognitoService) { }

  ngOnInit(): void {
    this.cognitoService.visual1().then((res) => {
    })
  }

}
