Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sense_hat import SenseHat
import time, sense_hat


s = SenseHat()
sense = sense_hat.SenseHat()
s.low_light = True

red = (255, 0, 0)
nothing = (0,0,0)


def Colton():
    R = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, R, R, R, R, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, R, R, R, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def North():
    R = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, O, R, O,
    O, R, O, R, O, O, R, O,
    O, R, O, O, R, O, R, O,
    O, R, O, O, O, R, R, O,
    O, R, O, O, O, O, R, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
images = [Colton, North]
s.set_pixels(images[0]())
count = 1

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
            s.set_pixels(images[count % len(images)]())
            count += 1