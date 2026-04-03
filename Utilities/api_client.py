import requests


class APIClient:
    """ Reusable API client for sending HTTP request. """

    def get(self, url, params=None):
        return requests.get(url, params=params)

    def post(self, url, payload, is_json=True):
        if is_json:
          return requests.post(url, json=payload)
        return requests.post(url, data=payload)

    def put(self, url, payload, is_json=True):
        if is_json:
            return requests.put(url, json=payload)
        return requests.put(url, data=payload)

    def delete(self, url, payload=None, is_json=True):
        if is_json:
            return requests.delete(url, json=payload)
        return requests.delete(url, data=payload)
