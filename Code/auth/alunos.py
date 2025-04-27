from .utils import criptografar_senha, verificar_senha
import banco
# RF01 - Cadastro de alunos
# RF02 - Validação de idade mínima (7 anos)
# RF03 - Validação de email (@gmail.com)
# RF04 - Armazenamento seguro de senha
# Função para o cadastro de alunos
def cadastro_aluno():
    print("\nCadastro de Alunos\n")
    while True:
        # Coleta as informações do aluno para o cadastro
        nome = input("Informe seu nome: ").strip().title()
        email = input("Informe seu melhor email: ").strip().lower()

        # RF03 - Verifica se o e-mail é válido
        if not email.endswith("@gmail.com"):
            print("Email inválido. Use @gmail.com")
            continue

        # Verifica se o e-mail já está cadastrado
        if email in banco.usuarios_alunos:
            print("Usuário já cadastrado")
            continue

        # RF02 - Valida e coleta a idade do aluno
        idade = int(input("Informe sua idade: "))
        if idade < 7:
            print("Idade mínima: 7 anos")
            continue

        senha = input("Informe uma senha forte: ")
        repet_senha = input("Repita a senha: ")

        # Verifica se as senhas coincidem
        if senha != repet_senha:
            print("As senhas diferentes. Tente novamente")
            continue

        senha_criptografada = criptografar_senha(senha) # Criptografa a senha
        banco.usuarios_alunos[email] = {
            "nome": nome, 
            "idade": idade, 
            "senha": senha_criptografada
        }
        banco.salvar_usuarios() # RF12 - Salva os dados no arquivo
        print("Cadastro realizado com sucesso!")
        return

# RF05 - Função para o login do aluno
def login_aluno():
    print("\nLogin de Aluno\n")

    # Coleta as credenciais do aluno
    email = input("Email: ").strip().lower()
    senha = input("Senha: ").strip()

    # Verifica se o usuário existe
    if email in banco.usuarios_alunos:
        # RF04 - Verificação segura de senha
        if verificar_senha(senha, banco.usuarios_alunos[email]["senha"]):# Verifica se a senha está correta
            print(f"Bem-vindo, {banco.usuarios_alunos[email]['nome']}!")
            return email
    print("Email ou senha incorretos!")
    return None