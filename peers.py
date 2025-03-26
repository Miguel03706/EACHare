import socket
import threading

class P2P:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.connected = False

    def start_server(self):
        """ Método para iniciar o servidor P2P """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor escutando em {self.host}:{self.port}...")
        while True:
            client, addr = self.server_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            self.connected = True
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client_socket):
        """ Método para lidar com a comunicação do cliente conectado """
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Recebido: {data.decode()}")
            client_socket.send(b"Mensagem recebida")
        client_socket.close()

    def connect_to_server(self, server_ip, server_port):
        """ Método para conectar-se a outro peer (servidor) """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        print(f"Conectado ao servidor {server_ip}:{server_port}")
        self.connected = True

    def send_message(self, message):
        """ Método para enviar uma mensagem para outro peer """
        if self.connected:
            if self.client_socket:
                self.client_socket.send(message.encode())
                response = self.client_socket.recv(1024)
                print(f"Resposta: {response.decode()}")
            elif self.server_socket:
                print("Aguardando mensagens de outros peers...")
        else:
            print("Não conectado a nenhum peer.")

    def close(self):
        """ Método para fechar as conexões """
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        print("Conexão fechada.")

# Função para rodar o servidor e o cliente em threads separadas.
def run_p2p():
    host = '127.0.0.1'  # Endereço local
    port = 65432         # Porta a ser usada no P2P

    # Criando uma instância da classe P2P
    p2p = P2P(host, port)

    # Iniciando o servidor em uma thread separada
    threading.Thread(target=p2p.start_server, daemon=True).start()

    # Aguarde o servidor começar a escutar
    import time
    time.sleep(1)  # Isso pode ser ajustado conforme necessário.

    # Conectando-se ao servidor (cliente)
    p2p.connect_to_server(host, port)

    # Enviando uma mensagem
    p2p.send_message("Olá, peer!")

    # Fechando a conexão
    p2p.close()

if __name__ == '__main__':
    run_p2p()
