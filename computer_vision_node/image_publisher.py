import paho.mqtt.client as mqtt
import numpy as np
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import cv2
from calibrate import calibrate
from yaml_config import loadYAML 

cap = cv2.VideoCapture(1)
ret, frame = cap.read()
transform = calibrate(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), loadYAML('parameters.yml'))

# MQTT Integration Testing
mqttc = mqtt.Client()
mqttc.connect(os.getenv("HOST"), int(os.getenv("PORT")))
mqttc.loop_start()

while True:
    ret, frame = cap.read()
    mqttc.publish('CV_NODE/ENVIRONMENT', np.array2string(cv2.cvtColor(transform(frame), cv2.COLOR_BGR2GRAY)))