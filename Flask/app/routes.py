from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/testes')
def testes():
    return render_template('testes.html')

#Módulo 1

questions_1 = [
    {
        'id': 1,
        'question': '1) Qual é a principal transformação que o desenvolvimento de software passou nos últimos anos?',
        'options': ['a)Aumento da rigidez nas abordagens de gestão de projetos.', 'b)Maior foco na entrega incremental.', 'c)Redução da competitividade no mercado.', 'd)A adoção de métodos ágeis.'],
        'answer': 'A adoção de métodos ágeis.'
    },
    {
        'id': 2,
        'question': '2) Quais são os três pilares fundamentais do Scrum?',
        'options': ['a)Planejamento, execução, controle', 'b)Transparência, inspeção, adaptação', 'c)Documentação, revisão, entrega', 'd)Individualidade, inovação, adaptação'],
        'answer': 'Transparência, inspeção, adaptação'
    },
    {
        'id': 3,
        'question': '3) Onde o Scrum pode ser aplicado?',
        'options': ['a)Apenas em projetos de desenvolvimento de software', 'b)Apenas em projetos com requisitos estáveis e definidos', 'c)A uma variedade de projetos, desde que haja complexidade e incerteza', 'd)Apenas em empresas de grande porte'],
        'answer': 'A uma variedade de projetos, desde que haja complexidade e incerteza'
    },
    {
        'id': 4,
        'question': '4) Qual é um dos benefícios do Scrum em termos de gerenciamento de projetos?',
        'options': ['a)Maior rigidez no controle do progresso do projeto', 'b)Redução da colaboração entre os membros da equipe', ' c)Detecção precoce de problemas', 'd)Menor foco no valor entregue ao cliente'],
        'answer': 'Detecção precoce de problemas'
    },
    {
        'id': 5,
        'question': '5) Quem são os criadores do SCRUM?',
        'options': ['a)Steve Jobs e Bill Gates.', 'b)Jeff Sutherland e Ken Schwaber.', 'c)Tim Berners-Lee e Linus Torvalds.', 'd)Larry Page e Sergey Brin.'],
        'answer': 'Jeff Sutherland e Ken Schwaber.'
    },
    {
        'id': 6,
        'question': '6) O que é enfatizado pelo Manifesto Ágil?',
        'options': ['a)Indivíduos e interações, software em funcionamento, colaboração com o cliente e resposta a mudanças', 'b)Processos e ferramentas, documentação abrangente, negociação de contratos, seguir um plano', 'c)Entrega de produtos finais sem interações com o cliente', 'd)Priorização de documentação sobre indivíduos e interações'],
        'answer': 'Indivíduos e interações, software em funcionamento, colaboração com o cliente e resposta a mudanças'
    },
    {
        'id': 7,
        'question': '7) Quais são alguns exemplos práticos de valores do Scrum?',
        'options': ['a)Controle e estagnação', 'b)Rigidez e documentação abrangente', 'c)Foco e respeito', 'd)Falta de colaboração e coragem'],
        'answer': 'Foco e respeito'
    },
    {
        'id': 8,
        'question': '8) O que os princípios ágeis enfatizam?',
        'options': ['a)Satisfação do desenvolvedor', 'b)Satisfação do cliente, entrega incremental, colaboração e adaptação contínua', 'c)Foco na documentação e nos processos', 'd)Resistência à mudança'],
        'answer': 'Satisfação do cliente, entrega incremental, colaboração e adaptação contínua'
    },
    {
        'id': 9,
        'question': '9) O que é essencial para promover a colaboração, o trabalho em equipe e a busca pela excelência no Scrum?',
        'options': ['a)Rigidez e falta de adaptação', 'b)Resistência à mudança', 'c)Valores e princípios do Scrum', 'd)Controle centralizado'],
        'answer': ' WValores e princípios do Scrum'
    },
    {
        'id': 10,
        'question': '10) O que são Métodos Ágeis?',
        'options': ['a)Abordagens inflexíveis e rígidas.', 'b)Estratégias para reduzir a colaboração da equipe.', 'c)Uma abordagem flexível e adaptativa para maximizar o valor entregue ao cliente.', 'd)Práticas para evitar feedback contínuo.'],
        'answer': 'Uma abordagem flexível e adaptativa para maximizar o valor entregue ao cliente.'
    },
]

@app.route('/mod_1')
def modulo_1():
    return render_template('mod_1.html')

@app.route('/mod_1_quiz')
def modulo_1_quiz():
    return render_template('mod_1_quiz.html', questions=questions_1)

