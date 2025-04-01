# Importando a biblioteca bcrypt para criptografar senhas de forma segura
import bcrypt
# Importando a biblioteca json para manipulação de arquivos JSON
import json

# Definindo o nome do arquivo onde os dados de usuários serão salvos
arquivo_json = "usuarios.json"

# Dicionários para armazenar os dados de alunos e professores
usuarios_alunos = {}
usuarios_professores = {}

# Lista de questões para a prova
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
# RF12 - Função para carregar os usuários de um arquivo JSON
def carregar_usuarios():
    global usuarios_alunos, usuarios_professores
    try:
        # Tentando abrir o arquivo e carregar os dados
        with open(arquivo_json,"r") as json_aberto:
            dados = json.load(json_aberto)
            usuarios_alunos = dados.get("alunos", {})
            usuarios_professores  = dados.get("professores", {})
    except FileNotFoundError:
        # Se o arquivo não for encontrado, ele avisa e não faz nada
        print("Arquivo \"usuarios.json\" não encotrado. Gerando novo arquivo...")

# RF12 - Função para salvar os dados de usuários de volta no arquivo JSON
def salvar_usuarios():
    with open(arquivo_json, "w") as json_aberto:
        json.dump({"alunos":usuarios_alunos, "professores":usuarios_professores}, json_aberto, indent= 4)

# RF04 - Função para criptografar a senha usando bcrypt
def criptografar_senha(senha):
    salt = bcrypt.gensalt()  # Gera um salt para a criptografia
    return bcrypt.hashpw(senha.encode(), salt).decode()  # Criptografa e retorna a senha

# Função para verificar se a senha digitada corresponde à senha armazenada
def verificar_senha(senha_digitada, senha_armazenada):
    return bcrypt.checkpw(senha_digitada.encode(), senha_armazenada.encode())  # Retorna True ou False

# Função para carregar os usuários assim que o programa iniciar
carregar_usuarios()

# Exibe uma mensagem de boas-vindas
print("Bem-vindo ao nosso site.")

