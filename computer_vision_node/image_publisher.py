import paho.mqtt.client as mqtt
import numpy as np
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import cv2
from calibrate2 import calibrate
from center_of_shape import get_points
from yaml_config import loadYAML 

cap = cv2.VideoCapture(1)
ret, frame = cap.read()
transform = calibrate(frame)

# MQTT Integration Testing
mqttc = mqtt.Client()
mqttc.connect(os.getenv("HOST"), int(os.getenv("PORT")))
mqttc.loop_start()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    output = transform(frame)

    mqttc.publish('CV_NODE/ENVIRONMENT', np.array2string(get_points(output)))

    # Display the resulting frame
    contours(output)
    cv2.imshow('Live Feed',output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()