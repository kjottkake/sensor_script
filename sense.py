from sense_hat import SenseHat

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
speed = 0.1

while True:
	sense.show_message("Yo waht up asdfasdd", text_colour=red, scroll_speed=speed)

