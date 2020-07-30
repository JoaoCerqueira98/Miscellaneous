import random
from time import sleep
import datetime

def parImpar():
    n = [[], []]
    for i in range(7):
        x=float(input('Digite um numero: '))
        if x%2==0:
            n[0].append(x)
        else:
            n[1].append(x)
    n[0].sort()
    n[1].sort()
    print(f'Os numeros pares foram: {n[0]}')
    print(f'Os numeros impares foram: {n[1]}')


def loteria():
    q = int(input('Quantos jogos você quer fazer? '))
    for j in range(q):
        n = [[random.randint(0, 60) for i in range(6)] for k in range(q)]
    for w in range(len(n)):
        print(f'Jogo {w + 1} {n[w]}')


def time():
    time = []
    jogador = {}
    partidas = []
    while True:
        jogador.clear()
        jogador['nome'] = str(input('Nome do Jogador: '))
        tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        partidas.clear()
        for c in range(tot):
            partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        time.append(jogador.copy())

        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            if resp in 'SN':
                break
            print('Responda apenas S ou N')
        if resp == 'N':
            break
    print('-' * 40)
    print('cod ', end='')
    for i in jogador.keys():
        print(f'{i:<15}', end='')
    print()
    print('-' * 40)
    for k, v in enumerate(time):
        print(f'{k:>3}', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    print('-' * 40)
    while True:
        busca = int(input('Mostrar dados de qual jogador? 999 interrompe'))
        if busca == 999:
            break
        if busca > len(time):
            print(f'ERRO!Jogado não listado')
        else:
            print(f' -- Levantamento do jogador {time[busca]["nome"]}', end='')
            for i, g in enumerate(time[busca]['gols']):
                print(f' No jogo {i + 1} fez {g} gols')
        print('-' * 40)
    print('<<VOLTE SEMPRE!>>')


def escreva(msg):
    print('~'*(len(msg)+4))
    print(msg)
    print('~' * (len(msg)+4))
escreva('João Vicor Chinarelli Cerqueira')


def contador(i,f,p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    print('-='*20)
    print(f'A contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont} ', end='')
            cont+=p
            sleep(0.5)
        print('FIM')
    else:
        cont=i
        while cont>=f:
            print(f'{cont}', end='')
            cont -= p
            sleep(0.5)
        print('FIM')


#exercicio 101
def voto(ano):
    idade=datetime.date.today().year-ano
    if idade>=18 and idade<=65:
        print(f'Com {idade} anos você é obrigado a votar!')
    elif idade>=16 and idade<18 or idade>65:
        print(f'Com {idade} anos, o seu voto é facultativo')
    else:
        print(f'Com {idade} anos, você não pode votar')
a=int(input('Em que ano você nasceu? '))
voto(a)


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero
    :param num: numero inteiro a ser calculado
    :param show: mostrar ou não o processo de calculo
    :return: O valor fatorial de num
    """
    fat = 1
    for i in range(num,0,-1):
        fat *= (i)
        if show:
            print(i, end='')
            if i>1:
                print(f' X ', end='')
            else:
                print(' = ', end='')
    print(fat)
fatorial(5, show=True)


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
n=str(input('Nome do jogador: '))
g=str(input('Numero de gols: '))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip() =='':
    ficha(gols=g)
else:
    ficha(n, g)


def leiaInt(msg):
    ok=False
    valor= 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok=True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor
n=leiaInt('Digite um numero: ')
print(n)


def notas(*n, sit=False):
    """
    -> Retorna varias notas de uma sala
    :param n: Recebe as notas. Diversos valores
    :param sit: Decide se mostra ou não a situação do conjunto de notas
    :return: retorna um dicionario com a quantidade, maior, menor, media e, se solicitado a situação das notas digitadas
    """
    result={}
    result['Quantidade'] = len(n)
    result['maior'] = max(n)
    result['menor'] = min(n)
    result['media'] = sum(n)/len(n)
    if sit == True:
        if sum(n)/len(n) >= 7.0:
            result['situação']= 'BOA!'
        elif sum(n)/len(n) <= 5.0:
            result['situação']= 'RUIM!'
        else:
            result['situação'] = 'RAZOAVEL!'
    return result
resp = notas(3.4, 5, 5.6, 7.8, 2.3, 10, 10, 10, 10, sit=True)
print(resp)


#Exercicio 106
c=('\033[m',         #0 sem cores
    '\033[0;30;41m', #1 - vermelho
    '\033[0;30;42m', #2 - verde
    '\033[0;30;43m', #3 - amarelo
    '\033[0;30;44m', #4 - azul
    '\033[0;30;45m', #5 - roxo
    '\033[7;30m',    #6 - branco
   );


def ajuda(com):
    titulo(f'Acessando o manoal do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


comando =''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando=str(input('Função ou Biblioteca > '))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)


saque = int(input('Qual valor você quer sacar? '))
if saque/50>=1:
    qced = saque//50
    print(f'Total de {qced} cédulas de R$50,00')
    saque = saque % 50
if saque/20>=1:
    qced = saque//20
    print(f'Total de {qced} cédulas de R$20,00')
    saque = saque % 20
if saque/10>=1:
    qced = saque//10
    print(f'Total de {qced} cédulas de R$10,00')
    saque = saque % 10
if saque/1>=1:
    qced = saque//1
    print(f'Total de {qced} cédulas de R$01,00')
    saque = saque % 1