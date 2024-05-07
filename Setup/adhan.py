import network   # handles connecting to WiFi
import urequests  # handles making and servicing network requests

import time
import ntptime
from picographics import PicoGraphics, DISPLAY_ENVIRO_PLUS
from pimoroni import RGBLED

# Turn off LED
led = RGBLED(6, 7, 10, invert=True)  # setting pins for the RGB led
led.set_rgb(0, 0, 0)

display = PicoGraphics(display=DISPLAY_ENVIRO_PLUS)
WIDTH, HEIGHT = display.get_bounds()
display.set_backlight(1.0)
display.set_font("bitmap8")


BG = display.create_pen(0, 0, 0)
TEXT = display.create_pen(255, 255, 255)

display.set_pen(BG)
display.set_pen(TEXT)


# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

try:
    ssid = 'PHILIP'
    password = 'IRRAGLI1'
    wlan.connect(ssid, password)
    print("Connected to wifi")
except Exception as e:
    print(e)


time.localtime()
ntptime.settime()
time.localtime()


display.text(str(time.localtime()), 10, 10, WIDTH, 3)
display.update()
