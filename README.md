# Sistema de Gestão de Ensino (Skills Manager)

Este projeto é uma aplicação web desenvolvida em Python utilizando o framework Flask. O sistema foi desenhado para facilitar a gestão académica de uma instituição de ensino, permitindo o controlo centralizado de turmas, alunos, professores e atividades avaliativas.

A arquitetura do projeto segue o padrão MVC (Model-View-Controller), garantindo uma organização clara entre a lógica de negócio, a interface do utilizador e a gestão de dados.

<div align="center"> <img width="1160" height="550" alt="Screenshot 2025-11-28 121515" src="https://github.com/user-attachments/assets/6c543d0b-3c2d-402f-8146-ca9a9fc35889" /> </div>

## Contexto Académico
Este software foi desenvolvido como parte dos requisitos do 6º período de Engenharia de Software na Unisenai, para a disciplina de Backend Development.

## Funcionalidades Principais

O sistema possui um controlo de acesso baseado em cargos (Role-Based Access Control), dividindo as funcionalidades entre Administradores e Professores.

    Nota: O sistema é de gestão interna. Os alunos não possuem acesso direto (login); os seus dados, entregas e notas são geridos exclusivamente pelos administradores e professores.

## Acesso e Segurança

    Autenticação: Sistema de login e registo seguro com hash de senhas (via Bcrypt).

    Códigos de Verificação: O registo de novos administradores ou professores é restrito e exige um código de validação específico para cada cargo, garantindo que apenas pessoal autorizado se cadastre.

    Gestão de Sessão: O sistema mantém o utilizador logado e suporta a funcionalidade de "Lembrar senha".

### Tela de Registro
<div align="center"> <img width="725" height="650" alt="Screenshot 2025-11-28 121705" src="https://github.com/user-attachments/assets/055b1cb3-3e89-4a62-b992-06b931022971" /> </div>

## Painel do Administrador

O administrador tem a visão global da instituição e gere a estrutura base:

    Gestão de Professores: Visualizar a lista de docentes e remover acessos quando necessário.

    Gestão de Turmas: Criar, editar e remover turmas, além de associar os professores responsáveis a cada uma delas.

    Gestão de Alunos: Cadastrar novos alunos, editar informações e gerir a sua alocação nas turmas.

    Monitorização: Acesso aos detalhes de desempenho dos alunos, visualizando as notas atribuídas pelos professores em diferentes atividades.

### Tela de Gerenciamento de Turmas
<div align="center"> <img width="1100" height="450" alt="Screenshot 2025-11-28 121928" src="https://github.com/user-attachments/assets/99aeed12-31e5-4b32-8071-0d7fa0c9e22f" /> </div>

### Tela de Criação de um Novo Estudante
<div align="center"> <img width="570" height="450" alt="Screenshot 2025-11-28 123028" src="https://github.com/user-attachments/assets/0576d4d7-1ecd-44f8-98c5-f186d6b0689d" /> </div>

## Painel do Professor

O professor gere o conteúdo académico das turmas às quais está vinculado:

    Gestão de Tarefas (Assignments):

        Criação de novas tarefas com definição de nome, valor (nota) e data de entrega.

        Upload de Ficheiros: Possibilidade de anexar enunciados ou materiais de apoio (PDF) às tarefas.

        Edição e remoção de tarefas existentes.

    Lançamento de Notas: Interface dedicada para atribuir e atualizar as notas dos alunos em cada atividade específica.

    Relatórios de Turma: Visualização do progresso dos alunos da sua turma.

### Tela Inicial do Professor (Turmas Vinculadas)
<div align="center"> <img width="1100" height="465" alt="Screenshot 2025-11-28 122040" src="https://github.com/user-attachments/assets/869b24fe-3e70-417a-aecf-c513ab2fb078" /> </div>

### Tela Detalhada da Turma
<div align="center"> <img width="1080" height="705" alt="Screenshot 2025-11-28 122242" src="https://github.com/user-attachments/assets/f0be4459-1ebd-4ae5-9bce-89b51b1d212f" /> </div>

### Tela para Avaliação de uma Atividade
<div align="center"> <img width="760" height="390" alt="Screenshot 2025-11-28 122305" src="https://github.com/user-attachments/assets/b2af0e01-80d4-42ef-8bd0-965702fb5fea" /> </div>

### Tela para Observar o Desenpenho do Aluno
<div align="center"> <img width="1070" height="580" alt="Screenshot 2025-11-28 122852" src="https://github.com/user-attachments/assets/5246e13f-5b3e-468f-a651-12312ac27778" /> </div>

## API Integrada

O backend disponibiliza endpoints que retornam dados em formato JSON, permitindo a consulta programática de:

    Listagem de Turmas e Alunos.

    Detalhes das Tarefas (Assignments).

    Informações dos Professores. Esta estrutura facilita futuras integrações ou o desenvolvimento de novos frontends.

### Teste da API que Retorna Todos os Estudantes
<div align="center"> <img width="495" height="350" alt="image" src="https://github.com/user-attachments/assets/d5200262-916a-4541-b511-38502a4198c0" /> </div>


## Tecnologias Utilizadas

O núcleo do projeto é focado no desenvolvimento Backend robusto e modular:

    Linguagem: Python 3

    Framework Web: Flask (seguindo arquitetura MVC)

    Base de Dados: PostgreSQL (via SQLAlchemy ORM)

    Segurança: Flask-Bcrypt (Hashing de senhas)

    Uploads: Gestão segura de ficheiros (PDFs)

    Frontend: HTML5, CSS3 (Bootstrap) e Jinja2 para renderização de templates.

## Como Executar o Projeto

Siga os passos abaixo para colocar o sistema a funcionar no seu ambiente local.

Pré-requisitos

    Python 3.x instalado.

    PostgreSQL instalado e configurado (ou ajuste para outro banco de dados no ficheiro de configuração).

Instalação

    Instalar as dependências:
    Bash

pip install -r requirements.txt

Configurar Variáveis de Ambiente: Crie um ficheiro .env na raiz do projeto com as configurações do banco de dados e as chaves de segurança (baseado no config.py e project_model.txt):
Snippet de código

## Configuração da Base de Dados
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco

## Códigos de Registo (Defina os seus)
TEACHER_REGISTER_CODE=123
ADMIN_REGISTER_CODE=456

Inicializar a Base de Dados e Executar: O sistema irá criar as tabelas automaticamente na primeira execução.
Bash

    python app.py

    Aceder: Abra o navegador em http://127.0.0.1:5000.

📂 Estrutura do Projeto

    controllers/: Contém a lógica das rotas (Blueprints) para Admin, Professor, Utilizador e API.

    models/: Definição das tabelas da base de dados (Classes ORM).

    view/templates/: Ficheiros HTML (Jinja2) da interface do utilizador.

    uploads/: Diretório onde os ficheiros das tarefas são armazenados.

    utils/: Funções auxiliares e decoradores de segurança.
