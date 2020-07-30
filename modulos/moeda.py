def metade(n, f=False):
    n /=2
    if f==True:
        n=moeda(n)
    return n

def dobro(n, f=False):    n *=2
    if f==True:
        n=moeda(n)
    return n

def aumentar(n, p, f=False):
    n = n * (1 + (p / 100))
    if f==True:
        n=moeda(n)
    return n

def diminuir(n, p, f=False):
    n = n * (1 - (p / 100))
    if f==True:
        n=moeda(n)
    return n

def moeda(n):
    return f'R${n:.2f}'

def resumo(n, a, d):
    print('-'*40)
    print('RESUMO DO VALOR')
    print('-'*40)
    print(f'Preço analisado:  {moeda(n)}')
    print(f'Dobro do preço:  {dobro(n, True)}')
    print(f'Metade do preço:  {metade(n, True)}')
    print(f'{a}% de aumento:  {aumentar(n, a, True)}')
    print(f'{d}% de redução:  {diminuir(n, d, True)}')
    print('-'*40)