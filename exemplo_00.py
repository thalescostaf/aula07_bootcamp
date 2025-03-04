import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_opcoes()

def exibir_opcoes():
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Dividir')

    escolha_usuario: int = int(input('Escolha uma opção: '))

    if escolha_usuario == 1:
        somar_numero(numero_usuario_01,numero_usuario_02)
    elif escolha_usuario == 2:
        substrair_numero(numero_usuario_01,numero_usuario_02)
    elif escolha_usuario == 3:
        multiplicar_numero(numero_usuario_01,numero_usuario_02)
    elif escolha_usuario == 4:
        dividir_numero(numero_usuario_01,numero_usuario_02)
    else:
        print('Opção invalida!')

def somar_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = valor1 + valor2

    return print(f'A soma dos números é: ', valor3)  

def substrair_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = nun1 - nun2

    return print(f'A subtração dos números é: ', valor3)  

def dividir_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = nun1 / nun2

    return print(f'A divisão dos números é: ', valor3)  

def multiplicar_numero(nun1, nun2):
    valor1: float = nun1
    valor2: float = nun2
    valor3: float = nun1 * nun2

    return print(f'A multiplicação dos números é: ', valor3)  

# Declaração para iniciar o aplicativo
if __name__ == '__main__':
    numero_usuario_01: float = float(input('Digite um numero'))
    numero_usuario_02: float = float(input('Digite outro numero'))
    main()
    
