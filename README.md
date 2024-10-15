# aula-python
O que preciso instalado no meu computador:

- Linguagem:
Python 3.9 ou superior https://www.python.org/downloads/windows/
- IDE:
Pycharm https://www.jetbrains.com/pt-br/pycharm/download
ou VS Code https://code.visualstudio.com/download
- Versionamento:
Git https://git-scm.com/downloads

# Como rodar o projeto na sua maquina local:

- Passo 1: fazer o clone com git
    - abrir uma pasta do seu pc no terminal e executar no terminal o comando: git clone https://github.com/cleberleao/aula-python.git
* Passo 2: abrir o projeto com a IDE de preferência
    - criar a venv no terminal windows: py -m venv venv
    - criar a venv no terminal linux: python -m venv venv
    - ativar a venv no terminal windows: .\venv\Scripts\activate
    - ativar a venv no terminal linux: source venv/Scripts/activate
    - navegar via terminal na IDE até chegar na pasta onde está o requirements.txt
    - executar no terminal o comando: pip install -r requirements.txt
    - executar o comando no terminal para subir o servidor: py manage.py runserver (linux use python no lugar de py)
- Se tudo deu certo vai aparecer na sua IDE a url do projeto: http://127.0.0.1:8000/
* agora é com voce:
    - Fazer um CRUD de um tema diferente do "Members" com as paginas:
      - Home
      - Listar todos cadastros
      - Cadastar o item
      - Editar o item do cadastro
      - Excluir o item do cadastro