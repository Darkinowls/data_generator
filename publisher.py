import json
import os
from datetime import datetime

import paho.mqtt.client as mqtt


class Publisher:
    TOPIC = os.environ.get("TOPIC", "tv_house")
    BROKER = "broker.hivemq.com"

    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect(self.BROKER)

    def publish(self, message: dict):
        message.update({"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        json_ = json.dumps(message)
        self.client.publish(self.TOPIC, json_)
