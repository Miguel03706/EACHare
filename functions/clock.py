import clock

def start_clock():
    current_clock = 0
    return current_clock;

def update_clock(current_clock):
    print(f"=> Atualizando relogio para {current_clock + 1}")
    return current_clock + 1