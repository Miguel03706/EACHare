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



from peers import (
    run_p2p,
    send_message
)

def capturar_argumentos():
    """ Captura e retorna os argumentos passados via terminal. """
    if len(sys.argv) != 4:
        print("Uso correto: python eachare.py <endereco>:<porta> <neighbors5000.txt> <shared>")
        sys.exit(1)

    address_port = sys.argv[1]
    archive_neighbors = sys.argv[2]
    shared_folder = sys.argv[3]

    return address_port, archive_neighbors, shared_folder

def iniciar_peers(neighbors, peers):        
 # Iniciar cada peer vizinho em uma thread separada
    for neighbor in neighbors:
        neighbor_ip, neighbor_port = neighbor.split(":")
        neighbor_port = int(neighbor_port)
        run_p2p(neighbor_ip, neighbor_port)
        peers.append((f"{neighbor_ip}:{neighbor_port}", "OFFLINE"))
        print (f"Adicionado novo peer {neighbor_ip}:{neighbor_port} status OFFLINE")


def main():
    # Utiliza os argumentos capturados
    address_port, archive_neighbors, shared_folder = capturar_argumentos()

    addres = address_port.split(":")[0]
    port = int(address_port.split(":")[1])
    peers = [] # talvez passar para o "peers.py"
    neighbors = load_neighbors(archive_neighbors)
    peer_local = [(f"{addres}:{port}", "ONLINE")]
    run_p2p(addres, port)

    iniciar_peers(neighbors, peers)
    # print(peers)

    while True:
        printMenu()
        op = input("Escolha uma opção: ")
        if op == "1":
            listPeers(peer_local, peers)
        elif op == "2":
            getPeers()
        elif op == "3":
            listLocalFiles(shared_folder)
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