@app.route('/submit_quiz_1', methods=['POST'])
def submit_quiz_1():
    # Lógica para processar o formulário e verificar as respostas
    score = 0
    user_answers = {}
    for question in questions_1:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id)
        correct_answer = question['answer']
        if user_answer == correct_answer:
            score += 1
        user_answers[question['question']] = user_answer
    total_questions = len(questions_1)
    return render_template('mod_1_results.html', score=score, total_questions=total_questions, results=user_answers)

@app.route('/mod_2')
def modulo_2():
    return render_template('mod_2.html')

# Módulo 2

questions_2 = [
    {
        'id': 1,
        'question': '1) Qual é um dos pilares fundamentais do Scrum, que permeia todas as atividades e interações da equipe?',
        'options': ['A Inspeção', 'A Adaptação', 'Possuir Transparência', 'Colaboração'],
        'answer': 'Possuir Transparência'
    },
    {
        'id': 2,
        'question': '2) Durante o planejamento do sprint, a equipe seleciona itens para incluir no backlog do sprint com base em:',
        'options': ['Feedback dos stakeholders', 'Prioridades estabelecidas pela equipe', 'Revisões de sprint', 'Objetivos do produto'],
        'answer': 'Prioridades estabelecidas pela equipe'
    },
    {
        'id': 3,
        'question': '3) O que acontece durante as reuniões diárias de stand-up no Scrum?',
        'options': ['Análises da sprint', 'Discussão dos resultados do sprint', 'Compartilhamento do progresso do trabalho', 'Atualização do backlog do sprint'],
        'answer': 'Compartilhamento do progresso do trabalho'
    },
    {
        'id': 4,
        'question': '4) Qual é uma das oportunidades importantes de inspeção no Scrum, onde a equipe reflete sobre o processo de trabalho e identifica melhorias?',
        'options': ['Reunião diária de stand-up', 'Planejamento do sprint', 'Análise de sprint', 'Retrospectiva do sprint'],
        'answer': 'Retrospectiva do sprint'
    },
    {
        'id': 5,
        'question': '5) O que permite que o Scrum responda de forma eficaz aos desafios e mudanças ao longo do ciclo de vida do projeto?',
        'options': ['Transparência', 'Inspeção',  'Adaptação', 'Todas as opções acima'],
        'answer': 'Todas as opções acima'
    },
    {
        'id': 6,
        'question': '6) Durante a adaptação no Scrum, que tipo de ajustes a equipe pode fazer no backlog do sprint?',
        'options': ['Alterações na estrutura das reuniões diárias', 'Adição ou remoção de tarefas com base no feedback do cliente', 'Revisão do progresso do trabalho', 'Definição de metas para o próximo sprint'],
        'answer': 'Adição ou remoção de tarefas com base no feedback do cliente'
    },
    {
        'id': 7,
        'question': '7) Qual é o objetivo principal das reuniões de revisão de sprint no Scrum?',
        'options': ['Selecionar itens para o backlog do sprint', 'Apresentar o trabalho concluído aos stakeholders', 'Identificar tendências preocupantes', 'Refletir sobre o processo de trabalho'],
        'answer': 'Apresentar o trabalho concluído aos stakeholders'
    },
    {
        'id': 8,
        'question': '8) O que é considerado um artefato central do Scrum que captura todas as funcionalidades, requisitos e correções desejadas para o produto em desenvolvimento?',
        'options': ['Reuniões diária de stand-up', 'Backlog do Sprint', 'Backlog do Produto', 'Retrospectiva do Sprint'],
        'answer': 'Backlog do Produto'
    },
    {
        'id': 9,
        'question': '9) Quando ocorre a inspeção do progresso e dos resultados no Scrum?',
        'options': ['Durante o planejamento do sprint', 'Nas reuniões diárias de stand-up', 'Na análise de sprint', 'Na retrospectiva do sprint'],
        'answer': 'Na análise de sprint'
    },
    {
        'id': 10,
        'question': '10) Por que a adaptabilidade é essencial para o sucesso do Scrum?',
        'options': ['Para garantir que todas as tarefas sejam concluídas dentro do prazo', 'Para responder eficazmente às mudanças no ambiente do projeto', 'Para manter a qualidade do produto', 'Para garantir a transparência em todas as atividades da equipe'],
        'answer': 'Para responder eficazmente às mudanças no ambiente do projeto'
    },
]

@app.route('/mod_2_quiz')
def modulo_2_quiz():
    return render_template('mod_2_quiz.html', questions=questions_2)

