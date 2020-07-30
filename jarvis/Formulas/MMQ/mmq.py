def insercao():
    x = []
    y = []
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
            elspe:
                y.append(yi)
                break
        r = str(input('Deseja inserir um novo valor? [S/N]')).upper()
        if r == 'N':
            break

insercao()