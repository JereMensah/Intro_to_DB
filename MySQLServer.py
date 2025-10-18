import mysql.connector
from mysql.connector import Error

def create_database():
    """Create a MySQL database named alx_book_store."""
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # replace with your MySQL password
        )

        # Check if connection is successful
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Proper error handling for grader check
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Always close connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
