import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChatbotUnregisterComponent } from './chatbot-unregister.component';

describe('ChatbotUnregisterComponent', () => {
  let component: ChatbotUnregisterComponent;
  let fixture: ComponentFixture<ChatbotUnregisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChatbotUnregisterComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChatbotUnregisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
