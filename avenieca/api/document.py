import requests

from avenieca.api.client import Client
from avenieca.api.model import DocumentInsert, DocumentResponse, Error


class Document:
    """
    Make calls to the /document endpoint.
    """

    def __init__(self, config):
        self.client = Client(config)

    def create(self, data: DocumentInsert):
        """
        Create a new document.

        :param data: DocumentInsert
        """
        response, status = self.client.http_post("/document", None, data.__dict__)
        if status != requests.codes['created']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return DocumentResponse(**response), status

    def create_from_ess(self, module_id, ess_id):
        """
        Create a new document from an existing ESS.
        """
        response, status = self.client.http_post("/document/ess/%s/%s" % (module_id, ess_id), None, None)
        if status != requests.codes['created']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return DocumentResponse(**response), status

    def create_from_sequence(self, module_id, sequence_id):
        """
        Create a new document from an existing Sequence.
        """
        response, status = self.client.http_post("/document/sequence/%s/%s" % (module_id, sequence_id), None, None)
        if status != requests.codes['created']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return DocumentResponse(**response), status

    def get_all(self):
        """
        Get all documents.
        """
        response, status = self.client.http_get("/document", None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        document_list = []
        if not response:
            return response, status
        for doc in response:
            doc_response = DocumentResponse(**doc)
            document_list.append(doc_response)
        return document_list, status

    def get_one(self, db_id):
        """
        Get a document using the DB ID.
        """
        response, status = self.client.http_get("/document/%s" % db_id, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return DocumentResponse(**response), status

    def update(self, db_id, data: DocumentInsert):
        """
        Update a document.

        :param db_id:
        :param data: DocumentInsert
        """
        response, status = self.client.http_patch("/document/%s" % db_id, None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return DocumentResponse(**response), status

    def embed(self, db_id):
        """
        Embed an existing document.

        :param db_id:
        """
        response, status = self.client.http_put("/document/embed/%s" % db_id, None, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return DocumentResponse(**response), status

    def delete(self, db_id):
        """
        delete a particular Document.
        """
        response, status = self.client.http_delete("/document/%s" % db_id, None, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return response, status
