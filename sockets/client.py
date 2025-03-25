import socket
import threading
import time


# TODO: essas infos tem que vir dos parametros passados ao iniciar o código 
PORT = 5000
SERVER = "192.168.1.2"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# gerencia msg entre cliente e servidor
def handle_messages():
    while True:
        msg = client.recv(1024).decode() # tamanho da msg q vai receber
        print(msg)
        
# envia msg para o servidor
def send():
    msg = (f"{SERVER}:{PORT} 1 HELLO")
    client.send(msg.encode())
    # ESTRUTURA CORRETA: <ORIGEM> <CLOCK> <TIPO>
    # EX: 127.0.0.1:9002 1 HELLO
    print(f"Encaminhando mensagem {msg} para {SERVER}:{PORT}")

# para cada cliente, uma thread diferente vai ser criada
# TODO: dps aqui vai ter q ter um laço que cria essas threads eu acho
def start():
    thread1 = threading.Thread(target=handle_messages)
    thread2 = threading.Thread(target=send)
    thread1.start()
    thread2.start()

#start()