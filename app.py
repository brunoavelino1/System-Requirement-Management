from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import re

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS requisitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            serial TEXT UNIQUE,
            titulo TEXT NOT NULL,
            descricao TEXT,
            prioridade TEXT,
            categoria TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def gerar_serial(categoria):
    prefixos = {'Funcional': 'RF', 'Não Funcional': 'RNF', 'Negócio': 'RN'}
    prefixo = prefixos.get(categoria, 'REQ')
    conn = get_db_connection()
    ultimo = conn.execute('SELECT serial FROM requisitos WHERE categoria = ? ORDER BY id DESC LIMIT 1', (categoria,)).fetchone()
    conn.close()
    if ultimo:
        proximo_num = int(ultimo['serial'].split('-')[1]) + 1
    else:
        proximo_num = 1
    return f"{prefixo}-{str(proximo_num).zfill(3)}"

def validar_requisito(texto):
    # Regra de Atomicidade: não pode ter 'e' ou 'ou'
    if re.search(r'\b(e|ou)\b', texto.lower()) or len(texto) > 150:
        return False
    return True

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    requisitos = conn.execute('SELECT * FROM requisitos ORDER BY serial ASC').fetchall()
    conn.close()
    return render_template('index.html', requisitos=requisitos)

@app.route('/create', methods=('POST',))
def create():
    titulo = request.form.get('titulo', '')
    descricao = request.form.get('descricao', '')
    prioridade = request.form.get('prioridade', 'Média')
    categoria = request.form.get('categoria', 'Funcional')
    
    if validar_requisito(titulo):
        serial = gerar_serial(categoria)
        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO requisitos (serial, titulo, descricao, prioridade, categoria) VALUES (?, ?, ?, ?, ?)',
                         (serial, titulo, descricao, prioridade, categoria))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            pass
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    req = conn.execute('SELECT * FROM requisitos WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        titulo = request.form.get('titulo', '')
        descricao = request.form.get('descricao', '')
        prioridade = request.form.get('prioridade', 'Média')
        categoria = request.form.get('categoria', 'Funcional')
        
        conn.execute('UPDATE requisitos SET titulo = ?, descricao = ?, prioridade = ?, categoria = ? WHERE id = ?',
                     (titulo, descricao, prioridade, categoria, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('edit.html', req=req)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM requisitos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



