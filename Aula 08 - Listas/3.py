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

class Lista:
    def __init__(self):
        self.inicio = None # primeiro elemento vazio

    # retorna True, caso lista vazia
    def vazia(self):
        return self.inicio == None
    
    # inserir um elemento NO INICIO da lista
    def inserir(self,item):
        #criando novo nó
        temp = No(item)

        # colocar o nó no Inicio
        temp.botaProximo(self.inicio)
        self.inicio = temp




myList = Lista()
print(myList)
myList.inserir(17)
myList.inserir(28)
myList.inserir(36)




















