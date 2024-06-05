import getpass
from functions.user_functions import insert_user, login, remove_user, update_user, list_users
from functions.product_functions import insert_product, update_product, remove_product, list_product, list_allProducts
import stdiomask

while(True):
    print("""
        1 - Cadastrar Usuario 
        2 - Entrar no Sistema
    """)

    opc = int(input("Digite opcao: "))

    if opc == 1:
        username = input("Digita o email: ")
        password = input("Digite a senha: ")
        insert_user(username, password)

    elif opc == 2:
        username = input("Digita o email: ")
        password = stdiomask.getpass("Digite a senha: ", mask="*")
        autenticado = login(username, password)
        if autenticado:
            print("AUTENTICADO")
            while(True):
                print("""
                    0 - Mostrar usuarios
                    1 - Deletar usuario
                    2 - Update de usuario
                    3 - Cadastrar produto
                    4 - Alterar produto
                    5 - Remover produto
                    6 - Mostrar produto por id
                    7 - Mostrar todos produtos
                """)
                
                opcDentro =int(input('Digite opcao: '))
                if opcDentro == 0:
                    list_users()


                if opcDentro == 1:
                    user_id = int(input("ID: "))
                    remove_user(user_id)


                elif opcDentro == 2:
                    user_id = int(input("ID: \n"))
                    email = input("Digite novo email\n")
                    update_user(user_id, email)

                elif opcDentro == 3:
                    nomeProduto = input('Digite o nome do produto\n').title()
                    valorProduto = float(input('Digite o valor do produto\n'))
                    insert_product(nomeProduto,valorProduto)

                elif opcDentro == 4:
                    user_id = int(input("ID: \n"))
                    nome = input("Digite novo nome do produto\n")
                    valor = float(input('Digite novo valor do produto\n'))
                    update_product(user_id, nome, valor)
                
                elif opcDentro == 5:
                    user_id = int(input("ID: "))
                    remove_product(user_id)

                elif opcDentro == 6:
                    list_product()

                elif opcDentro == 7:
                    list_allProducts()

            
    
        
