import re
from typing import final

@final
class Account:
    def __init__(self, account_id, balance, account_type):
        if account_id == None:
            raise ValueError("invalid accound id")
        if balance == None or not (balance >= 0 and re.match(r'(0|[1-9][0-9]*)', str(balance))):
            raise ValueError('invalid balance')
        self.account_id = account_id
        self.balance = balance
        
        self.account_type = account_type
