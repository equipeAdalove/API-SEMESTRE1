from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/modulo_1')
def modulo_1():
    return render_template('mod_1.html')

@app.route('/modulo_2')
def modulo_2():
    return render_template('mod_2.html')

@app.route('/modulo_3')
def modulo_3():
    return render_template('mod_3.html')

@app.route('/modulo_4')
def modulo_4():
    return render_template('mod_4.html')

@app.route('/modulo_5')
def modulo_5():
    return render_template('mod_5.html')

@app.route('/modulo_6')
def modulo_6():
    return render_template('mod_6.html')

@app.route('/modulo_7')
def modulo_7():
    return render_template('mod_7.html')
