from auth import cadastro_aluno, login_aluno, cadastro_professor, login_professor
from avaliacao import aplicar_prova, mostrar_resultado_aluno, mostrar_gabarito, relatorio_professor
from banco import carregar_usuarios, salvar_usuarios, usuarios_alunos, usuarios_professores
from banco import carregar_usuarios, salvar_usuarios, carregar_tentativas, salvar_tentativas, usuarios_alunos, usuarios_professores

def menu_inicial():
    print("Bem-vindo ao Sistema de Avaliação\n")
    print("1. Cadastro de Aluno")
    print("2. Login de Aluno")
    print("3. Cadastro de Professor")
    print("4. Login de Professor")
    print("5. Aplicar Prova")
    print("6. Ver Resultado da Prova")
    print("7. Ver Gabarito")
    print("8. Gerar Relatório de Avaliação para Professores")
    print("0. Sair")

def menu_aluno():
    print("\nMenu Aluno:")
    print("1. Fazer Prova")
    print("2. Ver Resultado da Prova")
    print("3. Sair")

def menu_professor():
    print("\nMenu Professor:")
    print("1. Gerar Relatório de Avaliação")
    print("2. Sair")

def main():
    carregar_usuarios()  # Carrega os dados dos usuários no início
    carregar_tentativas() # Carrega os dados das notas dos alunos

    while True:
        menu_inicial()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":  # Cadastro de Aluno
            cadastro_aluno()
        elif opcao == "2":  # Login de Aluno
            aluno_email = login_aluno()
            if aluno_email:
                while True:
                    menu_aluno()
                    opcao_aluno = input("Escolha uma opção: ").strip()

                    if opcao_aluno == "1":  # Fazer Prova
                        aplicar_prova(aluno_email)
                    elif opcao_aluno == "2":  # Ver Resultado
                        mostrar_resultado_aluno(aluno_email)
                    elif opcao_aluno == "3":  # Sair
                        break
                    else:
                        print("Opção inválida.")
        elif opcao == "3":  # Cadastro de Professor
            cadastro_professor()
        elif opcao == "4":  # Login de Professor
            professor_email = login_professor()
            if professor_email:
                while True:
                    menu_professor()
                    opcao_professor = input("Escolha uma opção: ").strip()

                    if opcao_professor == "1":  # Gerar Relatório
                        relatorio_professor(usuarios_alunos)
                    elif opcao_professor == "2":  # Sair
                        break
                    else:
                        print("Opção inválida.")
        elif opcao == "5":  # Aplicar Prova (Opção rápida para qualquer um)
            email = input("Informe seu email: ").strip().lower()
            if email in usuarios_alunos or email in usuarios_professores:
                aplicar_prova(email)
            else:
                print("Usuário não encontrado!")
        elif opcao == "6":  # Ver Resultado
            email = input("Informe seu email: ").strip().lower()
            if email in usuarios_alunos:
                mostrar_resultado_aluno(email)
            else:
                print("Usuário não encontrado!")
        elif opcao == "7":  # Ver Gabarito
            mostrar_gabarito()
        elif opcao == "8":  # Gerar Relatório (Opção rápida para qualquer professor)
            email = input("Informe seu email de professor: ").strip().lower()
            if email in usuarios_professores:
                relatorio_professor(usuarios_alunos)
            else:
                print("Professor não encontrado!")
        elif opcao == "0":  # Sair
            salvar_usuarios()  # Salva os usuários antes de sair
            salvar_tentativas()  # Salva tentativas
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
