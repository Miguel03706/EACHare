import socket
import threading
import time

def start_server(host, port):
    """ Inicia o servidor P2P """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    while True:
        client, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client_socket):
    """ Lida com a comunicação do cliente conectado """
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Mensagem recebida: {data.decode()}")
        # atualizar o clock

        # client_socket.send(b"Mensagem recebida")
    client_socket.close()

def connect_to_server(server_ip, server_port):
    """ Conecta-se a outro peer """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket

def send_message(client_socket, message):
    """ Envia uma mensagem para outro peer """
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print(f"Resposta: {response.decode()}")

def run_p2p(host, port):
    # Iniciando o servidor em uma thread separada
    threading.Thread(target=start_server, args=(host, port), daemon=True).start()
    
    # Aguarde o servidor começar a escutar
    time.sleep(1)
    
    # Conectando-se ao servidor (cliente)
    # client_socket = connect_to_server(host, port)
    
    # Enviando uma mensagem
    # send_message(client_socket, "Olá, peer!")
    
    # Fechando a conexão
    # client_socket.close()
    # print("Conexão fechada.")


def enviar_mensagem(cliente_ip, cliente_porta, receptor_ip, receptor_porta, mensagem):
    try:
        # Criar socket do cliente
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectar ao receptor
        cliente_socket.connect((receptor_ip, receptor_porta))
        
        # Enviar mensagem
        cliente_socket.sendall(mensagem.encode())
        print(f"Encaminhando mensagem '{cliente_ip}:{cliente_porta} 1 HELLO' para {receptor_ip}:{receptor_porta}")
        
        resposta = cliente_socket.recv(1024)
        print(f"Mensagem recebida: {resposta.decode()}")
    
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
    finally:
        cliente_socket.close()