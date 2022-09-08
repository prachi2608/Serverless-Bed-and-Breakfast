import { Component, OnInit, TemplateRef } from '@angular/core';
import { ToastService } from '../toast-service';
@Component({
  selector: 'app-toast-global',
  templateUrl: './toast-global.component.html',
  styleUrls: ['./toast-global.component.scss'],
  host: { '[class.ngb-toasts]': 'true' }
})
export class ToastGlobalComponent implements OnInit {

  constructor(public toastService: ToastService) { }

  ngOnInit(): void {
  }
  isTemplate(toast: any) { return toast.textOrTpl instanceof TemplateRef; }
  showStandard(message: string) {
    this.toastService.show(message);
  }

  showSuccess(message: string) {
    this.toastService.show(message, { classname: 'bg-success text-light', delay: 10000 });
  }

  showWarning(message: string) {
    this.toastService.show(message, { classname: 'bg-warning text-light', delay: 10000 });
  }

  showInfo(message: string) {
    this.toastService.show(message, { classname: 'bg-info text-light', delay: 10000 });
  }

  showDanger(dangerTpl: string) {
    this.toastService.show(dangerTpl, { classname: 'bg-danger text-light', delay: 15000 });
  }

}
