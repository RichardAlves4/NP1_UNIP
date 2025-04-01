import bcrypt
import json

arquivo_json = "usuarios.json"

usuarios_alunos = {}
usuarios_professores = {}

questoes = [
    {"pergunta": "1. Qual é a saída do seguinte código?\nprint(2 + 3 * 4)", "opcoes": ["A) 20", "B) 14", "C) 24", "D) 10"], "resposta": "B", "valor": 1},
    {"pergunta": "2. Qual dessas opções representa um comentário em Python?", "opcoes": ["A) // Isso é um comentário", "B) <!-- Isso é um comentário -->", "C) # Isso é um comentário", "D)  /* Isso é um comentário */"], "resposta": "C", "valor": 1},
    {"pergunta": "3. Qual é a função usada para exibir algo na tela em Python?", "opcoes": ["A) display()", "B) echo()", "C) print()", "D) show()"], "resposta": "C", "valor": 1},
    {"pergunta": "4. O que acontece se tentarmos executar este código?\nx = 10\nif x > 5:\n    print(\"Maior que 5\")\nelse:\n    print(\"Menor ou igual a 5\")", "opcoes": ["A) Imprime \"Maior que 5\" normalmente", "B) Dá erro de indentação", "C) Imprime \"Menor ou igual a 5\"", "D) O código não faz nada"], "resposta": "B", "valor": 1},
    {"pergunta": "5. Qual dessas opções representa uma estrutura de repetição em Python?", "opcoes": ["A) loop()", "B) for", "C) repeat", "D) do-while"], "resposta": "B", "valor": 1},
    {"pergunta": "6. Qual é a saída do seguinte código?\na = 5\nb = \"10\"\nprint(a + int(b))", "opcoes": ["A) 15", "B) 510", "C) Erro de tipo", "D) 5 + 10"], "resposta": "A", "valor": 2},
    {"pergunta": "7. O que esse código faz?\nfor i in range(3):\n    print(i)", "opcoes": ["A) Imprime 1, 2, 3", "B) Imprime 0, 1, 2", "C) Imprime 0, 1, 2, 3", "D) Dá erro"], "resposta": "B", "valor": 1},
    {"pergunta": "8. Como declarar uma lista em Python?", "opcoes": ["A) lista = {1, 2, 3}", "B) lista = [1, 2, 3]", "C) lista = (1, 2, 3)", "D) lista = <1, 2, 3>"], "resposta": "B", "valor": 2}
]

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
            main_aluno(email_aluno)
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

def main_aluno(email):
    estado_main_aluno = False

    while not estado_main_aluno:
        menu_main_aluno = input("Digite:\n\n\"P\" Para acessar a prova\n\"R\" Para acessar sua nota\n\"E\" Para desconectar\n").upper()

        if menu_main_aluno not in ["P","R","E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_main_aluno == "P":
            avaliacao(email)
        elif menu_main_aluno == "R":
            avaliacao_resultado(email)
        elif menu_main_aluno == "E":
            print("Desconectar!")
            break

def main_professor():

    while True:
        menu_main_professor = input("Digite:\n\n\"R\" Para acessar o relatório completo\n\"G\" Para acessar o gabarito\n\"E\" Para desconectar\n").upper()

        if menu_main_professor == "R":
            relatorio_professor()
        elif menu_main_professor == "G":
            gabarito()  
        elif menu_main_professor == "E":
            print("Desconectar!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

def carregar_tentativas():
    try:
        with open("tentativas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_tentativas(tentativas):
    with open("tentativas.json", "w") as f:
        json.dump(tentativas, f)

def calcular_media(email):
    tentativas = carregar_tentativas()
    notas = tentativas.get(email, [])
    
    if notas:
        media_aluno = sum(notas) / len(notas)
        return media_aluno
    return 0

def avaliacao(email):
    tentativas = carregar_tentativas()
    max_tentativas = 3
    
    if len(tentativas.get(email, [])) >= max_tentativas:
        print("Você já atingiu o número máximo de tentativas!")
        return
    
    print(f"Tentativa {len(tentativas.get(email, [])) + 1} de {max_tentativas}")
    nota = 0
    
    for questao in questoes:
        print("\n" + questao["pergunta"])
        for opcao in questao["opcoes"]:
            print(opcao)
        
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == questao["resposta"]:
            nota += questao["valor"]
        else:
            print(f"Resposta errada! A correta era: {questao['resposta']}")
    
    print(f"\nSua nota final: {nota}/{len(questoes)}")
    tentativas.setdefault(email, []).append(nota)
    salvar_tentativas(tentativas)
    
    if len(tentativas[email]) < max_tentativas:
        print(f"Você ainda tem {max_tentativas - len(tentativas[email])} tentativa(s).\n")
    else:
        print("Suas tentativas acabaram.\n")

def avaliacao_resultado(email):
    media = calcular_media(email)
    print(f"Média das tentativas: {media:.2f}/10")

def gabarito():
    print("\nGabarito das questões:")
    for questao in questoes:
        print(f"{questao['pergunta']}")
        print(f"Resposta correta: {questao['resposta']}\n")

def relatorio_professor():
    tentativas = carregar_tentativas()

    if not tentativas:
        print("Nenhum aluno completou a prova ainda.")
        return

    print("\nRelatório do Professor:\n") 
    print("Notas dos alunos e suas médias:")

    for email, notas in tentativas.items():
        nome_aluno = usuarios_alunos[email]["nome"]
        media_aluno = calcular_media(email)  
        print(f"{nome_aluno} - Média: {media_aluno:.2f}")

    acertos = [0] * len(questoes)
    total_respostas = [0] * len(questoes)

    for respostas in tentativas.values():
        for i, nota in enumerate(respostas):
            if nota > 0:
                acertos[i] += 1
            total_respostas[i] += 1

    if total_respostas:
        questao_mais_acertada = acertos.index(max(acertos))
        questao_menos_acertada = acertos.index(min(acertos))
        
        print("\nQuestões com mais acertos e menos acertos:")
        print(f"Questão com mais acertos: {questoes[questao_mais_acertada]['pergunta']}")
        print(f"Questão com menos acertos: {questoes[questao_menos_acertada]['pergunta']}")
    else:
        print("Nenhuma tentativa registrada!")

verifica_user()