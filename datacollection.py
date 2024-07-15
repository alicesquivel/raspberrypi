import smbus2
import bme280  # Install with: pip3 install RPi.bme280
import time

# Raspberry Pi I2C bus (depends on the Raspberry Pi version)
# 0 for older versions (256MB, 512MB, 1GB RAM),
# 1 for newer versions (2GB, 4GB, 8GB RAM)
I2C_BUS = 1

# BME280 address
BME280_I2C_ADDR = 0x77

# Open the I2C bus
bus = smbus2.SMBus(I2C_BUS)

# Load calibration data
calibration_params = bme280.load_calibration_params(bus, BME280_I2C_ADDR)

def read_bme280_data():
    # Read raw sensor data
    raw_data = bme280.sample(bus, BME280_I2C_ADDR, calibration_params)

    # Extract temperature, pressure, and humidity
    temperature = raw_data.temperature
    pressure = raw_data.pressure
    humidity = raw_data.humidity

    return temperature, pressure, humidity

try:
    while True:
        temperature, pressure, humidity = read_bme280_data()
        print(f"Temperature: {temperature:.2f} °C, Pressure: {pressure:.2f} >
        time.sleep(1)  # Delay for 1 second
except KeyboardInterrupt:
    pass
finally:
    bus.close()
