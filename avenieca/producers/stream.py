import time

from avenieca.config.broker import Broker

from avenieca.producer import Producer
from avenieca.utils.signal import verify_signal


class Stream(Producer):
    """
    Stream producer class for continuous syncing at a sync_rate. Use this class if you want the
    library to handle the syncing logic for you. Provide a handler that returns the signal
    data for publishing.

    :param config: config dictionary
    :param sync_rate: float (time unit in seconds or sub-seconds)
    """

    def __init__(self, config: Broker, sync_rate: float):
        super().__init__(config)
        self.config = config
        self.sync_rate = sync_rate
        self.sync = True

    def publish(self, func, handler_params=None, sync_once=False):
        """
        Basic publish stream timed by the sync_rate

        :param func: handler to return the Signal dataclass for publishing
        :param handler_params: optional tuple of params to pass to the provided handler.
        :param sync_once: run the sync loop once
        :return: none
        """
        while self.sync:
            if handler_params is None:
                signal = func()
            else:
                signal = func(handler_params)
            verify_signal(signal)
            self.send(signal)
            if sync_once:
                break
            time.sleep(self.sync_rate)

    @property
    def config(self):
        return self.config

    @config.setter
    def config(self, value):
        self._config = value
