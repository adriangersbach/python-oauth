import requests

class OAuthInterface:
    def __init__(self, base_url, api_key, api_secret, username, password):
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.username = username
        self.password = password
        self.access_token = ""
        self.token_type = ""
        self.expires_in = 0
        self.refresh_token = ""

    def reset(self):
        self.access_token = ""
        self.token_type = ""
        self.expires_in = 0
        self.refresh_token = ""

    def request_access_token(self):
        final_url = "https://{0}/oauth/token".format(self.base_url)
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'client_id': self.api_key, 'client_secret': self.api_secret, 'grant_type': 'password',
                'username': self.username, 'password': self.password}
        response = requests.post(final_url, headers=headers, data=data)
        print(response.url)
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            print(json)
            self.access_token = json['access_token']
            self.token_type = ""
            self.expires_in = 0
            self.refresh_token = json['refresh_token']
        else:
            self.reset()

    def refresh_access_token(self, refresh_token):
        final_url = "https://{0}/oauth/token".format(self.base_url)
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'client_id': self.api_key, 'client_secret': self.api_secret, 'grant_type': 'refresh_token',
                'refresh_token': refresh_token}
        response = requests.post(final_url, headers=headers, data=data)
        print(response.url)
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            print(json)
            self.access_token = json['access_token']
            self.token_type = ""
            self.expires_in = 0
            self.refresh_token = json['refresh_token']
        else:
            self.reset()

    def revoke_access_token(self, access_token):
        final_url = "https://{0}/oauth/revoke".format(self.base_url)
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'client_id': self.api_key, 'client_secret': self.api_secret, 'token': access_token}
        return requests.post(final_url, headers=headers, data=data)
