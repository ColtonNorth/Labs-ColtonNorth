Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
from sense_hat import SenseHat
from random import randint
from time import sleep

#This program causes random colours to appear on random places in the sense hat LED Matrix.
s = SenseHat()
s.low_light = True
counter = 0
s.clear()

while counter <= 30:
  x = randint(0,7)
  y = randint(0,7)
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)

  s.set_pixel(x,y,r,g,b)
  counter += 1
  sleep(.5)
  