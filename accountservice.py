import mariadb
from customer import Customer
from account import Account

config = {
     'user': 'root',
     'password': '',
     'host': '127.0.0.1',
     'port': 3306,
     'database': 'flask_app',
 }

class AccountService:
    def __init__(self):
        pass
    
    def getAccounts(self, customer_id):
        # join customer id by customer id inside accounts table
        query = f"SELECT username, account_id, balance, account_type FROM Customer c JOIN Account a ON c.customer_id = a.customer_id WHERE c.customer_id = {customer_id};"
        
        try:
            # load customer object with data
            # do fetch all
            conn = mariadb.connect(**config)
            cursor = conn.cursor()
            print('executing query', query)
            cursor.execute(query)
            conn.commit()
            uname = None
            account_list = []
            for (username, account_id, balance, account_type) in cursor.fetchall():
                print(username, account_id, balance, account_type)
                uname = username
                account_list.append((account_id, balance, account_type))
            unmodifiable_account_list = tuple(account_list)
            result_customer = Customer(uname, unmodifiable_account_list)
            return result_customer
            # return result_customer
        finally:
            cursor.close()
            conn.close()
        
        return None
	
    def getAccountById(self, account_id):
        # get specific account within customer
        query = f"SELECT account_id, account_name, balance, account_type FROM Account WHERE account_id={account_id};"
     	# load account object
        # do fetch one
        # result_account = Account(account_id, balance, account_type)
        try:
            conn = mariadb.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            # (acc_id, balance, account_type) = cursor.fetchone()
            for (acc_id, account_name, balance, account_type) in cursor:
                result_account = Account(acc_id, account_name, balance, account_type)
            return result_account
        finally:
            cursor.close()
            conn.close()
        
        return None
    
    def createAccount(self, customer_id, account_name, balance, account_type):
        # update database with mysql
        try:
            conn = mariadb.connect(**config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Account VALUES (DEFAULT, ?, ?, ?, ?)", (customer_id, account_name, balance, account_type))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        # return nothing because we're returning to customer page requery db
        return None
    
    def withdraw(self, account_id, change):
        # get account snapshot using the entity snapshot 
        result_account = self.getAccountById(account_id)

        # validate balance
        balance = result_account.balance - change

        if balance < 0:
            raise ValueError(f"Cannot withdraw more than balance: {result_account.balance}")

        # update result_account.balance - change
        query = f"UPDATE Account SET balance = {balance} WHERE account_id = {account_id};"

        try:
            conn = mariadb.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        # return nothing because we're moving back to customer page
        return None
    
    def deposit(self, account_id, change):
        # get account snapshot using the entity snapshot 
        result_account = self.getAccountById(account_id)

        # validate balance
        balance = result_account.balance + change

        if balance < 0:
            raise ValueError(f"Cannot withdraw more than balance: {result_account.balance}")

        # update result_account.balance + change
        query = f"UPDATE Account SET balance = {balance} WHERE account_id = {account_id};"
        
        try:
            conn = mariadb.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        finally:
            cursor.close()
            conn.close()
        
        # return nothing because we're moving back to customer page
        return None

if __name__ == "__main__":
    AccountService().createAccount(1,'sample account', 100,"cd")
    AccountService().withdraw(1, 10)
    AccountService().withdraw(1, 10)
    AccountService().deposit(1, 10)
