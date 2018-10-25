import paho.mqtt.publish as publish
import os
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

tmp_payload = {"ballID": 8, "pocketID": 3}

publish.single("UI_NODE/COMMANDS", json.dumps(tmp_payload), hostname=os.getenv("HOST"), port=int(os.getenv("PORT")))