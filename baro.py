import math
import json
import datetime
from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
pressure = sense.get_pressure()

def calculate_altitude(pressure, sea_level_pressure=1013.25):
    # Constants
    molar_mass_air = 0.029  # kg/mol
    gravitational_acceleration = 9.81  # m/s^2
    universal_gas_constant = 8.314  # J/(mol*K)

    kentucky_modifier = 81
    # Calculate temperature in Kelvin (you'll need to provide this)
    temperature_in_celsius = temp  # Replace with the actual temperature in Celsius
    temperature_in_kelvin = temperature_in_celsius + 273.15

    # Calculate altitude using the barometric formula
    altitude = ((-universal_gas_constant * temperature_in_kelvin) / 
                (molar_mass_air * gravitational_acceleration) * 
                math.log(pressure / sea_level_pressure)) - kentucky_modifier

    return altitude

# Example usage
sea_level_pressure = 1013.25  # Standard sea level pressure in hPa or millibars
measured_pressure = pressure  # Replace with the measured atmospheric pressure in hPa or millibars

altitude = calculate_altitude(measured_pressure, sea_level_pressure)
print(f"Altitude: {altitude} meters")


