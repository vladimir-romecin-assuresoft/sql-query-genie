import sqlite3

def get_connection():
    return sqlite3.connect("database.db")

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results, None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()