import re
class Balance:
    def __init__(self, amount: float):
        if amount == None or not re.match(r'(0|[1-9][0-9]*)(\.\d{1,2})?', str(amount)) or amount < 0:
            raise ValueError('Invalid balance amount.')
        self.amount = amount
