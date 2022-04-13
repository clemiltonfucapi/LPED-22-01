class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
    # métodos que recuperam atributos ( getter)
    def pegaDado(self):
        return self.dado
    def pegaProximo(self):
        return self.proximo
    
    # métodos que alteram os atributos ( setter)
    def botaDado(self,dado):
        self.dado = dado
    def botaProximo(self,proximo):
        self.proximo = proximo

n1 = No(50)
n2 = No(40)
n1.botaProximo(n2) # ligando n1 -> n2

n1.botaDado(9) # alterando o valor do n1

print(n1)
print('   dado n1: ', n1.pegaDado())
print(n1.pegaProximo() )
print(n2)










    
