#!/usr/bin/env python3

import time
import datetime
import bme680
import paho.mqtt.client as mqtt

# MQTT Broker (Mosquitto) settings
broker_address = "YOUR_MQTT_BROKER_IP"  # Replace with your MQTT broker address
topic = "sensor/pressure"  # Topic to publish pressure data

def main():
    print("Publishing pressure data to MQTT broker")

    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    # These oversampling settings can be tweaked to change the balance between accuracy and noise in the data.
    sensor.set_pressure_oversample(bme680.OS_4X)

    # MQTT setup
    client = mqtt.Client("pressure_publisher")
    client.connect(broker_address)

    print('Polling:')
    try:
        while True:
            if sensor.get_sensor_data():
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                payload = '{ "timestamp": "%s", "pressure": %.2f }' % (
                    timestamp, sensor.data.pressure)
                client.publish(topic, payload)
                print(f"Published: {payload}")
            time.sleep(5)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        client.disconnect()
        pass

if __name__ == '__main__':
    main()

