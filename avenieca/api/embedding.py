import requests

from avenieca.api.client import Client
from avenieca.api.model import EmbeddingInputHash, EmbeddingInputInsert, EmbeddingInputResponse, Error


class Embedding:
    """
    Make calls to the /embedding endpoint.
    """

    def __init__(self, config):
        self.client = Client(config)

    def create(self, data: EmbeddingInputInsert):
        """
        Create a new embedding input.

        param data: EmbeddingInputInsert
        """
        response, status = self.client.http_post("/embedding", None, data.__dict__)
        if status != requests.codes['created']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return EmbeddingInputResponse(**response), status

    def get_all(self, module_id):
        """
        Get all Embedding Inputs.
        """
        response, status = self.client.http_get("/embedding/%s" % module_id, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        emb_inp_list = []
        if not response:
            return response, status
        for emb_inp in response:
            emb_inp_response = EmbeddingInputResponse(**emb_inp)
            emb_inp_list.append(emb_inp_response)
        return emb_inp_list, status

    def get_one(self, module_id, db_id):
        """
        Get an Embedding Input using the DB ID.
        """
        response, status = self.client.http_get("/embedding/%s/%s" % (module_id, db_id), None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return EmbeddingInputResponse(**response), status

    def get_one_with_hash(self, module_id, data: EmbeddingInputHash):
        """
        Get an Embedding Input using the hash.
        """
        response, status = self.client.http_get("/embedding/%s/hash" % module_id, None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return EmbeddingInputResponse(**response), status

    def update(self, module_id, db_id, data: EmbeddingInputInsert):
        """
        Update an Embedding Input.

        :param module_id:
        :param db_id:
        :param data: DocumentInsert
        """
        response, status = self.client.http_patch("/embedding/%s/%s" % (module_id, db_id), None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return EmbeddingInputResponse(**response), status

    def delete(self, module_id, db_id):
        """
        delete an Embedding Input.
        """
        response, status = self.client.http_delete("/embedding/%s/%s" % (module_id, db_id), None, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return response, status
