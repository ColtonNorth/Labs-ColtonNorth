from sense_hat import SenseHat
from random import randint
from time import sleep

#This program causes random colours to appear on random places in the sense hat LED Matrix.
s = SenseHat()
s.low_light = True
counter = 0
s.clear()

while counter < 3:

  s.set_pixel(0,0,143,200,65)
  s.set_pixel(0,7,143,200,65)
  s.set_pixel(7,0,143,200,65)
  s.set_pixel(7,7,143,200,65)
  
  counter += 1
  sleep(.5)
