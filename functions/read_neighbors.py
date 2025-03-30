import sys

def load_neighbors(archive_neighbors):
    neighbors = []
    try:
        with open(archive_neighbors, "r") as f:
            for linha in f:
                linha = linha.strip()  # Remove espaços e quebras de linha
                if linha:
                    endereco, porta = linha.split(":")  # Separa IP e porta
                    neighbors.append(f"{endereco}:{int(porta)}")  # Converte porta para inteiro
        print("Vizinhos carregados com sucesso!")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{archive_neighbors}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao carregar vizinhos: {e}")
        sys.exit(1)

    return neighbors