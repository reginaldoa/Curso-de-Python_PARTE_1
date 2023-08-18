import sqlite3
from pathlib import Path

ROOT_DIR =  Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE =  ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


connection =  sqlite3.connect(DB_FILE)
cursor = connection.cursor()


#SQL
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

#Registrar valores na coluna da tabela

#CUIDADO AO FAZER ASSIM : SQL INJECTION
cursor.execute(

    f'INSERT INTO {TABLE_NAME} (id , name, weight) '
    ' VALUES (NULL, "Reginaldo Alves", 96) , (NULL, "Regineide Alves", 70)'
) 
connection.commit()


#cursor.executemany('')


cursor.close()
connection.close()