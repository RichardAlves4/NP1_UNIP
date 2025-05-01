import bcrypt
import json
import os

# Função para carregar os dados
def carregar_usuarios():
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as file:
            return json.load(file)
    else:
        return {}

# Função para salvar os dados
def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

# Função para cadastro
def cadastrar_usuario():
    print("\nAntes de se cadastrar, você deve aceitar nossa Política de Privacidade.")
    print()
    print("Usaremos seus dados apenas para criar sua conta no sistema e permitir seu acesso às provas.")
    print()
    aceitar = input("Você aceita nossa Política de Privacidade? (s/n): ").lower()
    print()

    if aceitar != 's':
        print("Cadastro cancelado. Você deve aceitar os termos para continuar.\n")
        return

    usuarios = carregar_usuarios()

    email = input("Digite seu e-mail: ").lower()

    if email in usuarios:
        print()
        print("E-mail JÁ CADASTRADO!\n")
        return

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade:"))
    senha = input("Digite sua senha: ")

    # Hash da senha
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    usuarios[email] = {
        'nome': nome,
        'idade': idade,
        'senha': senha_hash.decode('utf-8')
    }

    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!\n")

# Função para login
def login_usuario():
    usuarios = carregar_usuarios()

    email = input("Digite seu e-mail: ").lower()
    senha = input("Digite sua senha: ")

    if email in usuarios:
        senha_armazenada = usuarios[email]['senha'].encode('utf-8')

        if bcrypt.checkpw(senha.encode('utf-8'), senha_armazenada):
            print(f"Login bem-sucedido! Bem-vindo(a), {usuarios[email]['nome']}.\n")
            menu_usuario(email)
        else:
            print("Senha incorreta.\n")
    else:
        print("Usuário não encontrado.\n")

# Menu do usuário logado
def menu_usuario(email):
    while True:
        print("1 - Editar meus dados")
        print("2 - Excluir minha conta")
        print("3 - Sair")
        print()
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            editar_dados(email)
        elif opcao == '2':
            excluir_conta(email)
            break
        elif opcao == '3':
            print("Saindo...\n")
            break
        else:
            print("Opção inválida.\n")

# Função para editar dados
def editar_dados(email):
    usuarios = carregar_usuarios()
    usuario = usuarios.get(email)

    if usuario:
        print("\nEdite seus dados (aperte Enter para manter o atual):")
        print()
        novo_nome = input(f"Nome atual ({usuario['nome']}): ")
        nova_idade = input(f"Idade atual ({usuario['idade']}): ")
        nova_senha = input("Nova senha (deixe vazio para não mudar): ")
        print()

        if novo_nome:
            usuario['nome'] = novo_nome
        if nova_idade:
            usuario['idade'] = nova_idade
        if nova_senha:
            usuario['senha'] = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        usuarios[email] = usuario
        salvar_usuarios(usuarios)
        print("DADOS ATUALIZADOS COM SUCESSO!\n")
    else:
        print("Usuário não encontrado.\n")

# Função para excluir conta
def excluir_conta(email):
    usuarios = carregar_usuarios()

    confirmacao = input("Tem certeza que deseja excluir sua conta? Esta ação é irreversível! (s/n): ").lower()

    if confirmacao == 's':
        usuarios.pop(email, None)
        salvar_usuarios(usuarios)
        print("Conta excluída com sucesso!\n")
    else:
        print("Exclusão cancelada.\n")

# Menu principal
def menu_principal():
    while True:
        print("=== Sistema de Provas ===")
        print()
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")
        print()
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            login_usuario()
        elif opcao == '3':
            print("Encerrando o sistema. Até mais!\n")
            break
        else:
            print("Opção inválida.\n")

# Iniciar o sistema
menu_principal()
