from gpiozero import LED, Button, Device
# from esp32tool import
from signal import pause

print("Before any device: pin factory →", Device.pin_factory)  # This will be None

status_led = LED(17)          # ← Here the factory loads!
test_button = Button(27)

print("After creating devices: pin factory →", Device.pin_factory)  # Now shows <LGPIOFactory ...> or similar

def on_button_pressed():
    status_led.on()
    print("Button PRESSED → Test stimulus ACTIVE")

def on_button_released():
    status_led.off()
    print("Button RELEASED → Test stimulus OFF")

test_button.when_pressed = on_button_pressed
test_button.when_released = on_button_released

print("Digital IO test running... Press the button on GPIO27!")
pause()