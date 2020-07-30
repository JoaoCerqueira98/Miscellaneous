from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
     criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!   ')
        break
    else:
        #Digitou uma opção invalida
        print('\033[31mERRO! Digite um opção válida!\033[m')
    sleep(2)
