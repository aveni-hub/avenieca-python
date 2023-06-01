import requests

from avenieca.api.client import Client
from avenieca.api.model import RetrievalRequest, RetrievalResponse, Error


class Retrieval:
    """
    Make calls to the /sequence endpoint.
    """

    def __init__(self, config):
        self.client = Client(config)

    def query(self, data: RetrievalRequest):
        """
        Post a retrieval request in natural language.

        :param data: RetrievalRequest
        """
        response, status = self.client.http_post("/retrieval", None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return RetrievalResponse(**response), status
