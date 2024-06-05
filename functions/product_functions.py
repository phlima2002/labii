import sqlite3
from utils import connection_db

@connection_db
def insert_product(cursor, nomeProduto, valorProduto):
    cursor.execute("""
        INSERT INTO produtos(nomeProduto, valorProduto) 
                VALUES (?, ?)
    """, [nomeProduto, valorProduto])
    print('Produto inserido.')

@connection_db
def update_product(cursor, id, new_Product, new_Value):
    sql = "UPDATE produtos SET nomeProduto=? WHERE id=?"
    cursor.execute(sql, [new_Product, id])

    sql2 = "UPDATE produtos SET valorProduto=? WHERE id=?"
    cursor.execute(sql2, [new_Value, id])
    print('Produto atualizado')

@connection_db
def remove_product(cursor, id):
    sql = "DELETE FROM produtos WHERE id=?"
    cursor.execute(sql, [id])
    print('Produto removido')

@connection_db
def list_product(cursor):
    idWanted = input('Digite o id do produto que você deseja achar\n')
    produtos = cursor.execute("""
        SELECT * FROM produtos WHERE id = (?)
                              """, [idWanted]).fetchall()
    print(produtos)

@connection_db
def list_allProducts(cursor):
    produtos = cursor.execute("""
        SELECT * FROM produtos
    """).fetchall()
    print(produtos)
