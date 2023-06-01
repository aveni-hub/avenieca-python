import os
from avenieca.config.broker import Broker
from avenieca.data import Signal
from avenieca.producers import Stream
from avenieca.producers import Event
from avenieca.consumer import Consumer


def consume(func, topic):
    config = Broker(
        url=os.environ["KAFKA_URL"],
        sub_topic=topic,
        group="test",
        pub_topic=topic
    )
    client = Consumer(config=config)
    client.consume(func, True)


def test_stream_publish():
    def verify(data):
        valence = data["valence"]
        state = data["state"]
        assert valence == 10.0
        assert state == "[0.2, 0.3, 0.8]"

    def handler():
        signal = Signal(
            valence=10.0,
            state=[0.2, 0.3, 0.8],
        )
        return signal

    config = Broker(
        url=os.environ["KAFKA_URL"],
        sub_topic="test_topic_1",
        group="test",
        pub_topic="test_topic_1"
    )
    stream = Stream(config=config, sync_rate=1)
    stream.publish(handler, True)
    consume(verify, config.sub_topic)


def test_event_publish():
    def verify(data):
        valence = data["valence"]
        state = data["state"]
        assert valence == 9.0
        assert state == "[0.1, 0.2, 0.1]"

    def handler():
        return Signal(
            valence=9.0,
            state=[0.1, 0.2, 0.1],
        )

    config = Broker(
        url=os.environ["KAFKA_URL"],
        sub_topic="test_topic_2",
        group="test",
        pub_topic="test_topic_2"
    )
    event = Event(config=config)
    event.publish(handler())
    consume(verify, config.sub_topic)
