from .utils import criptografar_senha, verificar_senha
import banco
# RF01 - Cadastro de professores
# RF02 - Validação de idade mínima (18 anos)
# RF03 - Validação de email (@gmail.com)
# RF04 - Armazenamento seguro de senha
# Função para o cadastro de professores
def cadastro_professor():
    print("\nCadastro de Professores\n")
    while True:
        # Coleta as informações do professor para o cadastro
        nome = input("Informe seu nome: ").strip().title()
        email = input("Informe seu melhor email: ").strip().lower()

        # RF03 - Verifica se o e-mail é válido
        if not email.endswith("@gmail.com"):
            print("Email inválido. Use @gmail.com")
            continue
        
        # Verifica se o e-mail já está cadastrado
        if email in banco.usuarios_professores:
            print("Usuário já cadastrado")
            continue
        
        # RF02 - Coleta a idade do professor
        idade = int(input("Informe sua idade: "))
        if idade < 18:
            print("Idade mínima: 18 anos. Tente novamente")
            continue
        
        # RF04 - Coleta e verifica a senha
        senha = input("Informe uma senha forte: ")
        repet_senha = input("Repita a senha: ")

        # Verifica se as senhas coincidem
        if senha != repet_senha:
            print("As senhas não coincidem")
            continue
        
        # Criptografa a senha
        senha_criptografada = criptografar_senha(senha)
        banco.usuarios_professores[email] = {
            "nome": nome,
            "idade": idade,
            "senha": senha_criptografada
        }
        banco.salvar_usuarios() # RF12 - Salva os dados no arquivo
        print("Cadastro realizado com sucesso!")
        return

# RF05 - Função para o login do professor
def login_professor():
    print("\nLogin de Professor\n")

    # Coleta as credenciais do professor
    email = input("Email: ").strip().lower()
    senha = input("Senha: ").strip()

    # Verifica se o usuário existe
    if email in banco.usuarios_professores:
        # RF04 - Verificação segura de senha
        if verificar_senha(senha, banco.usuarios_professores[email]["senha"]):
            print(f"Bem-vindo, {banco.usuarios_professores[email]['nome']}!")
            return email
    print("Email ou senha incorretos!")
    return None