print("Bem-vindo ao nosso site.")

def verifica_user():
    estado = False

    while not estado:
        cadastro = input("Digite:\n\"A\" Para acesso a área do aluno\n\"P\" Para acesso a área do professor\n\"E\" Para Sair\n").upper()
    
        if cadastro not in ["A", "a", "P", "p", "E", "e"]:
            print("\nOpção inválida. Tente novamente.\n")
            continue

        if cadastro == "A" or cadastro == "a":
            estado = True
            aluno()
        elif cadastro == "P" or cadastro == "p":
            estado = True
            professor()    
        elif cadastro == "E" or cadastro == "e":
            break


def aluno():
    print("Bem-vindo Aluno")

    

def professor():
    print("rpre")

main = verifica_user()

print(main)