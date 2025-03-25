import socket
import threading
import time

SERVER_IP = socket.gethostname()
SERVER_PORT = 5000
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

conections = []
messages = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDR)


def sendMessageIndividual(conn):
    global messages
    for msg in messages:
        conn.send(msg)
        # sem o sleep o server eventualmente buga
        time.sleep(0.5) # delay de 0.5s para não sobrecarregar o servidor

def sendMessageToAll(msg):
    global conections
    for conn in conections:
        sendMessageIndividual(conn)

# Envia mensagem para todos os clientes conectados
def handleClient(conn, addr):
    print(f"[Nova conexão] Usuário: {addr} conectado. \n")
    print(f"[Conexão] : {conn}")
    global conections
    global messages

    while True:
        msg = conn.recv(1024)
        # se não tiver msg, o usuário desconectou 
        # FIXME: mudar status para offline?
        if not msg:
            print(f"[Desconectado] Usuário: {addr} desconectado.")
            break
        print(f"[Mensagem] {addr}: {msg.decode()}")
        sendMessageToAll(msg)
        conections.append(msg)

# Inicia o servidor em threads
def startServer():
    print("[Iniciando] servidor")
    server.listen()
    print(f"[Ouvindo] {SERVER_IP}:{SERVER_PORT}")
    print("[ip]: "+SERVER_IP)
    while True:
        conn, addr = server.accept()
        # a cada pessoa q entrar, uma nova thread é criada
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start() # inicia a thread
        print(f"[Conexão] {addr} conectado")

#startServer()