import re
from typing import final
from balance import Balance

@final
class Account:
    def __init__(self, account_id: int, account_name: str, balance: Balance, account_type: str):
        if not account_id:
            raise ValueError("invalid accound id")
        if not account_type:
            raise ValueError("invalid account type")
        if not account_name:
            raise ValueError("invalid account name")
        self.account_id = account_id
        self.account_name = account_name
        self.balance = balance
        self.account_type = account_type
