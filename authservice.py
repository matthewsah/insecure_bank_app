import mysql.connector
import hashlib
from flask import session

class AuthService:
    def __init__(self):
        pass

    def register(self, username, password):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password.encode('utf-8'))
        hashed_pass = sha1_hash.hexdigest()
        query = f'INSERT INTO Customer VALUES ({username}, {hashed_pass});'

        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query)
        finally:
            cursor.close()
            conn.close()
    
    def login(self, username, password):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password.encode('utf-8'))
        hashed_pass = sha1_hash.hexdigest()
        query = f'SELECT customer_id FROM Customer WHERE username={username} AND password={hashed_pass}'
        
        customer_id = None
        
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            customer_id = cursor.execute(query)
        finally:
            cursor.close()
            conn.close()
        
        if customer_id:
            session['username'] = username
            session['customer_id'] = customer_id
        
        print('the session is now ', session)
        return session

    