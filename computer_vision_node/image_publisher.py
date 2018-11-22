import paho.mqtt.client as mqtt
import numpy as np
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

# Placeholder for environment map of pool table
env = np.zeros((5, 5), np.int8)

# MQTT Integration Testing
mqttc = mqtt.Client()
mqttc.connect(os.getenv("HOST"), int(os.getenv("PORT")))
mqttc.loop_start()

while True:
    mqttc.publish('CV_NODE/ENVIRONMENT', np.array2string(env))
