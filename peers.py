import socket
import threading
import time

from functions.clock import (
    start_clock,
    update_clock,
    get_clock
)

peers = [] # Lista de peers conhecidos

def add_peer(peer_ip, peer_port, status):
    global peers

    peer = (f"{peer_ip}:{peer_port}", status)
    if peer not in peers:
        peers.append(peer)
        print(f"Adicionado novo peer {peer_ip}:{peer_port} status {status}.")

def get_peers():
    global peers
    return peers 

def update_peer_status(peer_ip, peer_port, status):
    global peers
    peer = (f"{peer_ip}:{peer_port}", status)
    for i in range(len(peers)):
        if peers[i][0] == peer[0]:
            peers[i] = peer
            print(f"Atualizando peer {peer_ip}:{peer_port} status {status}.")
            break

def start_server(host, port):
    """ Inicia o servidor P2P """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    while True:
        client, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client,)).start()

""" Lida com a comunicação do cliente conectado """
def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        receptor_ip, receptor_port = client_socket.getsockname()
        msg = data.decode()
        parts = data.decode().split(" ")
        sender = parts[0]
        clock = parts[1]
        res_message = parts[2]

        match res_message:
            case "HELLO":
                # Atualizar o status do peer para ONLINE
                update_clock(get_clock())
                update_peer_status(receptor_ip, receptor_port, "ONLINE")
                print(f"Mensagem recebida: '{msg}'")
                break
            case "GET_PEERS":
                # preciso ver os peers conhecidos atualmente, e verificar se existe o arquivo txt
                # neighbors500x.txt, se existir, adicionar os vizinhos na lista de peers

                update_clock(get_clock())
                break
            case "PEERLIST":
                # Atualizar o status do peer para ONLINE
                update_clock(get_clock())
                # retornar a lista de peers conhecidos com endereço:porta:status:0
                print(f"Resposta recebida: '{receptor_ip}:{receptor_port} 4 PEER_LIST 1 127.0.0.1:9003:ONLINE:0'")
                break
            case _:
                print(f"Mensagem recebida: {msg}")
                break

        # client_socket.send(b"Mensagem recebida")
    client_socket.close()

""" Conecta-se a outro peer """
def connect_to_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket

def run_p2p(host, port):
    # Iniciando o servidor em uma thread separada
    threading.Thread(target=start_server, args=(host, port), daemon=True).start()
    



def send_message(receptor_ip, receptor_porta, mensagem):
    try:
        # Conectar ao peer receptor
        cliente_socket = connect_to_server(receptor_ip, receptor_porta)
        
        # Enviar mensagem
        cliente_socket.send(mensagem.encode())
        print(f"Encaminhando mensagem '{mensagem}' para {receptor_ip}:{receptor_porta}")

    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
    finally:
        time.sleep(0.5)
        cliente_socket.close()