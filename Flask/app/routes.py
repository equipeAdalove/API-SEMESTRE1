from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

#Módulo 1

questions_1 = [
    {
        'id': 1,
        'question': 'Qual é a principal transformação que o desenvolvimento de software passou nos últimos anos?',
        'options': ['Aumento da rigidez nas abordagens de gestão de projetos.', 'Maior foco na entrega incremental.', 'Redução da competitividade no mercado.', 'A adoção de métodos ágeis.'],
        'answer': 'A adoção de métodos ágeis.'
    },
    {
        'id': 2,
        'question': 'Quais são os três pilares fundamentais do Scrum?',
        'options': [' Planejamento, execução, controle', 'Transparência, inspeção, adaptação', 'Documentação, revisão, entrega', 'Individualidade, inovação, adaptação'],
        'answer': 'Transparência, inspeção, adaptação'
    },
    {
        'id': 3,
        'question': 'Onde o Scrum pode ser aplicado?',
        'options': ['Apenas em projetos de desenvolvimento de software', 'Apenas em projetos com requisitos estáveis e definidos', 'A uma variedade de projetos, desde que haja complexidade e incerteza', 'Apenas em empresas de grande porte'],
        'answer': 'A uma variedade de projetos, desde que haja complexidade e incerteza'
    },
    {
        'id': 4,
        'question': 'Qual é um dos benefícios do Scrum em termos de gerenciamento de projetos?',
        'options': ['Maior rigidez no controle do progresso do projeto', 'Redução da colaboração entre os membros da equipe', ' Detecção precoce de problemas', 'Menor foco no valor entregue ao cliente'],
        'answer': 'Detecção precoce de problemas'
    },
    {
        'id': 5,
        'question': 'Quem são os criadores do SCRUM?',
        'options': ['Steve Jobs e Bill Gates.', 'Jeff Sutherland e Ken Schwaber.', 'Tim Berners-Lee e Linus Torvalds.', 'Larry Page e Sergey Brin.'],
        'answer': 'Jeff Sutherland e Ken Schwaber.'
    },
    {
        'id': 6,
        'question': 'O que é enfatizado pelo Manifesto Ágil?',
        'options': ['Indivíduos e interações, software em funcionamento, colaboração com o cliente e resposta a mudanças', 'Processos e ferramentas, documentação abrangente, negociação de contratos, seguir um plano', 'Entrega de produtos finais sem interações com o cliente', 'Priorização de documentação sobre indivíduos e interações'],
        'answer': 'Indivíduos e interações, software em funcionamento, colaboração com o cliente e resposta a mudanças'
    },
    {
        'id': 7,
        'question': 'Quais são alguns exemplos práticos de valores do Scrum?',
        'options': ['Controle e estagnação', 'Rigidez e documentação abrangente', 'Foco e respeito', ' Falta de colaboração e coragem'],
        'answer': 'Foco e respeito'
    },
    {
        'id': 8,
        'question': 'O que os princípios ágeis enfatizam?',
        'options': ['Satisfação do desenvolvedor', 'Satisfação do cliente, entrega incremental, colaboração e adaptação contínua', 'Foco na documentação e nos processos', 'Resistência à mudança'],
        'answer': 'Satisfação do cliente, entrega incremental, colaboração e adaptação contínua'
    },
    {
        'id': 9,
        'question': 'O que é essencial para promover a colaboração, o trabalho em equipe e a busca pela excelência no Scrum?',
        'options': ['Rigidez e falta de adaptação', ' Resistência à mudança', 'Valores e princípios do Scrum', ' Controle centralizado'],
        'answer': ' WValores e princípios do Scrum'
    },
    {
        'id': 10,
        'question': 'O que são Métodos Ágeis?',
        'options': ['Abordagens inflexíveis e rígidas.', 'Estratégias para reduzir a colaboração da equipe.', 'Uma abordagem flexível e adaptativa para maximizar o valor entregue ao cliente.', ' Práticas para evitar feedback contínuo.'],
        'answer': 'Uma abordagem flexível e adaptativa para maximizar o valor entregue ao cliente.'
    },
]

@app.route('/mod_1')
def modulo_1():
    return render_template('mod_1.html')

@app.route('/mod_1_quiz')
def modulo_1_quiz():
    return render_template('mod_1_quiz.html', questions=questions_1)

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
