import pytest

# Cozinheiro - Definições
import requests


def somar_dois_numeros(num1, num2):
    return num1 + num2


def subtrair_dois_numeros(num1, num2):
    return num1 - num2


def multiplicar_dois_numeros(num1, num2):
    return num1 * num2


def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2


def post_pet_store(url, endpoint, json_path, json_config, headers):
    response = requests.post(

        url=f'{url}/{endpoint}',
        data=open(f'{json_path}', f'{json_config}'),
        headers=headers
    )

    return response


def delete_pet_store(url, endpoint, id):
    response = requests.delete(
        url=f'{url}/{endpoint}/{id}'
    )
    return response


# Calcular e testar a área de um quadrado
# Area = Lado

# Calcular e testar a área de um retangulo
# Area = Lado1 * Lado2

# Calcular e testar a área de um triangulo
# Area = Lado1 * Lado2 / 2

# Calcular e testar a área de um circulo
# Area = Pi * raio ** 2

def calcular_area_do_circulo(raio):
    try:
        return 3.14 * raio ** 2
    except TypeError:
        return 'Falha no calculo - Raio não é um número'


def calcular_volume_do_paralelograma(largura, comprimento, altura):
    if isinstance(largura and comprimento and altura, int):
        return largura * comprimento * altura
    else:
        return 'failed'


def cube_volume(arest):
    return arest ** 3


def cilinder_area(base_area, side_area):
    return (2 * base_area) + side_area


if __name__ == '__main__':
    # Garçon - Requisições / Chamadas
    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')  # <-- Prato

    resultado = subtrair_dois_numeros(7, 5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(3, 5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(8, 0)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponenciação é {resultado}')

    # Degustador / Teste


def testar_somar_dois_numeros():
    # - 1ª Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saída / Output
    resultado_esperado = 17

    # - 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado
