from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


humid = sense.get_humidity()
temp = sense.get_temperature_from_humidity()
press = sense.get_pressure()


print(f"humidity: {humid}")
print(f"temperature: {temp}")
print(f"pressure: {press}")
