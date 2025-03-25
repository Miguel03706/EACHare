import sys

def carregar_vizinhos(arquivo_vizinhos):
    vizinhos = []
    try:
        with open(arquivo_vizinhos, "r") as f:
            for linha in f:
                linha = linha.strip()  # Remove espaços e quebras de linha
                if linha:
                    endereco, porta = linha.split(":")  # Separa IP e porta
                    vizinhos.append((endereco, int(porta)))  # Converte porta para inteiro
        print("Vizinhos carregados com sucesso!")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_vizinhos}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao carregar vizinhos: {e}")
        sys.exit(1)

    return vizinhos