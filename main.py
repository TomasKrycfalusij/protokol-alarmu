
def on_logo_event_longpressed():
    pass
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_event_longpressed)

def on_logo_event_pressed():
    pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)



def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_number(ReceivedNumber):
    if ReceivedNumber == 1:
        music.play_tone(Note.B, 5000)
        basic.show_icon(IconNames.HEART)
radio.on_received_number(on_received_number)


