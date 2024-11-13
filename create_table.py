import psycopg2
from psycopg2 import sql
import os

# PostgreSQL connection string
DATABASE_URL = "postgresql://admin:vP0wcNFIG4jo@ep-bold-snow-a64ztnv3-pooler.us-west-2.aws.neon.tech/finalengine?sslmode=require"

# Establishing a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    print("Successfully connected to the database!")

    # Creating the table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255)
    );
    """
    cursor.execute(create_table_query)
    print("Table created successfully or already exists.")

    # Inserting a sample record
    name = "legionx"
    insert_query = "INSERT INTO users (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    print(f"Inserted {name} into the table.")

    # Fetching and printing all records
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    print("Users in the table:")
    for row in result:
        print(f"id: {row[0]}, name: {row[1]}")

    # Committing the transaction
    connection.commit()

except Exception as e:
    print("Error while interacting with the database:", e)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Database connection closed.")
