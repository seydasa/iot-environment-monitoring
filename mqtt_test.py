import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/test"


def on_connect(client, userdata, flags, rc):
    print("MQTT bağlantısı başarılı!")
    print("Connection result:", rc)


client = mqtt.Client()
client.on_connect = on_connect

client.connect(BROKER, PORT, 60)

client.loop_forever()