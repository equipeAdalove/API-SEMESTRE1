from app import app
from flask import render_template, request

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
        'options': ['Uma declaração clara dos métodos de desenvolvimento', 'Um documento rígido com requisitos detalhados', 'Uma declaração dos objetivos e valores do produto', ' Uma descrição dos recursos do produto', 'Um plano de projeto estático'],
        'answer': 'Uma declaração dos objetivos e valores do produto'
    },
    {
        'id': 8,
        'question': 'Qual é a importância dos critérios de aceitação em User Stories?',
        'options': ['Determinar o tamanho da história', 'Garantir que a história seja implementada', 'Avaliar o desempenho do Scrum Master', 'Controlar o escopo do projeto', 'Promover a inovação na equipe'],
        'answer': 'Garantir que a história seja implementada'
    },
    {
        'id': 9,
        'question': 'Qual é um dos elementos principais de uma User Story?',
        'options': ['Código-fonte', ' Estrutura de dados', 'Diagrama de Gantt', ' Lista de tarefas', ' Who, What, Why'],
        'answer': ' Who, What, Why'
    },
    {
        'id': 10,
        'question': 'Qual é o papel do Product Owner em relação à visão do produto?',
        'options': ['Criar a visão do produto sozinho', 'Desenvolver a visão do produto durante a Sprint Planning', 'Transmitir a visão do produto para a equipe', ' Ignorar a visão do produto após sua criação', 'Promover a competição entre os membros da equipe'],
        'answer': 'Transmitir a visão do produto para a equipe'
    },
]

@app.route('/mod_6')
def modulo_6():
    return render_template('mod_6.html')

@app.route('/mod_6_quiz')
def modulo_6_quiz():
    return render_template('mod_6_quiz.html', questions=questions_6)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    # Lógica para processar o formulário e verificar as respostas
    score = 0
    user_answers = {}
    for question in questions_6:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id)
        correct_answer = question['answer']
        if user_answer == correct_answer:
            score += 1
        user_answers[question['question']] = user_answer
    total_questions = len(questions_6)
    return render_template('mod_6_results.html', score=score, total_questions=total_questions, results=user_answers)

#Módulo 7

@app.route('/mod_7')
def modulo_7():
    return render_template('mod_7.html')
