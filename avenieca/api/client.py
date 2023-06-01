import requests
import json

from avenieca.api.model import Config
from avenieca.api.utils.response import response_helper


class Client:
    """
    Initializes a Client Object.
    """

    def __init__(self, config: Config):
        if config.api_token != "":
            self.api_token = config.api_token
            self.headers = {"Authorization": self.get_authorization(),
                            "Content-Type": "application/json; charset=utf-8"}
        else:
            self.headers = {"Content-Type": "application/json; charset=utf-8"}

        if config.uri == "":
            raise Exception("ECA URI not set")
        else:
            self.base_uri = config.uri

    def http_get(self, path, query, data=None):
        try:
            response = requests.get(self.build_path(path), headers=self.headers, params=query, data=json.dumps(data))
            try:
                res = response.json()
                return res, response.status_code
            except:
                return response, response.status_code
        except BaseException as e:
            response_helper(e)

    def http_post(self, path, query, data):
        try:
            response = requests.post(self.build_path(path), data=json.dumps(data), headers=self.headers, params=query)
            try:
                res = response.json()
                return res, response.status_code
            except:
                return response, response.status_code
        except BaseException as e:
            response_helper(e)

    def http_patch(self, path, query, data):
        try:
            response = requests.patch(self.build_path(path), data=json.dumps(data), headers=self.headers, params=query)
            try:
                res = response.json()
                return res, response.status_code
            except:
                return response, response.status_code
        except BaseException as e:
            response_helper(e)

    def http_put(self, path, query, data):
        try:
            response = requests.put(self.build_path(path), data=json.dumps(data), headers=self.headers, params=query)
            try:
                res = response.json()
                return res, response.status_code
            except:
                return response, response.status_code
        except BaseException as e:
            response_helper(e)

    def http_delete(self, path, query, data):
        try:
            response = requests.delete(self.build_path(path), data=json.dumps(data), headers=self.headers, params=query)
            try:
                res = response.json()
                return res, response.status_code
            except:
                return response, response.status_code
        except BaseException as e:
            response_helper(e)

    def get_base_url(self):
        return self.base_uri

    def get_authorization(self):
        return "Bearer %s" % self.api_token

    def build_path(self, path):
        return "%s%s" % (self.base_uri, path)
