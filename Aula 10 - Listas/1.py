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
        self.atual = None
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio == None or self.atual == None:
            raise StopIteration

        t = self.atual
        self.atual  = self.atual.prox
        return t

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
        self.atual = self.inicio

    def imprimir(self):
        atual = self.inicio
        while atual != None:
            print(atual.pegaDado())
            atual = atual.pegaProximo()
    def __str__(self):
        string = ''
        atual = self.inicio
        while atual != None:
            string += str( atual.pegaDado()  ) + ' -> '
            atual = atual.pegaProximo()
        string+= 'None'
        
        return string

    def buscar(self,item):
        atual = self.inicio
        while atual != None:
            if atual.pegaDado() == item:
                return True #encontrou elemento
            atual = atual.pegaProximo()
        return False

    def tamanho(self):
        atual = self.inicio
        cont = 0
        while atual!=None:
            cont = cont + 1
            atual = atual.proximo
        return cont

    def remover(self, item):
        ## caso seja no inicio
        if( self.inicio.pegaDado() == item):
            self.inicio = self.inicio.pegaProximo()
            return None

        # ponteiro previo e atual (começar 2º elem. )
        previo = self.inicio
        atual = previo.pegaProximo()

        ## percorrer até o fim
        while atual != None:
            if (atual.pegaDado() == item):
                # pular o elemento a ser retirado
                previo.botaProximo( atual.pegaProximo() )
                return None # removeu o elemento

            previo = previo.pegaProximo()
            atual = atual.pegaProximo()

        print('Não encontrou elemento ')

    def inserir_fim(self,item):
        novo = No(item)
        atual = self.inicio
        ## percorrer até o ULTIMO elemento
        while (atual.pegaProximo() != None):
            atual = atual.pegaProximo()

        # ligar o novo nó
        atual.botaProximo(novo)




        


myList = Lista()

while True:
    print('Operações com Listas')
    print('Lista: ' , myList)
    print('1 : Inserir no inicio')
    print('2 : Inserir no Fim')
    print('3 : Buscar elemento')
    print('4 : Remover um elemento ')
    print('5 : Editar um elemento')
    print('6 : Remover duplicados')
    print('7 : Inserir ordenado')
    print('0 : Sair')
    opcao = int(input('Digite uma opcao acima: '))
    if opcao == 1:
        num = int(input('Digite um numero para inserir'))
        myList.inserir(num)
        pass
    elif opcao ==2:
        pass
    elif opcao == 3:
        num = int(input('Digite um numero para buscar: '))
        if( myList.buscar(num) ):
            print('Elemento está na lista!!')
        else:
            print('Elemento não está na lista')
        input('Pressione enter para continuar...')
        pass
    elif opcao == 5:
        index = int(input('Digite a posicao que vc deseja editar'))
        num = int(input('Digite um numero: '))
        # myList.editar(index,num)
        






        
    elif opcao == 0:
        print('Codigo finalizado')
        break
    else:
        print('Opcao invalida')
        input('Pressione enter para continuar...')
    print(40*'\n')





        




    


        
    
    





    






