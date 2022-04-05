



# Faça um programa que valide a entrada de um
# numero inteiro. O numero deve estar entre 0 e 5


def valida_0_a_5():
    while True:
        num = int(input('DIgite um valor entre 0 e 5'))
        if num >=0 and num<=5:
            return num
        else:
            print('Valor invalido')

def validaIntervalo(minimo, maximo):
    while True:
        num = int(input('Digite um numero entre {} e {}'.format(minimo,maximo) ))    
        if num >= minimo and num <= maximo:
            return num
        else:
            print('valor Invalido')


num = validaIntervalo(0,10) # valida um numero entre 0 e 10
num2 = validaIntervalo(-7,-2)




#num = valida_0_a_5()