@app.route('/submit_quiz_2', methods=['POST'])
def submit_quiz_2():
    # Lógica para processar o formulário e verificar as respostas
    score = 0
    user_answers = {}
    for question in questions_2:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id)
        correct_answer = question['answer']
        if user_answer == correct_answer:
            score += 1
        user_answers[question['question']] = user_answer
    total_questions = len(questions_2)
    return render_template('mod_2_results.html', score=score, total_questions=total_questions, results=user_answers)

# Módulo 3

questions_3 = [
    {
        'id': 1,
        'question': '1) Qual das seguintes tarefas é uma responsabilidade do Product Owner?',
        'options': ['a)Codificar funcionalidades do produto.', 'b)Supervisionar o plano de lançamentos.', 'c)Executar testes de qualidade do produto.', 'd)Configurar o ambiente de desenvolvimento.'],
        'answer': 'b)Supervisionar o plano de lançamentos.'
    },
    {
        'id': 2,
        'question': '2) Qual é uma das principais responsabilidades do Scrum Master?',
        'options': ['Ditar regras para a equipe.', 'Ser o líder absoluto da equipe.', 'Garantir que a equipe siga as regras e valores do Scrum.', 'Tomar todas as decisões importantes no projeto.'],
        'answer': 'Garantir que a equipe siga as regras e valores do Scrum.'
    },
    {
        'id': 3,
        'question': '3) Qual é a principal responsabilidade do Development Team em um framework Scrum?',
        'options': ['Estimar o esforço necessário para cada item do Product Backlog.', 'Criar partes do produto que possam ser entregues ao final de cada Sprint.', 'Gerenciar o trabalho do Scrum Master.', 'Definir as metas da Sprint.'],
        'answer': 'Criar partes do produto que possam ser entregues ao final de cada Sprint.Criar partes do produto que possam ser entregues ao final de cada Sprint.'
    },
    {
        'id': 4,
        'question': '4) Qual das seguintes afirmações melhor descreve uma característica das equipes Scrum?',
        'options': ['As equipes Scrum têm posições fixas, onde cada membro desempenha sempre o mesmo papel em todos os projetos.', 'As equipes Scrum são autogerenciadas e possuem a capacidade de decidir como realizar o trabalho sem supervisão constante.', 'As equipes Scrum dependem fortemente de recursos externos para realizar suas tarefas, tornando-as menos ágeis.', 'As equipes Scrum são especializadas em uma única habilidade e não possuem versatilidade para realizar diferentes tarefas.'],
        'answer': 'As equipes Scrum são autogerenciadas e possuem a capacidade de decidir como realizar o trabalho sem supervisão constante.'
    },
    {
        'id': 5,
        'question': '5) Por que é importante que o Product Owner defina a visão do produto?',
        'options': ['Para garantir que todas as funcionalidades sejam implementadas.', 'Para comunicar claramente os requisitos aos desenvolvedores.',  'Para controlar o acesso ao Product Backlog.', 'Para decidir quando cancelar uma Sprint.'],
        'answer': 'Para comunicar claramente os requisitos aos desenvolvedores.'
    },
    {
        'id': 6,
        'question': '6) Como o Scrum Master lidera a equipe?',
        'options': ['Através do controle autoritário.', 'Estabelecendo regras rígidas.', 'Pelo exemplo e pelo conhecimento.', 'Ignorando as necessidades individuais dos membros da equipe.'],
        'answer': 'Pelo exemplo e pelo conhecimento.'
    },
    {
        'id': 7,
        'question': '7) Por que é importante que os Development Teams sejam do tamanho certo?',
        'options': ['Para maximizar o número de membros no time', 'Para facilitar a coordenação e colaboração.', 'Para aumentar a competitividade entre os membros.', ' Para permitir a intervenção externa mais eficaz.'],
        'answer': 'Para facilitar a coordenação e colaboração.'
    },
    {
        'id': 8,
        'question': '8) Quem tem a autoridade para aceitar ou rejeitar o trabalho concluído no final de cada ciclo de trabalho?',
        'options': [' O Scrum Master.', ' A equipe de desenvolvimento.', 'O Product Owner.', 'O cliente final.'],
        'answer': 'O Product Owner.'
    },
    {
        'id': 9,
        'question': '9) Qual é o papel do Scrum Master durante as reuniões do Scrum?',
        'options': ['Liderar todas as discussões.', 'Garantir que todos tenham a chance de falar e que as decisões sejam tomadas rapidamente.', ' Ignorar as contribuições dos membros da equipe.', '  Impor suas próprias opiniões e decisões aos outros.'],
        'answer': 'Garantir que todos tenham a chance de falar e que as decisões sejam tomadas rapidamente.'
    },
    {
        'id': 10,
        'question': '10) Qual dos seguintes estágios é visto como parte do desenvolvimento de um time auto-organizado no Scrum?',
        'options': ['Planejamento.', ' Execução.', ' Conflito.', 'Monitoramento.'],
        'answer': 'Conflito.'
    },
]

