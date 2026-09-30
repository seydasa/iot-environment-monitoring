import csv
import matplotlib.pyplot as plt
from datetime import datetime

timestamps = []
temperatures = []
humidities = []

with open("sensor_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        timestamps.append(
            datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S")
        )
        temperatures.append(float(row["temperature"]))
        humidities.append(float(row["humidity"]))

plt.figure()
plt.plot(timestamps, temperatures)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(timestamps, humidities)
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.title("Humidity Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()