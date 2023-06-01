import requests

from avenieca.api.client import Client
from avenieca.api.model import Config, ESSInsert, ESSResponse, Error, AggregateError, Search, PrettyESS, SearchResult


class ESS:
    """
    Make calls to the /ess endpoint.
    """

    def __init__(self, config: Config):
        self.client = Client(config)

    def create(self, data: ESSInsert):
        """
        Create a new ESS.

        :param data: ESSInsert
        """
        response, status = self.client.http_post("/ess", None, data.__dict__)
        if status != requests.codes['created']:
            try:
                return AggregateError(**response), status
            except TypeError:
                try:
                    return Error(**response), status
                except TypeError:
                    return response, status
        return ESSResponse(**response), status

    def get_all(self, module_id):
        """
        Get all ESS.
        """
        response, status = self.client.http_get("/ess/%s" % module_id, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        ess = []
        if not response:
            return response, status
        for agg in response:
            ess_response = ESSResponse(**agg)
            ess.append(ess_response)
        return ess, status

    def get_all_aggregates(self, module_id, aggregate_module_id, ess_id):
        """
        Get all Aggregates that have the given ESS as an in-twin.
        """
        response, status = self.client.http_get(
            "/ess/%s/aggregate/%s/%s" % (module_id, aggregate_module_id, ess_id),
            None
        )
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        ess = []
        if not response:
            return response, status
        for agg in response:
            ess_response = ESSResponse(**agg)
            ess.append(ess_response)
        return ess, status

    def get_all_sequence(self, module_id):
        """
        Get all ESS from all Sequence.
        This endpoint provides a means to get all the
        ESS referenced by all Sequences ordered
        in descending order from the most recent sequence.
        """
        response, status = self.client.http_get("/ess/%s/sequence" % module_id, None)
        if status != requests.codes['ok']:
            return Error(**response), status
        ess = []
        if not response:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        for e in response:
            ess_response = ESSResponse(**e)
            ess.append(ess_response)
        return ess, status

    def get_one(self, module_id, db_id):
        """
        Get an ESS using the DB ID.
        """
        response, status = self.client.http_get("/ess/%s/%s" % (module_id, db_id), None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return ESSResponse(**response), status

    def get_one_with_embedding(self, module_id, emb_input):
        """
        Get an ESS using the Embedding Input ID.
        """
        response, status = self.client.http_get("/ess/%s/embedding/%s" % (module_id, emb_input), None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return ESSResponse(**response), status

    def get_one_pretty(self, module_id, db_id):
        """
        Get an ESS (using the DB ID) with the state mapped
        to a vector of the original input.
        """
        response, status = self.client.http_get("/ess/%s/pretty/%s" % (module_id, db_id), None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return PrettyESS(**response), status

    def get_one_sequence(self, module_id, sequence_id):
        """
        Get the reference ESS for the Sequence
        at the given database id.
        """
        response, status = self.client.http_get("/ess/%s/sequence/%s" % (module_id, sequence_id), None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return ESSResponse(**response), status

    def update(self, module_id, db_id, data: ESSInsert):
        """
        Update an ESS.

        :param db_id: database id
        :param module_id: module id
        :param data: ESSInsert
        """
        response, status = self.client.http_patch("/ess/%s/%s" % (module_id, db_id), None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return AggregateError(**response), status
            except TypeError:
                try:
                    return Error(**response), status
                except TypeError:
                    return response, status
        return ESSResponse(**response), status

    def search(self, data: Search):
        """
        Search for ess with similar state.

        :param data: Search
        """
        response, status = self.client.http_post("/ess/search", None, data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        search_results = []
        if not response:
            return response, status
        for vsr in response:
            search_result = SearchResult.from_dict(vsr)
            search_results.append(search_result)
        return search_results, status

    def upsert(self, module_id, db_id):
        """
        Upsert an ESS to the VSE Collection
        """
        response, status = self.client.http_put("/ess/%s/upsert/%s" % (module_id, db_id), None, None)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        return response, status
