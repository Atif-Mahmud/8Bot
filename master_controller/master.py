import paho.mqtt.client as mqtt
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

class MasterController (mqtt.Client):
    def __init__(self, host=None, port=None):
        self.connect(host or os.getenv("HOST"), port or int(os.getenv("PORT")), 60)

    def run(self):
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self.loop_forever()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code", rc)

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.

        # System Subscription
        #client.subscribe("$SYS/#")

        # Environment Subscription
        client.subscribe("CV_NODE/ENVIRONMENT")

        # UI Subscription
        client.subscribe("UI_NODE/COMMANDS")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        if (msg.topic == "CV_NODE/ENVIRONMENT"):
            print(msg.payload.decode("utf-8"))
        elif (msg.topic == "UI_NODE/COMMANDS"):
            print(msg.payload.decode("utf-8"))
        else:
            print("ERROR: unhandled mqtt topic")

client = MasterController()

client.run()
