import sqlite3

def criar_conexao():
    conexao = sqlite3.connect('banco_projeto.db')
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()