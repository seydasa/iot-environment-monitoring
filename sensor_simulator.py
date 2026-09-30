import random
import time
import csv
from datetime import datetime
import paho.mqtt.client as mqtt

# MQTT ayarları
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensors"

# MQTT bağlantısı
client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

temperature = 24.0
humidity = 45.0

target_temperature = 24.0
target_humidity = 45.0

with open("sensor_data.csv", "a", newline="") as file:
    writer = csv.writer(file)

    # CSV dosyası boşsa başlıkları ekle
    if file.tell() == 0:
        writer.writerow(["timestamp", "temperature", "humidity"])

    while True:

        # Hedef değerleri küçük miktarlarda değiştir
        target_temperature += random.uniform(-0.1, 0.1)
        target_humidity += random.uniform(-0.3, 0.3)

        # Hedeflerin gerçekçi sınırlar içinde kalmasını sağla
        target_temperature = max(18, min(30, target_temperature))
        target_humidity = max(30, min(70, target_humidity))

        # Ölçümü hedefe doğru küçük bir adımla yaklaştır
        temperature += (target_temperature - temperature) * 0.1
        humidity += (target_humidity - humidity) * 0.1

        # Ölçüm zamanını al
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Değerleri yuvarla
        temperature_value = round(temperature, 2)
        humidity_value = round(humidity, 2)

        # Terminale yazdır
        print(
            timestamp,
            "| Temperature:", temperature_value, "°C",
            "| Humidity:", humidity_value, "%"
        )

        # CSV dosyasına kaydet
        writer.writerow([
            timestamp,
            temperature_value,
            humidity_value
        ])

        # Dosyaya hemen yaz
        file.flush()

        # MQTT mesajı oluştur
        message = (
            f'{{"timestamp": "{timestamp}", '
            f'"temperature": {temperature_value}, '
            f'"humidity": {humidity_value}}}'
        )

        # MQTT üzerinden gönder
        client.publish(TOPIC, message)

        # 2 saniye bekle
        time.sleep(2)