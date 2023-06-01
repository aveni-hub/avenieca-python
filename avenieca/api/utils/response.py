import requests


def response_helper(e):
    if e == requests.exceptions.HTTPError:
        raise Exception("Http Error: %s" % e)
    if e == requests.exceptions.ConnectionError:
        raise Exception("Error Connecting: %s" % e)
    if e == requests.exceptions.Timeout:
        raise Exception("Timeout Error: %s" % e)
    if e == requests.exceptions.RequestException:
        raise Exception(e)
    else:
        raise Exception(e)
