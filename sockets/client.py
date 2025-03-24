import socket
import threading
import time

PORT = 5000
SERVER = "192.168.1.4"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# gerencia msg entre cliente e servidor
def handle_messages():
    while True:
        msg = client.recv(1024) # tamanho da msg q vai receber
        print(msg)
        

def send():
    client.send("HELLO")

# def send_message(msg):
#    send("msg="+msg)

# Envia quem é o autor da mensagem TODO: acho q nem vai precisar disso
# def send_author():
#    nome = input("Digite seu nome: ")
#    send_message(nome)

# def start_send():
#     send_author()
#    send_message("HELLO")

def start():
    thread1 = threading.Thread(target=handle_messages)
    thread2 = threading.Thread(target=send)
    thread1.start()
    thread2.start()

start()