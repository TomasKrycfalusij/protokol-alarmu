learn = 0
alarm = 0
neighbours = []
send = 0
cislo = []
radio.set_transmit_serial_number(False)

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
    radio.send_value("alarm", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

#VYPNUTÍ ALARMU
def on_button_pressed_b():
    radio.send_value("alarm", 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

#PŘIJMUTÍ SIGNÁLU
def data_received(name, value):
    if name == "alarm" and value == 1:
        basic.show_number(1)
        basic.pause(200)
        basic.clear_screen()
    if name == "alarm" and value == 0:
        basic.show_number(0)
        basic.pause(200)
        basic.clear_screen()
radio.on_received_value(data_received)

#remote_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)