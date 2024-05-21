import re
from typing import final

# pattern = r'[a-z0-9]'

@final
class Customer:
    def __init__(self, username: str, accounts: tuple = ()):
        if username == None:
            raise ValueError("username cannot be null")
        self.username = username
        self.accounts = accounts
