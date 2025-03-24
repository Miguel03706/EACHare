def printMenu():
    print("[1] Listar peers")
    print("[2] Obter peers")
    print("[3] Listar arquivos locais")
    print("[4] Buscar arquivos locais")
    print("[5] Exibir estatísticas") 
    print("[6] Alterar tamanho do chunk") 
    print("[9] Sair")

def listPeers():
    print("Listar peers")
    # executar comando para listar peers
    main()

def getPeers():
    print("Obter peers")
    # executar comando para obter peers
    main()

def listLocalFiles():
    print("Listar arquivos locais")
    # executar comando para listar arquivos locais
    main()

def searchLocalFiles():
    print("Buscar arquivos locais")
    # executar comando para buscar arquivos locais
    main()

def showStats():
    print("Exibir estatísticas")
    # executar comando para exibir estatísticas
    main()

def changeChunkSize():
    print("Alterar tamanho do chunk")
    # executar comando para alterar tamanho do chunk
    main()


def leave():
    print("Saindo...")
    # executar comando para sair
    exit()

def main():
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