import os

from functions.clock import get_clock
from peers import (
    send_message,
    get_peers,
)

# Finalizado
def listPeers(peer_local):
    peers = get_peers()
    print ("\n Lista de peers:")
    print ("[0] voltar para o menu anterior")
    for i in range(len(peers)):
        print(f"[{i+1}] {peers[i][0]} {peers[i][1]}") 

    op = input("> ")
    if op == "0":
        return
    for i in range(len(peers)):
        if op == str(i+1):
            address_receptor = peers[i][0].split(":")[0]
            port_receptor = int(peers[i][0].split(":")[1])
            send_message(address_receptor, port_receptor, f"{peer_local[0][0]} {get_clock()} HELLO")
            peers[i] = (peers[i][0], "ONLINE")
            break
    return

# Wesley
def getPeers(peer_local, peers):
    # executar comando para enviar mensagem para todos os peers conhecidos
     """ ler os vizinhos dos peers atuais(se existir) e mandar msg para eles
         adicionando eles na lista de peers e atualizando o status deles
     """
     pass
 

# Finalizado
def listLocalFiles(archive):
    print("Listando arquivos locais")
    # executar comando para listar arquivos locais
    pasta = os.path.join(os.path.dirname(__file__), "..", archive)
    for f in os.listdir(pasta):
        if os.path.isfile(os.path.join(pasta, f)):
            print(f)

# Não precisa fazer
def searchLocalFiles():
    print("Buscar arquivos locais")
    # executar comando para buscar arquivos locais

# Não precisa fazer
def showStats():
    print("Exibir estatísticas")
    # executar comando para exibir estatísticas

# Não precisa fazer
def changeChunkSize():
    print("Alterar tamanho do chunk")
    # executar comando para alterar tamanho do chunk

# Finalizado
# executa comando para sair
def leave():
    print("Saindo...")
    exit()