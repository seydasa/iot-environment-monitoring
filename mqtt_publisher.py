import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensors"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

while True:
    message = "Merhaba MQTT!"
    client.publish(TOPIC, message)

    print(f"Mesaj gönderildi → {message}")

    time.sleep(2)