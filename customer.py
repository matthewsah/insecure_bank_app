import re
from typing import final

pattern = r'[_\-\.0-9a-z]'

@final
class Customer:
    def __init__(self, username: str, accounts: tuple):
        if username == None or not re.match(pattern, username):
            raise ValueError("username cannot be null")
        self.username = username
        self.accounts = accounts
