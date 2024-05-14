import mysql.connector
import hashlib

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'flask_app',
    'raise_on_warnings': True
}

try:
    # Establish a database connection
    conn = mysql.connector.connect(**config)
    print("Connection successful!")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT DATABASE();")

    # Fetch the result
    database_name = cursor.fetchone()
    print(f"Connected to database: {database_name[0]}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()

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