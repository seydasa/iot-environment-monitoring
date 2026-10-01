# IoT Environment Monitoring

A simple IoT environment monitoring project developed to simulate, collect, transmit, store and visualize temperature and humidity data.

## Project Overview

This project is being developed as a learning and development project for IoT systems.

The project currently includes:

- Temperature and humidity data simulation
- Realistic sensor value changes
- Timestamped data logging
- MQTT-based communication
- Mosquitto MQTT broker
- MQTT publisher and subscriber
- CSV data storage
- Temperature and humidity visualization
- Git and GitHub version control

## System Architecture

```text
Sensor Simulator
       |
       | MQTT Publish
       v
Mosquitto MQTT Broker
       |
       | MQTT Subscribe
       v
MQTT Subscriber
       |
       v
sensor_data.csv
       |
       v
Data Visualization

Project Structure
iot-environment-monitoring/
│
├── sensor_simulator.py
├── mqtt_publisher.py
├── mqtt_subscriber.py
├── mqtt_test.py
├── plot_sensor_data.py
├── sensor_data.csv
├── requirements.txt
├── .gitignore
└── README.md
MQTT Configuration

The project uses the local Mosquitto MQTT broker.

Broker: localhost
Port: 1883
Topic: iot/sensors

The sensor simulator generates temperature and humidity data and publishes these values to the MQTT topic. The MQTT subscriber receives the data and stores it in sensor_data.csv.

Data Flow
Sensor Simulation
       ↓
MQTT Publish
       ↓
Mosquitto Broker
       ↓
MQTT Subscriber
       ↓
CSV Data Storage
       ↓
Data Visualization
Current Status

The MQTT communication layer has been successfully implemented and tested.

The sensor simulator generates realistic temperature and humidity values every two seconds. These values are published through MQTT, received by the subscriber, and stored in sensor_data.csv.

Future Development

Planned improvements include:

Connecting a real IoT sensor or ESP32 device
Database integration
Real-time data visualization
Web-based monitoring dashboard
Sensor and device management
Additional environmental parameters