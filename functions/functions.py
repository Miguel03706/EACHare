import os

from peers import (
enviar_mensagem
)

from functions.clock import (
    get_clock, 
    update_clock
)

# Finalizado
def listPeers(peer_local, peers):
    print ("\n Lista de peers:")
    print ("[0] voltar para o menu anterior")
    for i in range(len(peers)):
        print(f"[{i+1}] {peers[i][0]} {peers[i][1]}") 

    op = input("> ")
    if op == "0":
        return
    for i in range(len(peers)):
        if op == str(i+1):
            address_local = peer_local[0][0].split(":")[0]
            port_local = int(peer_local[0][0].split(":")[1])
            address_receptor = peers[i][0].split(":")[0]
            port_receptor = int(peers[i][0].split(":")[1])

            enviar_mensagem(address_local, port_local, address_receptor, port_receptor, f"{peer_local[0][0]} 1 HELLO")
            print(f"Atualizando peer {peers[i][0]} status ONLINE")
            update_clock(get_clock())
            peers[i] = (peers[i][0], "ONLINE")
            break
    return

# Wesley
def getPeers(peer_local, peers):
    # executar comando para enviar mensagem para todos os peers conhecidos
     update_clock(get_clock())
     """ ler os vizinhos dos peers atuais(se existir) e mandar msg para eles
         adicionando eles na lista de peers e atualizando o status deles
     """
     for i in range(len(peers)):
        address_local = peer_local[0][0].split(":")[0]
        port_local = int(peer_local[0][0].split(":")[1])
        address_receptor = peers[i][0].split(":")[0]
        port_receptor = int(peers[i][0].split(":")[1])
        try:
            enviar_mensagem(address_local, port_local, address_receptor, port_receptor, f"{peer_local[0][0]} 2 GET_PEERS")
            print(f"Atualizando peer {peers[i][0]} status ONLINE")
            update_clock(get_clock())
            peers[i] = (peers[i][0], "ONLINE")
        except:
            peers[i] = (peers[i][0], "OFFLINE")

        break
 

# Finalizado
def listLocalFiles(archive):
    print("Listando arquivos locais")
    # executar comando para listar arquivos locais
    pasta = os.path.join(os.path.dirname(__file__), "..", archive)
    for f in os.listdir(pasta):
        if os.path.isfile(os.path.join(pasta, f)):
            print(f)

# Wesley
def searchLocalFiles():
    print("Buscar arquivos locais")
    # executar comando para buscar arquivos locais

# Miguel
def showStats():
    print("Exibir estatísticas")
    # executar comando para exibir estatísticas

# Wesley
def changeChunkSize():
    print("Alterar tamanho do chunk")
    # executar comando para alterar tamanho do chunk

# Finalizado
# executa comando para sair
def leave():
    print("Saindo...")
    exit()