import time
import os

def listPeers():
    print("Listar peers")
    # executar comando para listar peers

def getPeers():
    print("Obter peers")
    # executar comando para obter peers

def listLocalFiles():
    print("Listando arquivos locais")
    # executar comando para listar arquivos locais
    pasta = os.path.join(os.path.dirname(__file__), "..", "shared")
    for f in os.listdir(pasta):
        if os.path.isfile(os.path.join(pasta, f)):
            print(f)

def searchLocalFiles():
    print("Buscar arquivos locais")
    # executar comando para buscar arquivos locais

def showStats():
    print("Exibir estatísticas")
    # executar comando para exibir estatísticas

def changeChunkSize():
    print("Alterar tamanho do chunk")
    # executar comando para alterar tamanho do chunk


def leave():
    print("Saindo...")
    # executar comando para sair
    exit()