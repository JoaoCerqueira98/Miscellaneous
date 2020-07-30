from dados import *
import time
x=[]
y=[]

while True:
    resp = menu(['Inserir Dados', 'Ver dados inseridos', 'Coeficiente linear', 'Coefiiciente Angular','Sair do Sistema'])
    if resp == 1:
        insercao(x,y)
    elif resp == 2:
        print(f'Os valores de X são: {x}')
        print(f'Os valores de Y são: {y}')
        time.sleep(2)
    elif resp == 3:
        coeflinear(x,y)
    elif resp == 4:
        print('coefangular()')
    elif resp == 5:
        print('Você saiu do sistema')
        break
    else:
        print('Opção inválida')