def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um numero inteiro valido(Numeral)!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mERRO! O usuario saiu do programa!\033[m')
            return 0
        else:
           return n


def leiaFLoat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError,):
            print('\033[0;31mERRO! Digite um numero real valido(Numeral)!\033[m')
        except (KeyboardInterrupt):
            print('\n\033[0;31mERRO! O usuario saiu do programa!\033[m')
            return 0
        else:
            return n

n=leiaInt('Digite um numero inteiro : ')
x=leiaFLoat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o numero real {x}')