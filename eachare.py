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
    
main()