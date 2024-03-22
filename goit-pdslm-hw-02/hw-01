import psycopg2 as ps
import pandas as pd
from IPython.display import display

def create_connection():
    """ create a database connection to a PostgreSQL database """
    try:
        connect = ps.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5432"
        )
        print("Connected successfully!")
        return connect
    except ps.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def create_tables(connect):
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                fullname VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS status (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
            );
        """)
        
        connect.commit()
        print("Tables created successfully!")
        cursor.close()
    except ps.Error as e:
        print(f"Error creating tables: {e}")

def display_tables(connect):
    try:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM users;")
        users_data = cursor.fetchall()
        users_df = pd.DataFrame(users_data, columns=[desc[0] for desc in cursor.description])
        print("Users Table:")
        display(users_df)
        
        cursor.execute("SELECT * FROM status;")
        status_data = cursor.fetchall()
        status_df = pd.DataFrame(status_data, columns=[desc[0] for desc in cursor.description])
        print("Status Table:")
        display(status_df)
        
        cursor.execute("SELECT * FROM tasks;")
        tasks_data = cursor.fetchall()
        tasks_df = pd.DataFrame(tasks_data, columns=[desc[0] for desc in cursor.description])
        print("Tasks Table:")
        display(tasks_df)
        
        cursor.close()
    except ps.Error as e:
        print(f"Error displaying tables: {e}")

if __name__ == '__main__':
    connect = create_connection()
    if connect is not None:
        create_tables(connect)
        display_tables(connect)
        connect.close()
    else:
        print("Error! Cannot create the database connection.")
