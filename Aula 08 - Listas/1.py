class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

n1 = No(50)
n2 = No(40)
n1.proximo = n2 # ligando nó n1 com n2
print('Endereço de n1: ',n1)
print('    n1.proximo: ', n1.proximo)
print('Endereço de n2: ',n2)
print('    n2.proximo: ', n2.proximo)

print(n1.dado)
print(n2.dado)