@app.route('/mod_3')
def modulo_3():
    return render_template('mod_3.html')

@app.route('/mod_3_quiz')
def modulo_3_quiz():
    return render_template('mod_3_quiz.html', questions=questions_3)

@app.route('/submit_quiz_3', methods=['POST'])
def submit_quiz_3():
    # Lógica para processar o formulário e verificar as respostas
    score = 0
    user_answers = {}
    for question in questions_3:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id)
        correct_answer = question['answer']
        if user_answer == correct_answer:
            score += 1
        user_answers[question['question']] = user_answer
    total_questions = len(questions_3)
    return render_template('mod_3_results.html', score=score, total_questions=total_questions, results=user_answers)

# Módulo 4

questions_4 = [
    {
        'id': 1,
        'question': '1) Qual é a função principal da Sprint Planning Meeting?',
        'options': ['Rever o progresso da Sprint.', 'Planejar as entregas em produção.', 'Planejar o trabalho a ser realizado durante a Sprint.', 'Coletar feedbacks do produto.'],
        'answer': 'Planejar o trabalho a ser realizado durante a Sprint.'
    },
    {
        'id': 2,
        'question': '2) Como é dividida a Sprint Planning Meeting em suas duas partes e quais são as perguntas que cada parte responde?',
        'options': ['Uma parte: Planejar o trabalho da Sprint; Segunda parte: Avaliar o progresso da Sprint.', 'Uma parte: O que será entregue?; Segunda parte: Como vamos entregar?', 'Uma parte: Estimar o tempo; Segunda parte: Coletar feedbacks do cliente.', 'Uma parte: Discutir problemas; Segunda parte: Resolver impedimentos.'],
        'answer': 'Uma parte: O que será entregue?; Segunda parte: Como vamos entregar?'
    },
    {
        'id': 3,
        'question': '3) Qual é o propósito da Daily Scrum e como ela beneficia o Time de Desenvolvimento?',
        'options': ['Reportar para o Scrum Master.', 'Sincronizar o trabalho e resolver impedimentos.', 'Revisar o progresso da Sprint.', 'Discutir questões técnicas.'],
        'answer': ' Sincronizar o trabalho e resolver impedimentos.'
    },
    {
        'id': 4,
        'question': '4) Quais são as três perguntas padrão que cada membro responde durante a Daily Scrum?',
        'options': ['O que fiz desde a última reunião, o que farei até a próxima e qual o meu cargo?', 'O que realizei desde a última Daily Scrum, quais são os meus planos até a próxima e houve algum obstáculo?', 'Quem impediu o meu progresso, o que realizei e o que planejo fazer?', 'O que realizei desde a última reunião, quem está com problemas e quem realizou mais tarefas?'],
        'answer': 'O que realizei desde a última Daily Scrum, quais são os meus planos até a próxima e houve algum obstáculo?'
    },
    {
        'id': 5,
        'question': '5) Quais são os objetivos da Sprint Review e quem participa dessa cerimônia?',
        'options': ['Rever o progresso da Sprint; Apenas o Scrum Master.', 'Inspecionar o produto e coletar feedbacks; Todos interessados no produto.', 'Resolver impedimentos; Apenas o Product Owner.', 'Definir a meta da Sprint; Apenas o Development Team.'],
        'answer': 'Inspecionar o produto e coletar feedbacks; Todos interessados no produto.'
    },
    {
        'id': 6,
        'question': '6) Qual é a importância da Sprint Retrospective e o que geralmente é discutido durante essa reunião?',
        'options': ['Identificar problemas e discutir sobre o próximo sprint; Técnicas de programação.', 'Rever o progresso da Sprint e discutir problemas pessoais; Avaliar o mercado.', 'Reflexão e melhoria contínua do processo; Interação entre os membros do time e práticas utilizadas.', 'Decidir os próximos passos do projeto; Revisão de documentos.'],
        'answer': 'Reflexão e melhoria contínua do processo; Interação entre os membros do time e práticas utilizadas.'
    },
    {
        'id': 7,
        'question': '7) O que é uma Release Planning Meeting e quando ela ocorre?',
        'options': ['Uma reunião para revisar o progresso da Sprint; No início de cada Sprint.', 'Uma reunião para planejar as entregas em produção; Ao final de uma Sprint.', 'Uma reunião para resolver impedimentos; Diariamente.', 'Uma reunião para revisar o Product Backlog; Mensalmente.'],
        'answer': 'Uma reunião para planejar as entregas em produção; Ao final de uma Sprint.'
    },
    {
        'id': 8,
        'question': '8) Por que é importante manter o período entre as Releases o mais curto possível?',
        'options': ['Para evitar reuniões longas.', 'Para aumentar a precisão do planejamento.', 'Para obter feedbacks mais rápidos e frequentes.', 'Para reduzir a participação dos membros do Time Scrum.'],
        'answer': 'Para obter feedbacks mais rápidos e frequentes.'
    },
    {
        'id': 9,
        'question': '9) Quais são os principais tópicos que podem ser incluídos em uma agenda para uma Release Planning Meeting?',
        'options': ['Revisão do propósito da reunião e estrutura; Discussão de problemas pessoais.', 'Apresentação de gráficos de status das últimas Sprints; Decisões sobre tecnologias a serem utilizadas.', 'Definição da meta para a Release; Montagem de gráficos de Release Burndown.', 'Discussão sobre o roadmap do produto; Revisão dos documentos legais.'],
        'answer': 'efinição da meta para a Release; Montagem de gráficos de Release Burndown.'
    },
    {
        'id': 10,
        'question': '10) Durante a Sprint Planning Meeting, quem apresenta os itens prioritários do Product Backlog ao Time Scrum?',
        'options': ['Scrum Master.', 'Product Owner.', 'Todos os membros do Time Scrum.', 'Development Team.'],
        'answer': 'Product Owner.'
    },
]

