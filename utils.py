import sqlite3

def connection_db(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('auladb.sqlite')
        cursor = conn.cursor()
        result = func(cursor, *args, **kwargs)
        conn.commit()
        cursor.close()
        conn.close()
        return result
    return wrapper
