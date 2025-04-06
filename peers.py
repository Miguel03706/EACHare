import socket
import threading
import time

from functions.clock import (
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
        parts = msg.split(" ")
        sender = parts[0]
        clock_value = parts[1]
        res_message = parts[2]

        match res_message:
            case "HELLO":
                update_peer_status(receptor_ip, receptor_port, "ONLINE")
                print(f"Mensagem recebida: '{msg}'")
                update_clock(get_clock())
                break
            case "GET_PEERS":
                # Atualiza o relógio
                update_clock(get_clock())
                # Obtém a lista de peers conhecidos e exclui o remetente
                current_peers = get_peers()
                response_peers = []
                for p in current_peers:
                    if p[0] != sender:
                        # Formata: <endereço>:<porta>:<status>:0
                        response_peers.append(f"{p[0]}:{p[1]}:0")
                num_peers = len(response_peers)
                # Origem: o peer local (obtido via receptor_ip e receptor_port)
                origin = f"{receptor_ip}:{receptor_port}"
                response_message = f"{origin} {get_clock()} PEER_LIST {num_peers} " + " ".join(response_peers) + "\n"
                client_socket.send(response_message.encode())
                break
            case "PEER_LIST":
                # Essa mensagem pode ser processada no lado que enviou o GET_PEERS
                print(f"Resposta recebida: '{msg}'")
                update_clock(get_clock())
                break
            case _:
                print(f"Comando desconhecido")
                print(f"Mensagem recebida: '{msg}'")
                break
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