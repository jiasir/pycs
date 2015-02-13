__author__ = 'Taio'

import os

CS_ACCESS_KEY = os.environ.get('CS_ACCESS_KEY')
CS_SECURITY_KEY = os.environ.get('CS_SECURITY_KEY')


class Keys():
    def __init__(self):
        # Define your CS_ACCESS_KEY and CS_SECURITY_KEY env.
        self.access_key = CS_ACCESS_KEY
        self.security_key = CS_SECURITY_KEY

    def get_access_key(self):
        return self.access_key
    
    def get_security_key(self):
        return self.security_key