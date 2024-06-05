import sqlite3
from utils import connection_db
import bcrypt



def criptografar(password):
    bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
    return hashed

def checar_password(password, hashed):
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed)

@connection_db
def list_users(cursor):
    users = cursor.execute("""
        SELECT id, email FROM users
    """).fetchall()
    print(users)


@connection_db
def insert_user(cursor, email, password):
    password = criptografar(password)
    cursor.execute("""
        INSERT INTO users(email, password) 
                VALUES (?, ?)
    """, [email, password])
    print('Usuario inserido.')


@connection_db
def login(cursor, username, password):
    sql = "SELECT * FROM users WHERE email=?"
    user =  cursor.execute(sql, [username]).fetchone()
    return user and checar_password(password, user[2])



@connection_db
def remove_user(cursor, id):
    sql = "DELETE FROM users WHERE id=?"
    cursor.execute(sql, [id])
    print('Usuario removido')
    

@connection_db
def update_user(cursor, id, new_email):
    sql = "UPDATE users SET email=? WHERE id=?"
    cursor.execute(sql, [new_email, id])
    print('Usuario atualizado')