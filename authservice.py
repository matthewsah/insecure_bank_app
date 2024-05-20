import hashlib
from flask import session
import mariadb

config = {
     'user': 'root',
     'password': '',
     'host': '127.0.0.1', # try changing to localhost
     'port': 3306,
     'database': 'flask_app',
 }

class AuthService:
    def __init__(self):
        pass

    def register(self, username, password):
        conn = mariadb.connect(**config)
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password.encode('utf-8'))
        hashed_pass = sha1_hash.hexdigest()
        query = f'INSERT INTO Customer VALUES ({username}, {hashed_pass});'
        print('query is ', query)

        try:
            print('getting cursor')
            cursor = conn.cursor()
            print('got cursor')
            cursor.execute(query)
            print('executing query')
        finally:
            cursor.close()
            conn.close()
    
    def login(self, username, password):
        conn = mariadb.connect(**config)
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password.encode('utf-8'))
        hashed_pass = sha1_hash.hexdigest()
        query = f'SELECT customer_id, username FROM Customer WHERE username="{username}" AND password="{hashed_pass}"'
        
        # customer_id = None
        # username = None

        try:
            cursor = conn.cursor()
            res = cursor.execute(query)
        finally:
            cursor.close()
            conn.close()
        
        if res:
            session['customer_id'], session['username'] = res[0], res[1]
        
        return session
    