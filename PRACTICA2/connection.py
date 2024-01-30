import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="user_postgres",
    password="pass_postgres",
    host="localhost",
    port="5432"
)
connectcion = conn.cursor()

print (connectcion);