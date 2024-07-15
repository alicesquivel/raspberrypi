#!/usr/bin/env python3

import time
import datetime
import bme680
import paho.mqtt.client as mqtt

# MQTT Broker (Mosquitto) settings
broker_address = "localhost"  # Replace with your MQTT broker address
topic = "sensor/bme680"  # Topic to publish sensor data

def main():
    print("Publishing BME680 sensor data to MQTT broker")

    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    # These oversampling settings can be tweaked to change the balance between accuracy and noise in the data.
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)

    # MQTT setup
    client = mqtt.Client("bme680_publisher")
    client.connect(broker_address)

    print('Polling:')
    try:
        while True:
            if sensor.get_sensor_data():
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                payload = '{ "timestamp": "%s", "temperature": %.2f, "pressure": %.2f, "humidity": %.3f }' % (
                    timestamp, sensor.data.temperature, sensor.data.pressure, sensor.data.humidity)
                client.publish(topic, payload)
                print(f"Published: {payload}")
            time.sleep(5)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        client.disconnect()
        pass

if __name__ == '__main__':
    main()
