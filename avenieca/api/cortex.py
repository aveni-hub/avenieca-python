import requests

from avenieca.api.client import Client
from avenieca.api.model import NextStateRequest, NextStateResponse, NextStateResponseRaw, Error


class Cortex:
    """
    Make calls to the /predictions endpoint.
    """

    def __init__(self, config):
        self.client = Client(config)

    def predictions(self, data: NextStateRequest):
        """
        Given the current Twin, predict the next n states
        and get the response mapped back to the embedding input, if defined.

        :param data: NextStateRequest
        """
        response, status = self.client.http_post("/predictions", None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return NextStateResponse.from_dict(response), status

    def predictions_raw(self, data: NextStateRequest):
        """
        Given the current Twin, predict the next n states
        and get the response as raw Aggregate values.

        :param data: NextStateRequest
        """
        response, status = self.client.http_post("/predictions/raw", None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return NextStateResponseRaw.from_dict(response), status
