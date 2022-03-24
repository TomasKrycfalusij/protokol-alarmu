let learn = 0
let alarm = 0
let neighbours = []
let send = 0
let cislo = []
radio.setTransmitSerialNumber(false)
// MANUÁL
//  1. Dlouhý stisk loga pro vypnutí nebo zapnutí LEARN módu
//  2. Krátký stisk loga pro zapnutí nebo vypnutí SEND módu
//  3. Stisknutí tlačítka A pro zapnutí alarmu
//  4. Stisknutí tlačítka B pro vypnutí alarmu
// ZAPNUTÍ/VYPNUTÍ ODESÍLACÍHO MÓDU
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_event_longpressed() {
    
    if (send == 0) {
        send = 1
    } else {
        send = 0
    }
    
    console.log("Am I sending?")
    console.log(send)
})
// ZAPNUTÍ LEARN MÓDU
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    if (learn == 0) {
        learn = 1
    } else {
        learn = 0
    }
    
    console.log("Am I learning?")
    console.log(learn)
})
// ZAPNUTÍ ALARMU
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendValue("ahoj", 1)
})
// VYPNUTÍ ALARMU
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
})
// PŘIJMUTÍ SIGNÁLU
radio.onReceivedValue(function data_received(name: string, value: number) {
    console.log(value)
    let remote_serial = radio.receivedPacket(RadioPacketProperty.SerialNumber)
    console.log(remote_serial)
})