@app.route('/mod_4')
def modulo_4():
    return render_template('mod_4.html')

@app.route('/mod_4_quiz')  #altere apenas o número do seu módulo  )
def modulo_4_quiz():   #altere apenas o número do seu módulo          
    return render_template('mod_4_quiz.html', questions=questions_6)   #altere apenas o número do seu módulo

@app.route('/submit_quiz_4', methods=['POST'])  #altere apenas o número do seu módulo
def submit_quiz_4():  #altere apenas o número do seu módulo
    # Lógica para processar o formulário e verificar as respostas
    score = 0
    user_answers = {}
    for question in questions_4:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id)
        correct_answer = question['answer']
        if user_answer == correct_answer:
            score += 1
        user_answers[question['question']] = user_answer
    total_questions = len(questions_4)
    return render_template('mod_4_results.html', score=score, total_questions=total_questions, results=user_answers)

 # Módulo 5

questions_5 = [
    {
        'id': 1,
        'question': '1) O Product Backlog contém:',
        'options': ['a) Somente itens funcionais.', 'b) Itens priorizados apenas pelo Scrum Master.', 'c) Itens de negócios, funcionais, não funcionais, arquiteturais e de infraestrutura.', 'd) Itens sem critérios claros de aceitação.'],
        'answer': 'c) Itens de negócios, funcionais, não funcionais, arquiteturais e de infraestrutura.'
    },
    {
        'id': 2,
        'question': '2) Qual é o principal requisito para um Product Increment?',
        'options': ['a) Ser completamente perfeito.', 'b) Ser potencialmente entregável.', 'c) Ser aprovado pelo Scrum Master.', 'd) Ser entregue em cada Daily Scrum.'],
        'answer': 'b) Ser potencialmente entregável.'
    },
    {
        'id': 3,
        'question': '3) O que é o Sprint Backlog?',
        'options': ['a) Uma lista de tarefas organizadas por ordem alfabética.', 'b) Uma lista de itens selecionados para implementação durante a Sprint.', 'c) Uma lista de bugs identificados após o final da Sprint.', 'd) Uma lista de itens priorizados pelo Product Owner.'],
        'answer': 'b) Uma lista de itens selecionados para implementação durante a Sprint.'
    },
    {
        'id': 4,
        'question': '4) Qual é a função do Definition of Done (DoD)?',
        'options': ['a) Definir os itens que serão incluídos no Sprint Backlog.', 'b) Determinar quem é responsável por cada tarefa na Sprint.', 'c) Estabelecer critérios para uma funcionalidade ser considerada "pronta".', 'd) Gerenciar o Product Increment ao longo do tempo.'],
        'answer': 'c) Estabelecer critérios para uma funcionalidade ser considerada "pronta".'
    },
    {
        'id': 5,
        'question': '5) O que o Burndown Chart mostra visualmente?',
        'options': ['a) O número total de itens no Product Backlog', 'b) A quantidade de trabalho concluída a cada dia durante a Sprint.', 'c) A lista de itens a serem entregues no próximo Sprint.', 'd) O tempo estimado para cada tarefa no Sprint Backlog.'],
        'answer': 'b) A quantidade de trabalho concluída a cada dia durante a Sprint.'
    },
    {
        'id': 6,
        'question': '6) Quem é responsável por gerenciar o Product Backlog?',
        'options': ['a) O Scrum Master.', 'b) O Time de Desenvolvimento.', 'c) O Product Owner.', 'd) O Gerente de Projeto.'],
        'answer': 'c) O Product Owner.'
    },
    {
        'id': 7,
        'question': '7) Qual é o objetivo principal do Sprint Review?',
        'options': ['a) Analisar as métricas de produtividade da equipe.', 'b) Revisar e adaptar o processo de desenvolvimento.', 'c) Demonstrar o Product Increment e obter feedback.', 'd) Priorizar novos itens para o Product Backlog.'],
        'answer': 'c)Demonstrar o Product Increment e obter feedback.'
    },
    {
        'id': 8,
        'question': '8) Qual é a analogia mais adequada para descrever o Sprint Backlog?',
        'options': [' a) Uma lista de tarefas em um buffet de ideias.', 'b) Um mapa de tesouro com objetivos para explorar.', 'c) Um álbum de figurinhas colecionáveis para completar.', 'd) Uma caixa de ferramentas com os recursos necessários para construir algo incrível.'],
        'answer': 'd) Uma caixa de ferramentas com os recursos necessários para construir algo incrível.'
    },
    {
        'id': 9,
        'question': '9) Qual seria uma comparação criativa para ilustrar a função do Burndown Chart?',
        'options': ['a) Um cronômetro em uma corrida de revezamento.', 'b) Um mapa de navegação em uma viagem de exploração.', 'c) Um termômetro que mede o progresso do projeto.', 'd) Uma linha do tempo em uma história em quadrinhos.'],
        'answer': 'c) Um termômetro que mede o progresso do projeto.'
    },
    {
        'id': 10,
        'question': '10) Qual é o principal objetivo da Sprint Planning para o Scrum Team?',
        'options': ['a) Definir metas pessoais para cada membro da equipe.', 'b) Revisar e ajustar o Product Backlog.', 'c) Estabelecer uma lista de tarefas para cada membro da equipe.', 'd) Planejar o trabalho a ser realizado durante a próxima Sprint.'],
        'answer': 'd) Planejar o trabalho a ser realizado durante a próxima Sprint.'
    },
]
@app.route('/mod_5')
def modulo_5():
    return render_template('mod_5.html')

