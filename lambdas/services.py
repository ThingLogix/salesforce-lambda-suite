import requests


class ForceApi:

    def __init__(self, client_id, client_secret, sandbox=False):
        """
        :param sandbox: true if in sandbox environment
        """
        self.env = 'login'
        if sandbox:
            self.env = 'test'
        self.client_id = client_id
        self.client_secret = client_secret

    def refresh_access_token(self, refresh_token):
        body = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }

        return requests.post('https://' + self.env + '.salesforce.com/services/oauth2/token', body).json()

    def get_access_token(self, username, password):
        body = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'password',
            'username': username,
            'password': password
        }

        return requests.post('https://' + self.env + '.salesforce.com/services/oauth2/token', body).json()


