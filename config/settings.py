import sqlite3

conexao = sqlite3.connect('auladb.sqlite')

cursor = conexao.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(255) UNIQUE,
        password VARCHAR(255)
        );
    """)

def create_table2():
    cursor.execute(""" 
        CREATE TABLE produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomeProduto VARCHAR(150) UNIQUE,
            valorProduto INTEGER NOT NULL
        );       
    """)

    
create_table2()