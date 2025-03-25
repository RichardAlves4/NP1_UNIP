print("Bem-vindo ao nosso site.")

def verifica_user():
    estado_verifica_user = False

    while not estado_verifica_user:
        menu_verifica_user = input("Digite:\n\n\"A\" Para acesso a área do aluno\n\"P\" Para acesso a área do professor\n\"E\" Para Sair\n").upper()

        if menu_verifica_user not in ["A", "a", "P", "p", "E", "e"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_verifica_user == "A" or menu_verifica_user == "a":
            aluno()
        elif menu_verifica_user == "P" or menu_verifica_user == "p":
            professor()
        elif menu_verifica_user == "E" or menu_verifica_user == "e":
            print("Saiu!")
            break

def aluno():
    estado_aluno = False
    
    print("Bem-vindo Aluno")

    while not estado_aluno:
        acao_aluno = str(input("Digite \"C\" para Cadastrar-se, \"L\" para acessar sua conta ou aperte \"E\" para voltar\n")).upper()
        
        if acao_aluno not in ["C", "c", "L", "l", "E", "e"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if acao_aluno == "C" or acao_aluno == "c":
            estado_aluno = True
            cadastro_aluno()
        elif acao_aluno == "L" or acao_aluno == "l":
            estado_aluno = True
            login_aluno()
        elif acao_aluno == "E" or acao_aluno == "e":
            print("Voltar!")
            return        

def professor():
    estado_professor = False

    print("Bem-vindo Professor")

    while not estado_professor:
        acao_professor = str(input("Digite \"C\" para Cadastrar-se, \"L\" para acessar sua conta ou aperte \"E\" para voltar\n")).upper()
        
        if acao_professor not in ["C", "c", "L", "l", "E", "e"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if acao_professor == "C" or acao_professor == "c":
            estado_professor = True
            cadastro_professor()
        elif acao_professor == "L" or acao_professor == "l":
            estado_professor = True
            login_professor()
        elif acao_professor == "E" or acao_professor == "e":
            print("Voltar!")
            return

def cadastro_aluno():
    print("\nCadastro de Alunos\n")
    
    while True:
        email_aluno = str(input("Informe seu melhor email: "))
        
        if not email_aluno.endswith("@gmail.com"):
            print("\nE-mail inválido! Certifique-se de usar um endereço @gmail.com.\n")
            continue
            
        while True:
            senha_aluno = str(input("Informe uma senha forte: "))
            repet_senha_aluno = str(input("Repita sua senha: "))

            if senha_aluno == repet_senha_aluno:
                login_aluno(email_aluno, senha_aluno)
                return   
            else:
                print("\nSenha incorreta! Tente novamente\n")

def cadastro_professor():
    print("\nCadastro de Professores\n")
    
    while True:
        email_professor = str(input("Informe seu melhor email: "))
        
        if not email_professor.endswith("@gmail.com"):
            print("\nE-mail inválido! Certifique-se de usar um endereço @gmail.com.\n")
            continue
            
        while True:
            senha_professor = str(input("Informe uma senha forte: "))
            repet_senha_professor = str(input("Repita sua senha: "))

            if senha_professor == repet_senha_professor:
                login_professor(email_professor, senha_professor)
                return 
            else:
                print("\nSenha incorreta! Tente novamente\n")

def login_aluno(email_cadastrado_aluno, senha_cadastrada_aluno):
    print("\nEntrar como aluno\n")

    while True:
        email_login_aluno = str(input("Email: "))
        senha_login_aluno = str(input("Senha: "))

        if email_login_aluno == email_cadastrado_aluno and senha_login_aluno == senha_cadastrada_aluno:
            main_aluno()
            break
        else:
            print("Email ou senha incorretos! Tente novamente")
                    
def login_professor(email_cadastrado_professor, senha_cadastrada_professor):
    print("\nEntrar como professor\n")

    while True:
        email_login_professor = str(input("Email: "))
        senha_login_professor = str(input("Senha: "))

        if email_login_professor == email_cadastrado_professor and senha_login_professor == senha_cadastrada_professor:
            main_professor()
            break
        else:
            print("Email ou senha incorretos! Tente novamente")

def main_aluno():
    estado_main_aluno = False

    while not estado_main_aluno:
        print("Bem-vindo aluno! ao site da Escola")
        menu_main_aluno = input("Digite:\n\n\"P\" Para acessar a prova\n\"R\" Para acessar sua nota\n\"E\" Para desconectar\n").upper()

        if menu_main_aluno not in ["P", "p", "R", "r", "E", "e"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_main_aluno == "P" or menu_main_aluno == "p":
            avaliacao()
        elif menu_main_aluno == "R" or menu_main_aluno == "r":
            avaliacao_resultado()
        elif menu_main_aluno == "E" or menu_main_aluno == "e":
            print("Desconectar!")
            break

def main_professor():
    estado_main_professor = False

    while not estado_main_professor:
        print("Bem-vindo professor! ao site da Escola")
        menu_main_professor = input("Digite:\n\n\"P\" Para acessar a prova\n\"R\" Para acessar sua nota\n\"E\" Para desconectar\n").upper()

        if menu_main_professor not in ["R", "r", "E", "e"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_main_professor == "R" or menu_main_professor == "r":
            avaliacao_resultado()
        elif menu_main_professor == "E" or menu_main_professor == "e":
            print("Desconectar!")
            break

def avaliacao():
    print("\nAqui será a avaliação do aluno...\n")

def avaliacao_resultado():
    print("rpre")

verifica_user()