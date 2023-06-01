import json

from avenieca.config.broker import Broker
from kafka import KafkaProducer


class Producer:
    """
    Base producer for publishing messages.

    :param config: configuration dictionary
    """
    def __init__(self,
                 config: Broker,
                 ):
        self.config = config
        self.topic = config.sub_topic
        self.client = KafkaProducer(bootstrap_servers=config.url)

    def send(self, data: dict):
        """
        :param data: serialized signal dictionary
        :return: FutureRecordMetadata
        """
        json_object = json.dumps(data).encode("utf-8")
        result = self.client.send(self.topic, json_object)
        return result
