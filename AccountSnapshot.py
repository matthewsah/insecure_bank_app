from typing import final

@final
class AccountSnapshot:
    def __init__(self, account_id, balance, account_type):
        self.account_id = account_id
        self.balance = balance
        self.account_type = account_type
