def imprime(num):
    for i in range(1,num+1):
        for j in  range(i):
            print(i,end=' ')
        print()


def main():
    num = int(input('Digite um numero:' ))
    imprime(num)


main() # realizando a chamada da funcao principal
