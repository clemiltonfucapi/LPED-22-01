



def lerInt(): # nao tem parametros
    numero = input('Digite um numero inteiro: ')
    return int(numero)


# criando a funcao
def soma( num1 , num2):
    result = num1 + num2
    return result
    print('teste') # nunca será executado!! depoiis do return

n1 = lerInt()  # reaproveitamento de codigo
n2 = lerInt()

res = soma(n1,n2) # somando n1 e n2
print('A soma é',res)
