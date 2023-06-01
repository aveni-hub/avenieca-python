import requests

from avenieca.api.client import Client
from avenieca.api.model import Config
from avenieca.api.model import AuthLogin
from avenieca.api.model import AuthResponse
from avenieca.api.model import Error


class Auth:
    """Initializes an Auth object to make calls to the /login endpoint.

    Parameters
    ----------
    config : dict of config values
    """

    def __init__(self, config: Config):
        self.client = Client(config)

    def login(self, data: AuthLogin):
        """
        login to retrieve api-token.
        Parameters
        ----------
        data = {"username": "","password": ""}
        """
        response, status = self.client.http_post("/login", "", data.__dict__)
        if status != requests.codes['ok']:
            try:
                return Error(**response), status
            except TypeError:
                return response, status
        auth_response = AuthResponse(**response)
        return auth_response, status
