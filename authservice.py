import hashlib
from flask import session
import mariadb
from accountservice import AccountService
from flask import current_app

config = {
     'user': 'root',
     'password': '',
     'host': '127.0.0.1', # try changing to localhost
     'port': 3306,
     'database': 'flask_app',
 }

accservice = AccountService()

class AuthService:
    def __init__(self):
        pass

    def register(self, username, password, balance=100.00):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password.encode('utf-8'))
        hashed_pass = sha1_hash.hexdigest()
        query = f"INSERT INTO Customer (username, password) VALUES ('{username}', '{hashed_pass}');"

        try:
            conn = mariadb.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            # create initial account with balance 100.00
            accservice.createAccount(cursor.lastrowid, f'default {username} account', balance, 'Default Checkings Account')
        except Exception as exception:
            print('caught exception:', exception)
            raise ValueError(str(exception))
        finally:
            cursor.close()
            conn.close()
    
    def login(self, username, password):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password.encode('utf-8'))
        hashed_pass = sha1_hash.hexdigest()
        query = f"SELECT customer_id, username FROM Customer WHERE username='{username}' AND password='{hashed_pass}';"
        
        res = None
        try:
            conn = mariadb.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query)
            res = cursor.fetchone()
        finally:
            cursor.close()
            conn.close()
        
        if res:
            session['customer_id'], session['username'] = res[0], res[1]
            session['secret_key'] = current_app.config['SECRET_KEY']
            return {'customer_id': session['customer_id'], 'username': session['username']}
        
        return {}
    