@app.route('/mod_5_quiz')
def modulo_5_quiz():
    return render_template('mod_5_quiz.html', questions=questions_5)

@app.route('/submit_quiz_5', methods=['POST'])
def submit_quiz_5():
    # Lógica para processar o formulário e verificar as respostas
    score = 0
    user_answers = {}
    for question in questions_5:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id)
        correct_answer = question['answer']
        if user_answer == correct_answer:
            score += 1
        user_answers[question['question']] = user_answer
    total_questions = len(questions_5)
    return render_template('mod_5_results.html', score=score, total_questions=total_questions, results=user_answers)

#Módulo 6

questions_6 = [ #question_<seu módulo>
    {
        'id': 1, #id segue padrão para todas
        'question': '1) Qual é a base da auto-organização no Scrum?', #coloque sua pergunta aqui
        'options': ['Instruções detalhadas', 'Microgerenciamento', 'Confiança mútua e clareza dos objetivos do projeto', 'Autoritarismo', 'Delegação excessiva'], #bote as opções de resposta
        'answer': 'Confiança mútua e clareza dos objetivos do projeto' #insira a resposta certa 
    },
    {
        'id': 2,
        'question': '2) O que a auto-organização promove nas equipes ágeis?',
        'options': ['Conformidade', 'Individualismo', 'Colaboração', 'Resistência à mudança', 'Competição'],
        'answer': 'Colaboração'
    },
    {
        'id': 3,
        'question': '3) Qual é uma das responsabilidades do Scrum Master?',
        'options': ['Promover o engajamento', 'Ditar as tarefas da equipe', 'Resolver todos os conflitos', 'Focar apenas nos resultados', 'Delegação excessiva'],
        'answer': 'Promover o engajamento'
    },
    {
        'id': 4,
        'question': '4) O que são User Stories em metodologias ágeis?',
        'options': ['Grandes descrições de funcionalidades', 'Requisitos escritos apenas pelo Product Owner', ' Histórias irrelevantes', 'Documentos detalhados e rígidos', 'Pequenas descrições de funcionalidades'],
        'answer': 'Pequenas descrições de funcionalidades'
    },
    {
        'id': 5,
        'question': '5) Qual é um dos benefícios da auto-organização?',
        'options': ['Microgerenciamento eficiente', 'Colaboração ativa', 'Resistência à mudança', 'Conformidade absoluta', ' Falta de autonomia'],
        'answer': 'Promover o engajamento'
    },
    {
        'id': 6,
        'question': '6) Qual é uma das funções do Scrum Master como facilitador?',
        'options': ['Aumentar os conflitos na equipe', 'Minimizar a comunicação entre os membros', 'Ignorar as necessidades dos stakeholders', 'Otimizar os processos de trabalho', 'Incentivar a competição entre os membros'],
        'answer': 'Otimizar os processos de trabalho'
    },
    {
        'id': 7,
        'question': '7) O que é a visão do produto em metodologias ágeis?',
        'options': ['Uma declaração clara dos métodos de desenvolvimento', 'Um documento rígido com requisitos detalhados', 'Uma declaração dos objetivos e valores do produto', ' Uma descrição dos recursos do produto', 'Um plano de projeto estático'],
        'answer': 'Uma declaração dos objetivos e valores do produto'
    },
    {
        'id': 8,
        'question': '8) Qual é a importância dos critérios de aceitação em User Stories?',
        'options': ['Determinar o tamanho da história', 'Garantir que a história seja implementada', 'Avaliar o desempenho do Scrum Master', 'Controlar o escopo do projeto', 'Promover a inovação na equipe'],
        'answer': 'Garantir que a história seja implementada'
    },
    {
        'id': 9,
        'question': '9) Qual é um dos elementos principais de uma User Story?',
        'options': ['Código-fonte', ' Estrutura de dados', 'Diagrama de Gantt', ' Lista de tarefas', ' Who, What, Why'],
        'answer': ' Who, What, Why'
    },
    {
        'id': 10,
        'question': '10) Qual é o papel do Product Owner em relação à visão do produto?',
        'options': ['Criar a visão do produto sozinho', 'Desenvolver a visão do produto durante a Sprint Planning', 'Transmitir a visão do produto para a equipe', ' Ignorar a visão do produto após sua criação', 'Promover a competição entre os membros da equipe'],
        'answer': 'Transmitir a visão do produto para a equipe'
    },
]

