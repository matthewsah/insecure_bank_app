import mysql.connector
import Customer
import AccountSnapshot

config = {
     'user': 'root',
     'password': '',
     'host': '127.0.0.1',
     'database': 'flask_app',
     'raise_on_warnings': True
 }

class AccountService:
    def __init__(self):
        pass
        
    def getCustomerById(self, customer_id):
        # join customer id by customer id inside accounts table
        query = f"SELECT username, account_id, balance, account_type FROM Customer c JOIN Account a ON c.customer_id = a.customer_id WHERE c.customer_id = {customer_id};"
        
        try:
            # load customer object with data
            # do fetch all
            conn = mysql.connector.connect(*config)
            cursor = conn.cursor()
            cursor.execute(query, (username, account_id, balance, account_type))
            uname = None
            account_list = []
            for (username, account_id, balance, account_type) in cursor:
                uname = username
                account_list.append((account_id, balance, account_type))
            unmodifiable_account_list = tuple(account_list)
            # result_customer = Customer(uname, unmodifiable_account_list)
            # return result_customer
        finally:
            cursor.close()
            conn.close()
        
        return None
	
    def getAccountById(self, account_id):
        # get specific account within customer
        query = f"SELECT account_id, balance, account_type FROM Account WHERE account_id = {account_id};"
        
     	# load account object
        # do fetch one
        # result_account = Account(account_id, balance, account_type)
        try:
            conn = mysql.connector.connect(*config)
            cursor = conn.cursor()
            cursor.execute(query)
            (acc_id, balance, account_type) = cursor.fetchone()
            result_account = AccountSnapshot(acc_id, balance, account_type)
            return result_account
        finally:
            cursor.close()
            conn.close()
        
        return None
        
    def createAccount(self, balance, account_type):
        # create account based on balance and account type
        query = f"INSERT INTO Account VALUES({balance}, '{account_type}');"
        
        # update database with mysql
        try:
            conn = mysql.connector.connect(*config)
            cursor = conn.cursor()
            cursor.execute(query)
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

        # update result_account.balance - change
        query = f"UPDATE Account SET balance = {balance} WHERE account_id = {account_id};"

        try:
            conn = mysql.connector.connect(*config)
            cursor = conn.cursor()
            cursor.execute(query)
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

        # update result_account.balance + change
        query = f"UPDATE Account SET balance = {balance} WHERE account_id = {account_id};"
        
        try:
            conn = mysql.connector.connect(*config)
            cursor = conn.cursor()
            cursor.execute(query)
        finally:
            cursor.close()
            conn.close()
        
        # return nothing because we're moving back to customer page
        return None
