import requests

from avenieca.api import auth, ess, sequence, cortex, document, retrieval, ecaresponse, embedding
from avenieca.api.model import AuthLogin, AuthResponse, Config


class ECA:
    """
    Initialize the ECA Object. Performs a login to retrieve API token.
    Provides access to all APIs and some utility methods.
    """

    def __init__(self, config: Config):
        if config.api_token == "":
            self.auth = auth.Auth(config)
            auth_login = AuthLogin(username=config.username, password=config.password)
            response, status = self.auth.login(auth_login)
            if status != requests.codes['ok']:
                raise Exception("login failed: %s", response)
            response: AuthResponse = response
            config.api_token = response.session_id
        self.ess = ess.ESS(config)
        self.sequence = sequence.Sequence(config)
        self.cortex = cortex.Cortex(config)
        self.document = document.Document(config)
        self.retrieval = retrieval.Retrieval(config)
        self.response = ecaresponse.ECAResponse(config)
        self.embedding = embedding.Embedding(config)
