from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

while True:
	num1 = randint(0, 255)
	num2 = randint(0, 255)
	num3 = randint(0, 255)
	color = (num1, num2, num3)
	space1 = randint(0, 7)
	space2 = randint(0, 7)

	sense.set_pixel(space1, space2, color)
	sleep(0.1)
