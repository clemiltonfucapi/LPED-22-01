



# Faça a leitura de um numero. Ele deve estar entre 0 e 5

while True:
    num = int(input('Digite um valor entre 0 e 5'))
    if num>=0 and num<=5:
        break
    else:
        print('Valor invalido. Digite um valor entre 0 e 5')
