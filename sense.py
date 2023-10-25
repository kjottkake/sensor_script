from sense_hat import SenseHat

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
speed = 0.04

while True:
	sense.show_message("Mommy do you see this? Send me a message on messenger if you do.", text_colour=red, scroll_speed=speed)

