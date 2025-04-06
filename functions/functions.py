import os
import socket


from functions.clock import get_clock

from peers import (
    send_message,
    get_peers,
    update_peer_status,
    add_peer
    )

# Finalizado
import socket
from functions.clock import get_clock
from peers import get_peers, update_peer_status

def listPeers(peer_local):
    peers = get_peers()
    print("\n Lista de peers:")
    print("[0] voltar para o menu anterior")
    for i, peer in enumerate(peers):
        print(f"[{i+1}] {peer[0]} {peer[1]}")

    op = input("> ")
    if op == "0":
        return

    # Valida a opção escolhida
    try:
        index = int(op) - 1
        selected_peer = peers[index]
        address = selected_peer[0].split(":")[0]
        port = int(selected_peer[0].split(":")[1])
    except Exception as e:
        print("Opção inválida.")
        return

    mensagem = f"{peer_local[0][0]} {get_clock()} HELLO"

    try:
        # Tenta se conectar ao peer e enviar a mensagem
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(3)  # tempo limite de 3 segundos para conexão
        client_socket.connect((address, port))
        client_socket.send(mensagem.encode())
        print(f"Encaminhando mensagem '{mensagem}' para {address}:{port}")
        client_socket.close()
        # Atualiza o status para ONLINE se o envio foi bem-sucedido
        update_peer_status(address, port, "ONLINE")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        # Atualiza o status para OFFLINE se não foi possível enviar
        update_peer_status(address, port, "OFFLINE")

    return


# Wesley
# ler os vizinhos dos peers atuais(se existir) e mandar msg para eles
# adicionando eles na lista de peers e atualizando o status deles
# add tbm no arquivo de vizinhos inicial
def getPeers(peer_local):
    peers = get_peers()
    for peer in peers:
        address = peer[0].split(":")[0]
        port = int(peer[0].split(":")[1])
        message = f"{peer_local[0][0]} {get_clock()} GET_PEERS"
        try:
            # Tenta se conectar e enviar a mensagem GET_PEERS
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(3)  # timeout de 3 segundos
            client_socket.connect((address, port))
            client_socket.send(message.encode())
            print(f"Encaminhando mensagem '{message}' para {address}:{port}")
            
            # Aguarda a resposta (PEER_LIST)
            response = client_socket.recv(4096).decode().strip()
            # Exemplo de resposta:
            # "127.0.0.1:9002 4 PEER_LIST 1 127.0.0.1:9003:ONLINE:0"
            parts = response.split(" ")
            if len(parts) >= 4 and parts[2] == "PEER_LIST":
                num_peers = int(parts[3])
                # A partir da posição 4, cada elemento é um peer codificado
                for peer_info in parts[4:]:
                    # Cada peer_info no formato: <endereço>:<porta>:<status>:0
                    info_parts = peer_info.split(":")
                    if len(info_parts) >= 4:
                        ip = info_parts[0]
                        port_peer = int(info_parts[1])
                        status = info_parts[2]
                        # Atualiza ou adiciona o peer à lista local
                        add_peer(ip, port_peer, status)
            update_peer_status(address, port, "ONLINE")
            client_socket.close()
        except Exception as e:
            print(f"Erro ao enviar GET_PEERS para {address}:{port} - {e}")
            update_peer_status(address, port, "OFFLINE")
    return

 

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