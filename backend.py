import sqlite3

def conectar():
    # Cria (ou conecta) a um arquivo de banco de dados chamado 'biblioteca.db'
    return sqlite3.connect("biblioteca.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER,
        categoria TEXT
    )
''')
    conn.commit()
    conn.close()

def adicionar_livro(titulo, autor, ano, categoria):
    conn = conectar()
    cursor = conn.cursor()
   cursor.execute(
    """
    INSERT INTO livros
    (titulo, autor, ano, categoria)
    VALUES (?, ?, ?, ?)
    """,
    (titulo, autor, ano, categoria)
)
    conn.commit()
    conn.close()

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    linhas = cursor.fetchall()
    conn.close()
    return linhas

def buscar_livros(termo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM livros
        WHERE titulo LIKE ? OR autor LIKE ?
    """, (f"%{termo}%", f"%{termo}%"))

    livros = cursor.fetchall()

    conn.close()
    return livros

def atualizar_livro(id_livro, titulo, autor, ano, categoria):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
    UPDATE livros
    SET titulo=?, autor=?, ano=?, categoria=?
    WHERE id=?
    """,
    (titulo, autor, ano, categoria, id_livro)
)
    conn.commit()
    conn.close()

def deletar_livro(id_livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id=?", (id_livro,))
    conn.commit()
    conn.close()