@app.route('/mod_6') #seu módulo normal
def modulo_6():
    return render_template('mod_6.html')

@app.route('/mod_6_quiz')  #altere apenas o número do seu módulo  )
def modulo_6_quiz():   #altere apenas o número do seu módulo          
    return render_template('mod_6_quiz.html', questions=questions_6)   #altere apenas o número do seu módulo

@app.route('/submit_quiz_6', methods=['POST'])  #altere apenas o número do seu módulo
def submit_quiz_6():  #altere apenas o número do seu módulo
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
    return render_template('mod_6_results.html', score=score, total_questions=total_questions, results=user_answers) #altere apenas o número do seu módulo no (mod_x_results.html)


#Módulo 7
questions_7 = [
        {
        'id': 1,
        'question': '1) Qual é o principal objetivo do Planning Poker no SCRUM?',
        'options': ['Determinar quem são os membros mais rápidos da equipe.', 'Estabelecer um consenso sobre o esforço necessário para as tarefas.','Aumentar a competição entre os membros da equipe.', 'Acelerar o processo de desenvolvimento de software.','Identificar os membros da equipe que precisam de treinamento adicional.'],
        'answer': 'Estabelecer um consenso sobre o esforço necessário para as tarefas.'
    },
    {
        'id': 2,
        'question': '2) O que os membros da equipe de desenvolvimento fazem durante uma sessão de Planning Poker?',
        'options': ['Estimam o esforço necessário para as tarefas.', 'Supervisionam o processo de estimativa.', 'Fornecem feedback sobre o progresso do projeto.', 'Decidem quais tarefas devem ser priorizadas.','Definem os requisitos das tarefas a serem estimadas.'],
        'answer': 'Estimam o esforço necessário para as tarefas.'
    },
    {
        'id': 3,
        'question': '3) O que um número baixo em uma rodada de Planning Poker sugere sobre a tarefa em questão?',
        'options': ['Que a tarefa será rápida e fácil de concluir.', 'Que a tarefa pode ser complexa e necessitará de mais análise.', 'Que a tarefa não está claramente definida e precisa de mais informações.', 'Que a tarefa é crítica para o sucesso do projeto.','Que a tarefa pode ser adiada para uma iteração futura.'],
        'answer': 'Que a tarefa pode ser complexa e necessitará de mais análise.'
    },
    {
        'id': 4,
        'question': '4)  Qual é a vantagem de utilizar a técnica de Planning Poker para estimativas? ',
        'options': ['Maior precisão nas estimativas e engajamento da equipe.', 'Redução da colaboração entre os membros da equipe', 'Redução do tempo de desenvolvimento e aumento do custo.', 'Aumento da competição entre os membros da equipe.','Diminuição da comunicação entre os membros da equipe.','Aumento da incerteza sobre o progresso do projeto.'],
        'answer': 'Maior precisão nas estimativas e engajamento da equipe.'
    },
    {
        'id': 5,
        'question': '5) O que é importante fazer após uma rodada de Planning Poker para alcançar um consenso na equipe?',
        'options': ['Descartar as estimativas mais baixas e mais altas.', 'Selecionar a média das estimativas fornecidas.', 'Atribuir a tarefa ao membro da equipe com a estimativa mais alta.', 'Ignorar todas as estimativas e decidir arbitrariamente o esforço necessário.','Realizar outra rodada de votação até que haja um consenso unânime.'],
        'answer': 'Selecionar a média das estimativas fornecidas.'
    },
    {
        'id': 6,
        'question': '6) Qual é a principal vantagem de usar cartas com valores discretos no Planning Poker?',
        'options': ['Facilita a comunicação e compreensão das estimativas.', 'Torna o processo mais complicado e demorado.', 'Reduz a necessidade de interação entre os membros da equipe.', ' Aumenta a probabilidade de conflitos durante a estimativa.',' Facilita a manipulação das estimativas para atender aos interesses pessoais.'],
        'answer': 'Facilita a comunicação e compreensão das estimativas.'
    },
    {
        'id': 7,
        'question': '7) Como o Planning Poker ajuda a evitar a influência de vieses individuais nas estimativas?',
        'options': ['Atribuindo um peso maior às estimativas dos membros mais experientes.', 'Limitando a participação na estimativa apenas aos membros mais antigos da equipe.', 'Encorajando discussões abertas e anônimas durante o processo de estimativa.', ' Ignorando as opiniões dos membros menos experientes.','Permitindo que apenas o Product Owner faça as estimativas.'],
        'answer': 'Encorajando discussões abertas e anônimas durante o processo de estimativa.'
    },
    {
        'id': 8,
        'question': '8) Quando é apropriado realizar uma rodada de reestimativa durante o desenvolvimento de um projeto SCRUM?',
        'options': ['Sempre que a equipe de desenvolvimento quiser mudar as estimativas.', 'Apenas quando o Product Owner solicitar uma nova estimativa.', 'Quando uma tarefa estimada excede o tempo planejado.', 'Antes de cada sprint, independentemente do progresso.','Quando uma tarefa é concluída antes do tempo previsto.'],
        'answer': 'Quando uma tarefa estimada excede o tempo planejado.'
    },
    {
        'id': 9,
        'question': '9) Como a técnica de Planning Poker promove a transparência no processo de desenvolvimento do SCRUM?',
        'options': ['Mantendo todas as estimativas em sigilo até o final do projeto.', 'Incentivando a comunicação aberta e honesta entre os membros da equipe.', 'Limitando a participação na estimativa apenas aos membros mais antigos da equipe.', ' Ocultando as estimativas dos clientes e partes interessadas externas.','Designando um único membro da equipe como responsável por todas as estimativas.'],
        'answer': 'Incentivando a comunicação aberta e honesta entre os membros da equipe.'
    },
    {
        'id': 10,
        'question': '10) Qual é o principal objetivo do Scrum Master durante uma sessão de Planning Poker? ',
        'options': ['Fornecer estimativas precisas para todas as tarefas do backlog.', 'Garantir que todas as estimativas sejam idênticas para evitar conflitos.', 'Facilitar o processo de estimativa e remover obstáculos.','Tomar todas as decisões relacionadas à priorização das tarefas.','Monitorar o progresso do projeto sem se envolver nas estimativas.'],
        'answer': 'Facilitar o processo de estimativa e remover obstáculos.'
    },
]

@app.route('/mod_7')
def modulo_7():
    return render_template('mod_7.html')

@app.route('/mod_7_quiz')
def modulo_7_quiz():
    return render_template('mod_7_quiz.html', questions=questions_7)

@app.route('/submit_quiz_7', methods=['POST'])
def submit_quiz_7():
    # Lógica para processar o formulário e verificar as respostas
    score = 0
    user_answers = {}
    for question in questions_7:
        question_id = str(question['id'])
        user_answer = request.form.get(question_id)
        correct_answer = question['answer']
        if user_answer == correct_answer:
            score += 1
        user_answers[question['question']] = user_answer
    total_questions = len(questions_7)
    return render_template('mod_7_results.html', score=score, total_questions=total_questions, results=user_answers)
