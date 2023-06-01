import requests

from avenieca.api.client import Client
from avenieca.api.model import ECAResponse as Res, Error


class ECAResponse:
    """
    Make calls to the /response endpoint.
    """

    def __init__(self, config):
        self.client = Client(config)

    def get_all(self):
        """
        Get all responses.
        """
        response, status = self.client.http_get("/response", None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        response_list = []
        if not response:
            return response, status
        for res in response:
            ess_response = Res(**res)
            response_list.append(ess_response)
        return response_list, status

    def get_one(self, db_id):
        """
        Get a response using the DB ID.
        """
        response, status = self.client.http_get("/response/%s" % db_id, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return Res(**response), status
