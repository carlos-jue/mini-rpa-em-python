from datetime import datetime

def log(mensagem):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {mensagem}\n")