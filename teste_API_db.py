import psycopg2
import psycopg2.extras

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# Objeto app
app = FastAPI()

class Cliente(BaseModel):
    id: int
    nome: str

#uvicorn teste_API_db:app --reload
#curl -X POST http://127.0.0.1:8000/create -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"id": 12, "nome": "Jean"}'

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/create")
def create_cli(cli: Cliente):

    # Conecta com a db
    conn = psycopg2.connect(
        host = "localhost",
        database = "clientes",
        user = "postgres",
        password = "password",
        port = 5432)
    
    # Inicializa cursor
    curs = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    linha = None

    id = cli.id
    nome = cli.nome

    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        linha = curs.fetchall()
        if len(linha) == 0:
            curs.execute("INSERT INTO clientes (id, nome) VALUES (%s, %s)", (id, nome))
            return {"id": id, "nome": nome}
        else:
            return {"id já existente"}
    except psycopg2.Error as ex:
        print(str(ex))
    finally:
        conn.commit()
        conn.close()
        curs.close()


@app.post("/read")
def read_cli(cli: Cliente):
    
    # Conecta com a db
    conn = psycopg2.connect(
        host = "localhost",
        database = "clientes",
        user = "postgres",
        password = "password",
        port = 5432)
    
    # Inicializa cursor
    curs = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    linha = None

    id = cli.id    
    
    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        linha = curs.fetchall()
        if len(linha) == 0:
            return {"id não encontrado": id}
        else:            
            return {"id": linha[0]['id'], "nome": linha[0]['nome']}            
    except psycopg2.Error as ex:
        print(str(ex))
    finally:
        conn.close()
        curs.close()  


@app.post("/update")
def update_cli(cli: Cliente):
    
    # Conecta com a db
    conn = psycopg2.connect(
        host = "localhost",
        database = "clientes",
        user = "postgres",
        password = "password",
        port = 5432)
    
    # Inicializa cursor
    curs = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    linha = None

    id = cli.id
    nome = cli.nome    
    
    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        linha = curs.fetchall()
        if len(linha) == 0:
            return {"id não encontrado": id}
        else:
            curs.execute("UPDATE clientes SET nome = %s WHERE id = %s", (nome, id))
            curs.execute("SELECT * FROM clientes WHERE id = %s", (id,))
            linha = curs.fetchall()            
            return {"id": linha[0]['id'], "nome": linha[0]['nome']}            
    except psycopg2.Error as ex:
        print(str(ex))
    finally:
        conn.commit()
        conn.close()
        curs.close()


@app.post("/delete")
def delete_cli(cli: Cliente):
    
    # Conecta com a db
    conn = psycopg2.connect(
        host = "localhost",
        database = "clientes",
        user = "postgres",
        password = "password",
        port = 5432)
    
    # Inicializa cursor
    curs = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    linha = None

    id = cli.id    
    
    try:
        curs.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        linha = curs.fetchall()
        if len(linha) == 0:
            return {"id não encontrado": id}
        else:
            curs.execute("DELETE FROM clientes WHERE id = %s", (id,))                        
            return {"id apagado": id}            
    except psycopg2.Error as ex:
        print(str(ex))
    finally:
        conn.commit()
        conn.close()
        curs.close()