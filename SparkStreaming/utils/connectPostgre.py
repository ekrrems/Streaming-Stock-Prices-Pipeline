# This script includes helper function

import os 
from dotenv import load_dotenv
import psycopg2
from datetime import datetime

load_dotenv()
postgre_password = os.getenv("POSTGRE_PASSWORD")

def write_to_database(batch_df, batch_id):
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="finnhub",
        user="postgres",
        password=postgre_password,
        host="localhost",
        port="5432"
    )
    
    # Insert rows into the database table
    cur = conn.cursor()
    for row in batch_df.collect():
        c, p, s, t, v = row
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO finnhub_data (c_array, p, s, t, v, timestamp_column) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (c, float(p), s, float(t), float(v), formatted_datetime))
    conn.commit()

    # Close the database connection
    cur.close()
    conn.close()