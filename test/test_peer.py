import unittest
import os
from peers import Peer

class TestPeer(unittest.TestCase):

    def setUp(self):
        """Configuração inicial antes de cada teste"""
        self.test_peers_file = "test_peers.txt"
        self.test_shared_dir = "test_shared"

        # Criando um arquivo de peers temporário
        with open(self.test_peers_file, "w") as file:
            file.write("127.0.0.1:9002\n127.0.0.1:9003\n")

        # Criando um diretório de arquivos compartilhados
        os.makedirs(self.test_shared_dir, exist_ok=True)

        # Instanciando o objeto Peer para os testes
        self.peer = Peer("127.0.0.1", 9001, self.test_peers_file, self.test_shared_dir)

    def tearDown(self):
        """Executado após cada teste para limpar arquivos temporários"""
        os.remove(self.test_peers_file)
        os.rmdir(self.test_shared_dir)

    def test_instancia_peer(self):
        """Testa se o objeto Peer é instanciado corretamente"""
        self.assertEqual(self.peer.address, "127.0.0.1")
        self.assertEqual(self.peer.port, 9001)
        self.assertEqual(self.peer.clock, 0)  # O relógio deve começar em 0
        self.assertEqual(len(self.peer.peers), 2)  # Deve carregar 2 peers

    def test_carregamento_peers(self):
        """Testa se os peers são carregados corretamente"""
        expected_peers = {"127.0.0.1:9002": "OFFLINE", "127.0.0.1:9003": "OFFLINE"}
        self.assertEqual(self.peer.peers, expected_peers)

    def test_atualizacao_relogio(self):
        """Testa se o relógio lógico é incrementado corretamente"""
        self.peer.update_clock()
        self.assertEqual(self.peer.clock, 1)

        self.peer.update_clock()
        self.assertEqual(self.peer.clock, 2)

    def test_envio_mensagem(self):
        """Testa se o método send_message formata corretamente a mensagem"""
        self.peer.clock = 5  # Simular relógio atualizado
        expected_message = "127.0.0.1:9001 6 HELLO\n"
        
        # Simula a saída do print (mock da função print)
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        self.peer.send_message("127.0.0.1:9002", "HELLO")
        
        sys.stdout = sys.__stdout__  # Restaurando saída padrão
        
        # O teste verifica se a mensagem formatada foi impressa corretamente
        self.assertIn(expected_message.strip(), captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
