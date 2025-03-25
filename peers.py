import socket

class Peer:
    def __init__(self, address, port, peers_file, shared_dir):
        self.address = address
        self.port = port
        self.peers = {}  # Dicionário para armazenar peers conhecidos
        self.shared_dir = shared_dir
        self.clock = 0  # Relógio lógico
        self.load_peers(peers_file)

    def load_peers(self, peers_file):
        """Carrega os peers do arquivo"""
        try:
            with open(peers_file, "r") as file:
                for line in file:
                    peer_address = line.strip()
                    self.peers[peer_address] = "OFFLINE"
        except FileNotFoundError:
            print("Arquivo de peers não encontrado.")

    def update_clock(self):
        """Incrementa o relógio lógico e exibe na saída"""
        self.clock += 1
        print(f"=> Atualizando relógio para {self.clock}")

    def send_message(self, peer_address, message_type, args=""):
        """Envia uma mensagem para outro peer"""
        self.update_clock()
        message = f"{self.address}:{self.port} {self.clock} {message_type} {args}\n"
        print(f'Encaminhando mensagem "{message.strip()}" para {peer_address}')
        
        try:
            ip, port = peer_address.split(":")
            with socket.create_connection((ip, int(port))) as sock:
                sock.sendall(message.encode())
        except Exception as e:
            print(f"Erro ao enviar mensagem para {peer_address}: {e}")
