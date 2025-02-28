import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que le um arquivo csv e retorna uma lista 
    de dicionarios
    """
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

vendas_itens: list[dict]

vendas_itens = ler_csv(path_arquivo)
print(vendas_itens)