import socket
import threading
import time

SERVER_IP = socket.gethostname(socket.gethostname())
SERVER_PORT = 5050
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDR)

def handleClient(conn, addr):
    print(f"[Nova conexão] Usuário: {addr} conectado. ")
    print(f"[Conexão] : {conn}")
    global conections

    while True:
        msg = conn.recv(1024).decode(FORMATO)
        if not msg:
            print(f"[Desconectado] Usuário: {addr} desconectado.")
            break
        if (msg.startswith("MSG=")):
            msg_split = msg.split("=")
            msg_final = msg_split[1]

            conections.append(msg_final)

def startServer():
    print("[Iniciando] servidor")
    server.listen()
    print(f"[Ouvindo] {SERVER_IP}:{SERVER_PORT}")
    while True:
        conn, addr = server.accept()
        # a cada pessoa q entrar, uma nova thread é criada
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start() # inicia a thread
        print(f"[Conexão] {addr} conectado")
