input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_event_longpressed() {
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(1)
})
radio.onReceivedNumber(function on_received_number(ReceivedNumber: number) {
    if (ReceivedNumber == 1) {
        basic.showIcon(IconNames.Heart)
    }
    
})
