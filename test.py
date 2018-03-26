import json
import requests

class GRRClient():

    def __init__(self, username, password, baseurl):
        self.data = {}
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.baseurl = baseurl
        self.session.auth = (self.username, self.password)

        try:
            self.login()
        except requests.HTTPError:
            sys.exit('Username-password invalid')

    def login(self):
        self.session.get(self.baseurl)
        xsrf_token = self.session.cookies.get('csrftoken')
        self.session.headers.update({'x-csrftoken': xsrf_token,
                                     'x-requested-with': 'XMLHttpRequest'})
