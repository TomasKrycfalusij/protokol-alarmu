learn = 0
alarm = 0
neighbours = []
send = 0

def on_forever():
    remote_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
    print(remote_serial)
    basic.pause(1000)
forever(on_forever)


#MANUÁL
# 1. Dlouhý stisk loga pro vypnutí nebo zapnutí LEARN módu
# 2. Krátký stisk loga pro zapnutí nebo vypnutí SEND módu
# 3. Stisknutí tlačítka A pro zapnutí alarmu
# 4. Stisknutí tlačítka B pro vypnutí alarmu

#ZAPNUTÍ/VYPNUTÍ ODESÍLACÍHO MÓDU
def on_logo_event_longpressed():
    global send
    if send == 0:
        send = 1
    else:
        send = 0
    print("Am I sending?")
    print(send)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_event_longpressed)

#ZAPNUTÍ LEARN MÓDU
def on_logo_event_pressed():
    global learn
    if learn == 0:
        learn = 1
    else:
        learn = 0
    print("Am I learning?")
    print(learn)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

#ZAPNUTÍ ALARMU
def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

#VYPNUTÍ ALARMU
def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)