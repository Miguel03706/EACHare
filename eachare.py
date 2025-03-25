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

def main():
    # Captura os argumentos da linha de comando
    # 192.168.1.2:5000 neighbors5000.txt shared  
    if len(sys.argv) != 4:
        print("Uso correto: python eachare.py <endereco>:<porta> <vizinhos.txt> <diretorio_compartilhado>")
        sys.exit(1)

    endereco_porta = sys.argv[1]
    vizinhos_arquivo = sys.argv[2]
    diretorio_compartilhado = sys.argv[3]

    print(f"Endereço e porta: {endereco_porta}")
    print(f"Arquivo de vizinhos: {vizinhos_arquivo}")
    print(f"Diretório compartilhado: {diretorio_compartilhado}")

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
