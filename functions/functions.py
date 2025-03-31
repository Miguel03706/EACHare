import os

from view.listPeers import listAllPeers

# Miguel
def listPeers(peer_local, peers):
    listAllPeers(peer_local, peers)

# Wesley
def getPeers():
    print("Obter peers")
    # executar comando para obter peers

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