# Função principal para verificar qual tipo de usuário está tentando acessar (aluno ou professor)
def verifica_user():
    estado_verifica_user = False

    while not estado_verifica_user:
        # Solicita ao usuário qual área deseja acessar
        menu_verifica_user = input("Digite:\n\n\"A\" Para acesso a área do aluno\n\"P\" Para acesso a área do professor\n\"E\" Para Sair\n").upper()

        # Verifica se a opção escolhida é válida
        if menu_verifica_user not in ["A", "P", "E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_verifica_user == "A":
            aluno()  # Chama a função para o aluno
        elif menu_verifica_user == "P":
            professor()  # Chama a função para o professor
        elif menu_verifica_user == "E":
            print("Saiu!")  # Sai do programa
            break

# Função para gerenciar as ações do aluno (cadastro, login ou voltar)
def aluno():
    estado_aluno = False
    
    print("Bem-vindo Aluno")

    while not estado_aluno:
        # Solicita a opção ao aluno
        acao_aluno = str(input("Digite \"C\" para Cadastrar-se, \"L\" para acessar sua conta ou aperte \"E\" para voltar\n")).upper()
        
        if acao_aluno not in ["C", "L", "E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if acao_aluno == "C":
            estado_aluno = True
            cadastro_aluno()  # Chama a função para cadastrar o aluno
        elif acao_aluno == "L":
            estado_aluno = True
            login_aluno()  # Chama a função para logar o aluno
        elif acao_aluno == "E":
            print("Voltar!")  # Volta para o menu anterior
            return

# Função para gerenciar as ações do professor (cadastro, login ou voltar)
def professor():
    estado_professor = False

    print("Bem-vindo Professor")

    while not estado_professor:
        # Solicita a opção ao professor
        acao_professor = str(input("Digite \"C\" para Cadastrar-se, \"L\" para acessar sua conta ou aperte \"E\" para voltar\n")).upper()
        
        if acao_professor not in ["C", "L", "E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if acao_professor == "C":
            estado_professor = True
            cadastro_professor()  # Chama a função para cadastrar o professor
        elif acao_professor == "L":
            estado_professor = True
            login_professor()  # Chama a função para logar o professor
        elif acao_professor == "E":
            print("Voltar!")  # Volta para o menu anterior
            return


# RF01 - Cadastro de alunos
# RF02 - Validação de idade mínima (7 anos)
# RF03 - Validação de email (@gmail.com)
# RF04 - Armazenamento seguro de senha
# Função para o cadastro de alunos
def cadastro_aluno():
    print("\nCadastro de Alunos\n")
    
    while True:
        # Coleta as informações do aluno para o cadastro
        nome_aluno = (input("Informe seu nome: ")).strip().title()
        email_aluno = (input("Informe seu melhor email: ")).strip().lower()
        
        # RF03 - Verifica se o e-mail é válido
        if not email_aluno.endswith("@gmail.com"):
            print("\nE-mail inválido! Certifique-se de usar um endereço @gmail.com.\n")
            continue

        if email_aluno in usuarios_alunos:  # Verifica se o e-mail já está cadastrado
            print("Usuário já cadastrado")
            continue

        # RF02 - Valida e coleta a idade do aluno
        while True:
            idade_aluno = int(input("Informe sua idade: ").strip())
            if idade_aluno < 7:
                print("\nIdade inválida! Tente novamente.\n")
                continue
            else:
                break
            
        # RF04 - Coleta e verifica a senha
        while True:
            senha_aluno = (input("Informe uma senha forte: ")).strip()
            repet_senha_aluno = (input("Repita sua senha: ")).strip()

            if senha_aluno == repet_senha_aluno:  # Verifica se as senhas coincidem
                senha_criptografada = criptografar_senha(senha_aluno)  # Criptografa a senha
                usuarios_alunos[email_aluno] = {
                    "nome": nome_aluno,
                    "idade": idade_aluno,
                    "senha": senha_criptografada
                } 
                salvar_usuarios()  # RF12 - Salva os dados no arquivo
                print("\nCadastro realizado com sucesso!\n")
                return
            else:
                print("\nSenha incorreta! Tente novamente\n")

# RF01 - Cadastro de professores
# RF02 - Validação de idade mínima (18 anos)
# RF03 - Validação de email (@gmail.com)
# RF04 - Armazenamento seguro de senha
# Função para o cadastro de professores
def cadastro_professor():
    print("\nCadastro de Professores\n")
    
    while True:
        # Coleta as informações do professor para o cadastro
        nome_professor = str(input("Informe o seu nome: ")).strip().title()
        email_professor = str(input("Informe seu melhor email: ")).strip()
        
        # RF03 - Verifica se o e-mail é válido
        if not email_professor.endswith("@gmail.com"):
            print("\nE-mail inválido! Certifique-se de usar um endereço @gmail.com.\n")
            continue

        if email_professor in usuarios_professores:  # Verifica se o e-mail já está cadastrado
            print("Usuário já cadastrado")
            continue

        # RF02 - Coleta a idade do professor
        while True:
            idade_professor = int(input("Informe sua idade: ").strip())
            if idade_professor < 18:
                print("\nIdade inválida! Tente novamente.\n")
                continue
            else:
                break
            
        # RF04 - Coleta e verifica a senha
        while True:
            senha_professor = str(input("Informe uma senha forte: ")).strip()
            repet_senha_professor = str(input("Repita sua senha: ")).strip()

            if senha_professor == repet_senha_professor:  # Verifica se as senhas coincidem
                senha_criptografada = criptografar_senha(senha_professor)  # Criptografa a senha
                usuarios_professores[email_professor] = {
                    "nome": nome_professor,
                    "idade": idade_professor,
                    "senha": senha_criptografada
                }
                salvar_usuarios()  # RF12 - Salva os dados no arquivo
                print("\nCadastro realizado com sucesso!\n")
                return
            else:
                print("\nSenha incorreta! Tente novamente\n")

# RF05 - Função para o login do aluno
def login_aluno():
    print("\nEntrar como aluno\n")

    while True:
        # Coleta as credenciais do aluno
        email_aluno = str(input("Email: ")).strip().lower()
        senha_aluno = str(input("Senha: ")).strip()

        # Verifica se o usuário existe
        if email_aluno in usuarios_alunos:
            senha_armazenada = usuarios_alunos[email_aluno]["senha"]

            # RF04 - Verificação segura de senha
        if verificar_senha(senha_aluno, senha_armazenada):  # Verifica se a senha está correta
            print(f"\nBem-vindo, {usuarios_alunos[email_aluno]['nome']}!")
            main_aluno(email_aluno)  # Chama a função para o menu do aluno
            break
        print("Email ou senha incorretos! Tente novamente")

# RF05 - Função para o login do professor
def login_professor():
    print("\nEntrar como professor\n")

    while True:
        # Coleta as credenciais do professor
        email_professor = str(input("Email: ")).strip().lower()
        senha_professor = str(input("Senha: ")).strip()

        # Verifica se o usuário existe
        if email_professor in usuarios_professores:
            senha_armazenada = usuarios_professores[email_professor]["senha"]

            # RF04 - Verificação segura de senha
        if verificar_senha(senha_professor, senha_armazenada):  # Verifica se a senha está correta
            print(f"\nBem-vindo, {usuarios_professores[email_professor]['nome']}!")
            main_professor()  # Chama a função para o menu do professor
            break
        print("Email ou senha incorretos! Tente novamente")

# Função para o menu principal do aluno (prova, ver resultado, desconectar)
def main_aluno(email):
    estado_main_aluno = False

    while not estado_main_aluno:
        # Exibe as opções para o aluno
        menu_main_aluno = input("Digite:\n\n\"P\" Para acessar a prova\n\"R\" Para acessar sua nota\n\"E\" Para desconectar\n").upper()

        # Verifica as opções escolhidas pelo aluno
        if menu_main_aluno not in ["P","R","E"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if menu_main_aluno == "P":
            avaliacao(email)  # Chama a função para realizar a prova
        elif menu_main_aluno == "R":
            avaliacao_resultado(email)  # Chama a função para ver o resultado
        elif menu_main_aluno == "E":
            print("Desconectar!")  # Desconecta o aluno
            break

# Função para o menu principal do professor (relatório, gabarito, desconectar)
def main_professor():

    while True:
        # Exibe as opções para o professor
        menu_main_professor = input("Digite:\n\n\"R\" Para acessar o relatório completo\n\"G\" Para acessar o gabarito\n\"E\" Para desconectar\n").upper()

        # Verifica as opções escolhidas pelo professor
        if menu_main_professor == "R":
            relatorio_professor()  # Chama a função para ver o relatório
        elif menu_main_professor == "G":
            gabarito()  # Chama a função para ver o gabarito
        elif menu_main_professor == "E":
            print("Desconectar!")  # Desconecta o professor
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

# Função para carregar as tentativas dos alunos do arquivo JSON
def carregar_tentativas():
    try:
        with open("tentativas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar as tentativas dos alunos no arquivo JSON
def salvar_tentativas(tentativas):
    with open("tentativas.json", "w") as f:
        json.dump(tentativas, f)

# RF08 - Função para calcular a média das notas do aluno
def calcular_media(email):
    tentativas = carregar_tentativas()
    notas = tentativas.get(email, [])
    
    if notas:
        # Calculando a média individual do aluno
        media_aluno = sum(notas) / len(notas)
        return media_aluno
    return 0

# RF06 - Função para a prova do aluno
def avaliacao(email):
    tentativas = carregar_tentativas()
    max_tentativas = 3
    
    if email in tentativas and len(tentativas[email]) >= max_tentativas:
        print("\nVocê já atingiu o número máximo de tentativas!\n")
        return
    
    print("\nComece a prova!\n")
    
    # RF07 - Cálculo de nota
    # A cada pergunta, o aluno tem que responder e vamos atribuindo uma pontuação
    pontuacao = 0
    for questao in questoes:
        print(questao["pergunta"])
        for opcao in questao["opcoes"]:
            print(opcao)
        
        resposta = input("\nDigite a letra da resposta correta: ").strip().upper()
        if resposta == questao["resposta"]:  # Se a resposta estiver correta
            print("Correto!\n")
            pontuacao += questao["valor"]
        else:
            print("Errado!\n")
    
    # Atualizando as tentativas do aluno
    if email not in tentativas:
        tentativas[email] = []
    
    tentativas[email].append(pontuacao)  # Adicionando a pontuação na lista de tentativas
    salvar_tentativas(tentativas)  # Salvando as tentativas no arquivo
    
    print(f"Você acertou {pontuacao} questões!\n")
    print(f"Sua média de notas é {calcular_media(email):.2f}\n")
    print("Fim da prova!")

# RF08 - Função para mostrar o resultado da avaliação do aluno
def avaliacao_resultado(email):
    tentativas = carregar_tentativas()

    if email not in tentativas or not tentativas[email]:
        print("\nVocê ainda não realizou a prova!\n")
        return
    
    print("\nSeu resultado de avaliações anteriores:\n")
    for i, pontuacao in enumerate(tentativas[email]):
        print(f"Tentativa {i + 1}: {pontuacao} pontos")

    print(f"\nSua média geral é: {calcular_media(email):.2f}\n")

# RF11 - Função para exibir o gabarito da prova
def gabarito():
    print("\nGabarito da prova\n")
    for questao in questoes:
        print(f"{questao['pergunta']} Resposta: {questao['resposta']}")

# RF09 - Função para exibir o relatório completo para o professor
def relatorio_professor():
    tentativas = carregar_tentativas()

    if not tentativas:
        print("Nenhum aluno completou a prova ainda.")
        return

    print("\nRelatório do Professor:\n") 
    print("Notas dos alunos e suas médias:")

    for email, notas in tentativas.items():
        nome_aluno = usuarios_alunos[email]["nome"]
        media_aluno = calcular_media(email)  # Calcula a média do aluno
        print(f"{nome_aluno} - Média: {media_aluno:.2f}")

    acertos = [0] * len(questoes)
    total_respostas = [0] * len(questoes)

    for respostas in tentativas.values():
        for i, nota in enumerate(respostas):
            if nota > 0:  # Conta acertos
                acertos[i] += 1
            total_respostas[i] += 1  # Conta o total de respostas para cada questão

    # RF10 - Exibe as estatísticas sobre as questões
    if total_respostas:
        questao_mais_acertada = acertos.index(max(acertos))
        questao_menos_acertada = acertos.index(min(acertos))
        
        print("\nQuestões com mais acertos e menos acertos:")
        print(f"Questão com mais acertos: {questoes[questao_mais_acertada]['pergunta']}")
        print(f"Questão com menos acertos: {questoes[questao_menos_acertada]['pergunta']}")
    else:
        print("Nenhuma tentativa registrada!")

# Função principal para executar o sistema
verifica_user()