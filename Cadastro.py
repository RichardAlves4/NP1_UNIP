import bcrypt
import json

arquivo_json = "usuarios.json"

usuarios_alunos = {}
usuarios_professores = {}

def carregar_usuarios():

    global usuarios_alunos, usuarios_professores
    try:
        with open(arquivo_json,"r") as json_aberto:
            dados = json.load(json_aberto)
            usuarios_alunos = dados.get("alunos", {})
            usuarios_professores  = dados.get("professores", {})
    except FileNotFoundError:
        print("Arquivo \"usuarios.json\" não encotrado. Gerando novo arquivo...")

def salvar_usuarios():
    with open(arquivo_json, "w") as json_aberto:
        json.dump({"alunos":usuarios_alunos, "professores":usuarios_professores}, json_aberto, indent= 4)

def criptografar_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt).decode()

def verificar_senha(senha_digitada, senha_armazenada):
    return bcrypt.checkpw(senha_digitada.encode(), senha_armazenada.encode())

carregar_usuarios()

print("Bem-vindo ao nosso site.")

def verifica_user():
    estado_verifica_user = False

    while not estado_verifica_user:
        menu_verifica_user = input("Digite:\n\n\"A\" Para acesso a área do aluno\n\"P\" Para acesso a área do professor\n\"E\" Para Sair\n").upper()

        if menu_verifica_user not in ["A", "P", "E",]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_verifica_user == "A":
            aluno()
        elif menu_verifica_user == "P":
            professor()
        elif menu_verifica_user == "E":
            print("Saiu!")
            break

def aluno():
    estado_aluno = False
    
    print("Bem-vindo Aluno")

    while not estado_aluno:
        acao_aluno = str(input("Digite \"C\" para Cadastrar-se, \"L\" para acessar sua conta ou aperte \"E\" para voltar\n")).upper()
        
        if acao_aluno not in ["C", "L", "E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if acao_aluno == "C":
            estado_aluno = True
            cadastro_aluno()
        elif acao_aluno == "L":
            estado_aluno = True
            login_aluno()
        elif acao_aluno == "E":
            print("Voltar!")
            return        

def professor():
    estado_professor = False

    print("Bem-vindo Professor")

    while not estado_professor:
        acao_professor = str(input("Digite \"C\" para Cadastrar-se, \"L\" para acessar sua conta ou aperte \"E\" para voltar\n")).upper()
        
        if acao_professor not in ["C", "L", "E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if acao_professor == "C":
            estado_professor = True
            cadastro_professor()
        elif acao_professor == "L":
            estado_professor = True
            login_professor()
        elif acao_professor == "E":
            print("Voltar!")
            return

def cadastro_aluno():
    print("\nCadastro de Alunos\n")
    
    while True:

        nome_aluno = (input("Informe seu nome: ")).strip().title()
        email_aluno = (input("Informe seu melhor email: ")).strip().lower()
        
        if not email_aluno.endswith("@gmail.com"):
            print("\nE-mail inválido! Certifique-se de usar um endereço @gmail.com.\n")
            continue

        if email_aluno in usuarios_alunos:
            print("Usuário já cadastrado")
            continue

        while True:
                idade_aluno = int(input("Informe sua idade: ").strip())
                if idade_aluno < 7:
                    print("\nIdade inválida! Tente novamente.\n")
                    continue
                else:
                    break
            
        while True:
            senha_aluno = (input("Informe uma senha forte: ")).strip()
            repet_senha_aluno = (input("Repita sua senha: ")).strip()

            if senha_aluno == repet_senha_aluno:
                senha_criptografada = criptografar_senha(senha_aluno)
                usuarios_alunos[email_aluno] = {
                    "nome": nome_aluno,
                    "idade": idade_aluno,
                    "senha": senha_criptografada
                } 
                salvar_usuarios()
                print("\nCadastro realizado com sucesso!\n")
                return
            else:
                print("\nSenha incorreta! Tente novamente\n")

def cadastro_professor():
    print("\nCadastro de Professores\n")
    
    while True:

        nome_professor = str(input("Informe o seu nome: ")).strip().title()
        email_professor = str(input("Informe seu melhor email: ")).strip()
        
        if not email_professor.endswith("@gmail.com"):
            print("\nE-mail inválido! Certifique-se de usar um endereço @gmail.com.\n")
            continue

        if email_professor in usuarios_professores:
            print("Usuário já cadastrado")
            continue

        while True:
            idade_professor = int(input("Informe sua idade: ").strip())
            if idade_professor < 18:
                print("\nIdade inválida! Tente novamente.\n")
                continue
            else:
                break
            
        while True:
            senha_professor = str(input("Informe uma senha forte: ")).strip()
            repet_senha_professor = str(input("Repita sua senha: ")).strip()

            if senha_professor == repet_senha_professor:
                senha_criptografada = criptografar_senha(senha_professor)
                usuarios_professores[email_professor] = {
                    "nome": nome_professor,
                    "idade": idade_professor,
                    "senha": senha_criptografada
                }
                salvar_usuarios()
                print("\nCadastro realizado com sucesso!\n")
                return
            else:
                print("\nSenha incorreta! Tente novamente\n")

def login_aluno():
    print("\nEntrar como aluno\n")

    while True:
        email_aluno = str(input("Email: ")).strip().lower()
        senha_aluno = str(input("Senha: ")).strip()

        if email_aluno in usuarios_alunos:
            senha_armazenada = usuarios_alunos[email_aluno]["senha"]
        if verificar_senha(senha_aluno, senha_armazenada):
            print(f"\nBem-vindo, {usuarios_alunos[email_aluno]['nome']}!")
            main_aluno()
            break
        print("Email ou senha incorretos! Tente novamente")
                    
def login_professor():
    print("\nEntrar como professor\n")

    while True:
        email_professor = str(input("Email: ")).strip().lower()
        senha_professor = str(input("Senha: ")).strip()

        if email_professor in usuarios_professores:
            senha_armazenada = usuarios_professores[email_professor]["senha"]
        if verificar_senha(senha_professor, senha_armazenada):
            print(f"\nBem-vindo, {usuarios_professores[email_professor]['nome']}!")
            main_professor()
            break
        print("Email ou senha incorretos! Tente novamente")

def main_aluno():
    estado_main_aluno = False

    while not estado_main_aluno:
        menu_main_aluno = input("Digite:\n\n\"P\" Para acessar a prova\n\"R\" Para acessar sua nota\n\"E\" Para desconectar\n").upper()

        if menu_main_aluno not in ["P","R","E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_main_aluno == "P":
            avaliacao()
        elif menu_main_aluno == "R":
            avaliacao_resultado()
        elif menu_main_aluno == "E":
            print("Desconectar!")
            break

def main_professor():
    estado_main_professor = False

    while not estado_main_professor:
        menu_main_professor = input("Digite:\n\n\"P\" Para acessar a prova\n\"R\" Para acessar sua nota\n\"E\" Para desconectar\n").upper()

        if menu_main_professor not in ["R", "E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_main_professor == "R":
            avaliacao_resultado()
        elif menu_main_professor == "E":
            print("Desconectar!")
            break

def avaliacao():
    print("\nAqui será a avaliação do aluno...\n")

def avaliacao_resultado():
    print("rpre")

verifica_user()