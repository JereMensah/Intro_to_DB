# ...existing code...
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (update credentials as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection is None or not connection.is_connected():
            print("Failed to connect to MySQL server.")
            return

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        # commit is optional for DDL but safe to call
        connection.commit()
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except Exception:
                pass
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
# ...existing code...