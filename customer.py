from typing import final

@final
class Customer:
    def __init__(self, username: str, password: str, accounts: tuple = ()):
        self.username = username
        self.password = password
        self.accounts = accounts
