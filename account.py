import re
from typing import final

@final
class Account:
    def __init__(self, account_id, account_name, balance, account_type):
        if not account_id:
            raise ValueError("invalid accound id")
        if balance == None or not (balance >= 0 and re.match(r'(0|[1-9][0-9]*)', str(balance))):
            raise ValueError('invalid balance')
        if not account_type:
            raise ValueError("invalid account type")
        if not account_name:
            raise ValueError("invalid account name")
        self._account_id = account_id
        self.account_name = account_name
        self.balance = balance
        self.account_type = account_type
    