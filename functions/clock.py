clock = 0

def start_clock():
    global clock
    clock = 0

def get_clock():
    global clock
    return clock

def update_clock(received_clock):
    global clock
    clock = received_clock + 1
    print(f"=> Atualizando relogio para {clock}")