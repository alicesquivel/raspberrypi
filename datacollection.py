#!/usr/bin/env python3

import time
import datetime
import bme680

def main():
    print("Reading BME680 sensor data with timestamps")

    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    # These oversampling settings can be tweaked to change the balance between accuracy and noise in the data.
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)

    print('Polling:')
    try:
        while True:
            if sensor.get_sensor_data():
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                output = '{0} - {1:.2f} C, {2:.2f} hPa, {3:.3f} %RH'.format(timestamp, sensor.data.temperature, sensor.data.pressure, sensor.data.humidity)
                print(output)
            time.sleep(1)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
