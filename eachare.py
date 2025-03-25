import sys
from functions.functions import (
    listPeers,
    getPeers,
    listLocalFiles,
    searchLocalFiles,
    showStats,
    changeChunkSize,
    leave
)
from view.menu import (
    printMenu
)

from functions.read_neighbors import(
    load_neighbors
)


def main():
    # Captura os argumentos da linha de comando
    # 192.168.1.2:5000 neighbors5000.txt shared  
    # mudar o ip de acordo com seu ipv4 (entrar no cmd e digita: ipconfig) -> la da pra ver o ipv4
    if len(sys.argv) != 4:
        print("Uso correto: python eachare.py <endereco>:<porta> <neighbors5000.txt> <shared>")
        sys.exit(1)

    address_port = sys.argv[1]
    archive_neighbors = sys.argv[2]
    shared_folder = sys.argv[3]

    print(f"Endereço e porta: {address_port}")
    print(f"Arquivo de vizinhos: {archive_neighbors}")
    print(f"Diretório compartilhado: {shared_folder}")

    neighbors = load_neighbors(archive_neighbors)
    print(neighbors)

    # pelo o que eu entendi, agora a gente tem que pegar essas infos
    # iniciar o servidor e o cliente com base nessas infos
    # depois disso, basta fazer cada uma das funções

    while True:
        printMenu()
        op = input("Escolha uma opção: ")
        if op == "1":
            listPeers()
        elif op == "2":
            getPeers()
        elif op == "3":
            listLocalFiles()
        elif op == "4":
            searchLocalFiles()
        elif op == "5":
            showStats()
        elif op == "6":
            changeChunkSize()
        elif op == "9":
            leave()
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
