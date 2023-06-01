import requests

from avenieca.api.client import Client
from avenieca.api.model import SequenceInsert, SequenceResponse, Error


class Sequence:
    """
    Make calls to the /sequence endpoint.
    """

    def __init__(self, config):
        self.client = Client(config)

    def create(self, data: SequenceInsert):
        """
        Create a new sequence for a twin or aggregate.

        :param data: SequenceInsert
        """
        response, status = self.client.http_post("/sequence", None, data.__dict__)
        if status != requests.codes['created']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return SequenceResponse(**response), status

    def get_all(self, module_id):
        """
        Get all Sequences for a twin or aggregate.
        """
        response, status = self.client.http_get("/sequence/%s" % module_id, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        sequence_list = []
        if not response:
            return response, status
        for seq in response:
            ess_response = SequenceResponse(**seq)
            sequence_list.append(ess_response)
        return sequence_list, status

    def get_one(self, module_id, db_id):
        """
        Get a sequence using the DB ID.
        """
        response, status = self.client.http_get("/sequence/%s/%s" % (module_id, db_id), None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return SequenceResponse(**response), status

    def update(self, module_id, db_id, data: SequenceInsert):
        """
        Update a sequence for a twin or aggregate.

        :param db_id:
        :param module_id:
        :param data: SequenceInsert
        """
        response, status = self.client.http_patch("/sequence/%s/%s" % (module_id, db_id), None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return SequenceResponse(**response), status
