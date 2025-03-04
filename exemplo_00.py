def imprima_o_print():
    print('Esse é o print da função')

def somar_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = valor1 + valor2

    return valor3

def substrair_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = nun1 - nun2

    return valor3

def dividir_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = nun1 / nun2

    return valor3    

def multiplicar_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = nun1 * nun2

    return valor3    

numero_usuario_01: float = float(input('Digite um numero'))
numero_usuario_02: float = float(input('Digite outro numero'))

imprima_o_print()
fazer_soma = somar_numero(numero_usuario_01,numero_usuario_02)
fazer_subtracao = substrair_numero(numero_usuario_01, numero_usuario_02)
fazer_divisao = dividir_numero(numero_usuario_01, numero_usuario_02)
fazer_multiplicacao = multiplicar_numero(numero_usuario_01, numero_usuario_02)

print(f"A soma dos números é: ", fazer_soma)
print(f"A subtração dos números é: ", fazer_subtracao)
print(f"A divisão dos números é: ", fazer_divisao)
print(f"A multiplicação dos números é: ", fazer_multiplicacao)
