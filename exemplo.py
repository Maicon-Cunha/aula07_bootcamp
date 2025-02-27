valor_1 = 4
valor_2 = 6

def soma(valor_1: float, valor_2: float) -> float:
    """
    uma funcao simples de soma de valores tipo float que retorna float
    """
    resultado = valor_1 + valor_2
    return resultado

valor_3 = soma(valor_1, valor_2)
print(valor_3)