import paho.mqtt.client as mqtt
import json
import csv
import os

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensors"
CSV_FILE = "sensor_data.csv"


def on_connect(client, userdata, flags, rc):
    print("MQTT broker'a bağlandı!")
    print("Connection result:", rc)

    client.subscribe(TOPIC)
    print(f"Dinleniyor: {TOPIC}")


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    print(
        f"Veri geldi → "
        f"{data['timestamp']} | "
        f"Temperature: {data['temperature']} °C | "
        f"Humidity: {data['humidity']} %"
    )

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(CSV_FILE) == 0:
            writer.writerow(["timestamp", "temperature", "humidity"])

        writer.writerow([
            data["timestamp"],
            data["temperature"],
            data["humidity"]
        ])


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_forever()