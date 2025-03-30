import socket
import threading
import time

def start_server(host, port):
    """ Inicia o servidor P2P """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor escutando em {host}:{port}...")
    
    while True:
        client, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr} \n")
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client_socket):
    """ Lida com a comunicação do cliente conectado """
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Recebido: {data.decode()}")
        client_socket.send(b"Mensagem recebida")
    client_socket.close()

def connect_to_server(server_ip, server_port):
    """ Conecta-se a outro peer """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Conectado ao servidor {server_ip}:{server_port} \n")
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
    client_socket = connect_to_server(host, port)
    
    # Enviando uma mensagem
    # send_message(client_socket, "Olá, peer!")
    
    # Fechando a conexão
    # client_socket.close()
    # print("Conexão fechada.")

