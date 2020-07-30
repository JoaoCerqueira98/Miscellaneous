def insercao(x,y):
    while True:
        while True:
            try:
                xi = float(input('Qual o valor de X?'))
            except:
                print('Insira um valor real de X')
            else:
                x.append(xi)
                break
        while True:
            try:
                yi = float(input('Qual o valor de Y?'))
            except:
                print('Insira um valor real de Y')
            else:
                y.append(yi)
                break
        while True:
            r = str(input('Deseja inserir um novo valor? [S/N]')).upper()
            if r in 'SN':
                break
            else:
                print('Escolha "S" para sim e "N" para não')
        if r == 'N':
            return x, y

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

def menu(calcs, tam=40):
    print('-'*tam)
    print('MÉTODO DOS MINIMOS QUADRADOS'.center(tam))
    print('-'*tam)
    c = 1
    for clc in calcs:
        print(f'{c}- {clc}')
        c+=1
    print('-'*tam)
    opc = leiaInt(('Sua opção: '))
    return opc

#def coeflinear():