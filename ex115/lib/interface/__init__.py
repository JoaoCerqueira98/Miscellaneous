def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m - {c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc