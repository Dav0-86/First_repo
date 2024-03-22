from faker import Faker
import psycopg2
import random

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5432"
        )
        print("Connected to PostgreSQL successfully!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def insert_data(conn):
    try:
        cur = conn.cursor()
        faker = Faker()
        # Insert users
        for _ in range(10):
            fullname = faker.name()
            email = faker.email()
            cur.execute("""
                INSERT INTO users (fullname, email) 
                VALUES (%s, %s);
            """, (fullname, email))
        
        # Insert status
        status_names = ['new', 'in progress', 'completed']
        for name in status_names:
            cur.execute("""
                INSERT INTO status (name) 
                VALUES (%s);
            """, (name,))
        
        # Insert tasks
        for _ in range(20):
            title = faker.sentence()
            description = faker.text()
            status_id = random.randint(1, len(status_names))
            user_id = random.randint(1, 10)
            cur.execute("""
                INSERT INTO tasks (title, description, status_id, user_id) 
                VALUES (%s, %s, %s, %s);
            """, (title, description, status_id, user_id))
        
        conn.commit()
        print("Data inserted successfully!")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")

if __name__ == '__main__':
    conn = create_connection()
    if conn is not None:
        insert_data(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")
