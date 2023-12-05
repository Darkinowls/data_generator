import json

import paho.mqtt.client as mqtt

from home_data import House


class Publisher:
    TOPIC = "tv_house"
    BROKER = "broker.hivemq.com"

    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect(self.BROKER)

    def publish(self, message: dict):
        json_ = json.dumps(message)
        self.client.publish(self.TOPIC, json_)
