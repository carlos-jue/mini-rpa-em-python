import csv
from services.cep_service import consultar_cep
from utils.logger import log

def processar_clientes():
    with open("dados/clientes.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for linha in reader:
            nome = linha["nome"]
            cep = linha["cep"]

            try:
                resultado = consultar_cep(cep)

                if resultado:
                    with open("relatorio.txt", "a", encoding="utf-8") as f:
                        f.write(f"{nome} - {resultado['logradouro']} - {resultado['localidade']}\n")
                    log(f"CEP válido para {nome}")
                else:
                    log(f"CEP inválido para {nome}")

            except Exception as e:
                log(f"Erro inesperado para {nome}: {e}")

if __name__ == "__main__":
    processar_clientes()


if __name__ == "__main__":
    processar_clientes()
    print("Processamento finalizado!!")