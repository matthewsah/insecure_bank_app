import hashlib
from flask import session
import mariadb

config = {
     'user': 'root',
     'password': '',
     'host': '127.0.0.1',
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

        try:
            cursor = conn.cursor()
            cursor.execute(query)
        finally:
            cursor.close()
            conn.close()
    
    def login(self, username, password):
        conn = mariadb.connect(**config)
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password.encode('utf-8'))
        hashed_pass = sha1_hash.hexdigest()
        query = f'SELECT customer_id FROM Customer WHERE username={username} AND password={hashed_pass}'
        
        customer_id = None
        
        try:
            cursor = conn.cursor()
            customer_id = cursor.execute(query)
        finally:
            cursor.close()
            conn.close()
        
        if customer_id:
            session['username'] = username
            session['customer_id'] = customer_id
        
        return session
    