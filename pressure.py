#!/usr/bin/env python3

import time
import bme680
import paho.mqtt.client as mqtt
import json

# MQTT broker details
MQTT_BROKER = "YOUR_MQTT_BROKER_IP"
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/pressure"

def main():
    print("Reading BME680 sensor data")

    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    # Set oversampling settings for the pressure sensor
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_filter(bme680.FILTER_SIZE_3)

    print('Polling:')

    # Set up MQTT client
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    try:
        while True:
            if sensor.get_sensor_data():
                pressure_data = {
                    "pressure": sensor.data.pressure
                }
                client.publish(MQTT_TOPIC, json.dumps(pressure_data))
                print(f"Published pressure: {sensor.data.pressure:.2f} hPa")
            time.sleep(1)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()

if __name__ == '__main__':
    main()
