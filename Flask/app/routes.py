from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/mod_1')
def modulo_1():
    return render_template('mod_1.html')

@app.route('/mod_2')
def modulo_2():
    return render_template('mod_2.html')

@app.route('/mod_3')
def modulo_3():
    return render_template('mod_3.html')

@app.route('/mod_4')
def modulo_4():
    return render_template('mod_4.html')

@app.route('/mod_5')
def modulo_5():
    return render_template('mod_5.html')

#Módulo 6

questions_6 = [
    {
        'id': 1,
        'question': 'Qual é a base da auto-organização no Scrum?',
        'options': ['Instruções detalhadas', 'Microgerenciamento', 'Confiança mútua e clareza dos objetivos do projeto', 'Autoritarismo', 'Delegação excessiva'],
        'answer': 'Confiança mútua e clareza dos objetivos do projeto'
    },
    {
        'id': 2,
        'question': 'O que a auto-organização promove nas equipes ágeis?',
        'options': ['Conformidade', 'Individualismo', 'Colaboração', 'Resistência à mudança', 'Competição'],
        'answer': 'Colaboração'
    },
    {
        'id': 3,
        'question': 'Qual é uma das responsabilidades do Scrum Master?',
        'options': ['Promover o engajamento', 'Ditar as tarefas da equipe', 'Resolver todos os conflitos', 'Focar apenas nos resultados', 'Delegação excessiva'],
        'answer': 'Promover o engajamento'
    },
    {
        'id': 4,
        'question': 'O que são User Stories em metodologias ágeis?',
        'options': ['Grandes descrições de funcionalidades', 'Requisitos escritos apenas pelo Product Owner', ' Histórias irrelevantes', 'Documentos detalhados e rígidos', 'Pequenas descrições de funcionalidades'],
        'answer': 'Pequenas descrições de funcionalidades'
    },
    {
        'id': 5,
        'question': 'Qual é um dos benefícios da auto-organização?',
        'options': ['Microgerenciamento eficiente', 'Colaboração ativa', 'Resistência à mudança', 'Conformidade absoluta', ' Falta de autonomia'],
        'answer': 'Promover o engajamento'
    },
    {
        'id': 6,
        'question': 'Qual é uma das funções do Scrum Master como facilitador?',
        'options': ['Aumentar os conflitos na equipe', 'Minimizar a comunicação entre os membros', 'Ignorar as necessidades dos stakeholders', 'Otimizar os processos de trabalho', 'Incentivar a competição entre os membros'],
        'answer': 'Otimizar os processos de trabalho'
    },
    {
        'id': 7,
        'question': 'O que é a visão do produto em metodologias ágeis?',
        'options': ['Grandes descrições de funcionalidades', 'Requisitos escritos apenas pelo Product Owner', ' Histórias irrelevantes', 'Documentos detalhados e rígidos', 'Pequenas descrições de funcionalidades'],
        'answer': 'Pequenas descrições de funcionalidades'
    },
]

@app.route('/mod_6')
def modulo_6():
    return render_template('mod_6.html')

@app.route('/mod_7')
def modulo_7():
    return render_template('mod_7.html')
