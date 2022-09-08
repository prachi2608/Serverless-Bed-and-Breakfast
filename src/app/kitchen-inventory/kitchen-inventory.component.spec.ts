import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KitchenInventoryComponent } from './kitchen-inventory.component';

describe('KitchenInventoryComponent', () => {
  let component: KitchenInventoryComponent;
  let fixture: ComponentFixture<KitchenInventoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ KitchenInventoryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KitchenInventoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
