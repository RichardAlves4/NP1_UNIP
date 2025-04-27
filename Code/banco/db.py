# Importando a biblioteca json para manipulação de arquivos JSON
import json
import os

# Diretório onde os arquivos serão guardados
diretorio_bd = os.path.dirname(__file__)

# Definindo o nome dos arquivos
arquivo_usuarios = os.path.join(diretorio_bd, "usuarios.json")
arquivo_tentativas = os.path.join(diretorio_bd, "tentativas.json")

# Dicionários para armazenar os dados de alunos e professores
usuarios_alunos = {}
usuarios_professores = {}
tentativas_alunos = {}

# RF12 - Função para carregar os usuários de um arquivo JSON
def carregar_usuarios():
    global usuarios_alunos, usuarios_professores
    try:
        # Tenta abrir o arquivo e carregar os dados
        with open(arquivo_usuarios, "r") as json_aberto:
            dados = json.load(json_aberto)
            # Limpa o que já existe na memória 
            usuarios_alunos.clear()
            usuarios_professores.clear()
            # Depois atualiza com os dados do arquivo
            usuarios_alunos.update(dados.get("alunos", {}))
            usuarios_professores.update(dados.get("professores", {}))
    except FileNotFoundError:
        print('Arquivo "usuarios.json" não encontrado. Um novo será criado quando salvar.')

# RF12 - Função para salvar os dados de usuários de volta no arquivo JSON
def salvar_usuarios():
    with open(arquivo_usuarios, "w") as json_aberto:
        json.dump({
            "alunos": usuarios_alunos,
            "professores": usuarios_professores
        }, json_aberto, indent=4)

# Função para carregar as tentativas dos alunos do arquivo JSON
def carregar_tentativas():
    global tentativas_alunos
    try:
        with open(arquivo_tentativas, "r") as f:
            dados = json.load(f)
            tentativas_alunos.clear()
            tentativas_alunos.update(dados)
    except FileNotFoundError:
        print('Arquivo "tentativas.json" não encontrado. Um novo será criado quando salvar.')

# Função para salvar as tentativas dos alunos no arquivo JSON
def salvar_tentativas():
    with open(arquivo_tentativas, "w") as f:
        json.dump(tentativas_alunos, f, indent=4)
