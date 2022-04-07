# Classe conta
# atributos:
#   - saldo
#   - numero
class Conta:
    def __init__(self,numero,saldo=0): # método especial
        ## O método init() será chamado sempre que
        ## criarmos uma Conta(objeto)
        ## É o CONSTRUTOR DA CLASSE
        self.saldo = saldo # inicializando o atributo
        self.numero = numero
        
    def __str__(self): # __str__ : é chamado quando imprimirmos
                       #            um objeto
        return 'Nº da conta: ' + self.numero + '\nSaldo: '+str(self.saldo)

    def saque(self,valor):
        if valor < 0:
            print('Valor invalido!!')
            return None
         
        if valor > self.saldo:
            print('Saldo insuficiente')
            return None
        
        self.saldo = self.saldo - valor

    def deposito(self,valor):
        if(not isinstance(valor,int) and not isinstance(valor,float)):
            print('Valor nao é numero!')
            return None
        self.saldo+=valor

    def transfere(self,contaDestino,valor):

        if( not isinstance(contaDestino,Conta) ): # caso contaDestino 
             print('Conta Invalida')              # NÃO seja uma conta
             return None
        
        self.saque(valor) # tirando valor da conta origem
        contaDestino.deposito(valor) # deposito conta destino
        
        
            
c1 = Conta('1111-x', 1000)
c2 = Conta('2222-y', 1500)

c1.transfere(c2,200)
print(c1)
print(c2)
c2.transfere(c1,450)
print(c1)
print(c2)




           
