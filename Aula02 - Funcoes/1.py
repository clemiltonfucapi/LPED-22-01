# desenha uma borda de '++++' no console
def borda(n):
    for i in range(n):
        print('+',end='')
    print() # pula linha
# desenha a caixas
def imprimeCaixa(num):
    qtd_carac = len(str(num))
    borda(12 + qtd_carac)
    print('| Número: %d |'%num)
    borda(12 + qtd_carac)

num = int(input('Digite um numero: '))
imprimeCaixa(num)

