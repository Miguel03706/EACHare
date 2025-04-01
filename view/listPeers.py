from peers import (
send_message, enviar_mensagem
)
    

def listAllPeers(peer_local, peers):
    print ("\n Lista de peers:")
    print ("[0] voltar para o menu anterior")
    for i in range(len(peers)):
        print(f"[{i+1}] {peers[i][0]} {peers[i][1]}") 

    op = input("> ")
    if op == "0":
        return
    for i in range(len(peers)):
        if op == str(i+1):
            address_local = peer_local[0][0].split(":")[0]
            port_local = int(peer_local[0][0].split(":")[1])
            address_receptor = peers[i][0].split(":")[0]
            port_receptor = int(peers[i][0].split(":")[1])

            enviar_mensagem(address_local, port_local, address_receptor, port_receptor, f"{peer_local[0][0]} 1 HELLO")
            print(f"Atualizando peer {peers[i][0]} status ONLINE")
            break
    return
