from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'api1ads'
mysql = MySQL(app)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        id = request.form['id']
        nome = request.form['nome']
        nota = request.form['nota']
        opiniao = request.form['opiniao']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO formulario (id, nome, nota, opiniao) VALUES (%d, %s, %d, %s)", (id, nome, nota, opiniao))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
