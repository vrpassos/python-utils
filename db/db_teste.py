import psycopg2
import psycopg2.extras

#Conecta com a db
conn = psycopg2.connect(    
    host = "localhost",
    database = "clientes",
    user = "postgres",
    password = "password",
    port = 5432)

#Cursor
curs = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def show_item():
    
    id = ''
    while not(id.isnumeric()):
        id = input("id: ")
        
    linha = None
    
    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        linha = curs.fetchall()
        if len(linha) == 0:
            print('Id não encontrado\n')
        else:
            print(f"id {linha[0]['id']} name {linha[0]['nome']}\n")
    except psycopg2.Error as ex:
	    print(str(ex))


def add_item():
    
    id_in = ''
    while not(id_in.isnumeric()):
        id_in = input("Digite o id: ")
    nome_in = input("Digite o nome: ")

    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id_in,))
        linha = curs.fetchall()
        if len(linha) == 0:
            curs.execute("INSERT INTO clientes (id, nome) VALUES (%s, %s)", (id_in, nome_in))
        else:
            print("Id já existe\n")
    except psycopg2.Error as ex:
        print(str(ex))
        
    conn.commit()


def update_item():
    
    id_in = ''
    while not(id_in.isnumeric()):
        id_in = input("Digite o id: ")

    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id_in,))
        linha = curs.fetchall()
        if len(linha) == 0:
            print("Id não encontrado\n")
        else:
            print(f"id {linha[0]['id']} name {linha[0]['nome']}\n")                 
    except psycopg2.Error as ex:
        print(str(ex))

    menu = input("Alterar(s/n)? ")

    if menu.upper() == 'S':
        nome_in = input("Digite o nome: ")
        curs.execute("UPDATE clientes SET nome = %s WHERE id = %s", (nome_in, id_in))
    
    conn.commit()


def del_item():

    id_in = ''
    while not(id_in.isnumeric()):
        id_in = input("Digite o id: ")

    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id_in,))
        linha = curs.fetchall()
        if len(linha) == 0:
            print('Id não encontrado\n')
        else:
            print(f"id {linha[0]['id']} name {linha[0]['nome']}\n")
    except psycopg2.Error as ex:
        print(str(ex))
        
    menu = input("Apagar(s/n)? ")

    if menu.upper() == 'S':
        curs.execute("DELETE FROM clientes WHERE id = %s", (id_in,))
    
    conn.commit()


while True:

    menu = ''
    print("Teste Database")
    print("1 - Consulta")
    print("2 - Adiciona")
    print("3 - Altera")
    print("4 - Exclui")
    print("5 - Sair")
    while not(menu.isnumeric()):
        menu = input("Opção: ")
    
    if menu == '1':
        show_item()
    elif menu == '2':
        add_item()
    elif menu == '3':
        update_item()
    elif menu == '4':
        del_item()
    elif menu == '5':
        print("Até logo")
        curs.close()
        conn.close()
        break
    else:
        print("Opção inválida.")

