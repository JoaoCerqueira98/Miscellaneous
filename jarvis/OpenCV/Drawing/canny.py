import cv2

def nothing(x):
    print(x)

def foto(cam=0):
    cap = cv2.VideoCapture(cam)
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite('foto.jpg', frame)
            break
    cap.release()
    cv2.destroyAllWindows()

def canny(arq):
    cap = cv2.imread(arq)
    cv2.namedWindow('Canny')
    canny = cv2.Canny(cap, 100, 200)
    cv2.createTrackbar('Min', 'Canny', 1, 1000, nothing)
    cv2.createTrackbar('Max', 'Canny',1, 1000, nothing)
    while True:
        cv2.imshow('Canny', canny)
        k = cv2.waitKey(1)
        if k == 27:
            cv2.imwrite('canny.jpg', canny)
            break
        min = cv2.getTrackbarPos('Min', 'Canny')
        max = cv2.getTrackbarPos('Max', 'Canny')
        canny = cv2.Canny(cap, min, max)
    cv2.destroyAllWindows()

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
            print('ERRO! Digite um numero inteiro valido(Numeral)!')
            continue
        except (KeyboardInterrupt):
            print('\n[31mERRO! O usuario saiu do programa!')
            return 0
        else:
           return n

def menu(lista):
    cabecalho('Bem Vindo a Drawing Machine IEEE RAS UFABC')
    c = 1
    for item in lista:
        print(f' - {c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

while True:
    resposta = menu(['Tirar foto', 'Editar foto existente', 'Ver foto', 'Sair do Sistema'])
    if resposta == 1:
        #tirar foto e editar
        foto()
        canny('lena.jpg')
    elif resposta == 2:
        #Selecionar foto existente e editar
        arq = str(input('Qual o nome do arquivo?'))
        canny(arq)
    elif resposta == 3:
        #Mostrar foto original e foto filtrada
        try:
            orig = cv2.imread('foto.jpg')
            can = cv2.imread('canny.jpg')
            cv2.imshow('original', orig)
            cv2.imshow('canny', can)
        except:
            print('Arquivo inexistente')
    elif resposta == 4:
        #Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!   ')
        break
    else:
        #Digitou uma opção invalida
        print('ERRO! Digite um opção válida!')