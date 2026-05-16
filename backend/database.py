import psycopg2

try:
    conn = psycopg2.connect(
        dbname="medical_ai",
        user="postgres",
        password="saurav4686",
        host="localhost",
        port="5432"
    )

    print("Database connected successfully")

    conn.close()

except Exception as e:
    print("Connection failed")
    print(e)