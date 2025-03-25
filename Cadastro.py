print("Bem-vindo ao nosso site.")

def verifica_user():
    estado_verifica_user = False

    while not estado_verifica_user:
        cadastro = input("Digite:\n\n\"A\" Para acesso a área do aluno\n\"P\" Para acesso a área do professor\n\"E\" Para Sair\n").upper()

        if cadastro not in ["A", "a", "P", "p", "E", "e"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if cadastro == "A" or cadastro == "a":
            aluno()
        elif cadastro == "P" or cadastro == "p":
            professor()
        elif cadastro == "E" or cadastro == "e":
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
                login_professor()
                return repet_senha_professor
            else:
                print("\nSenha incorreta! Tente novamente\n")

def login_aluno(email_cadastrado, senha_cadastrada):
    print("\nEntrar como aluno\n")

    while True:
        email_login_aluno = str(input("Email: "))
        senha_login_aluno = str(input("Senha: "))

        if email_login_aluno == email_cadastrado and senha_login_aluno == senha_cadastrada:
            avaliacao()
            break
        else:
            print("Email ou senha incorretos! Tente novamente")
            

def login_professor():
    print("vjhn mh")

def avaliacao():
    print("\nAqui será a avaliação do aluno...\n")

def avaliacao_resultado():
    print("rpre")

verifica_user()