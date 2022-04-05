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

    def saque(self,valor):
         
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo = self.saldo - valor
            

c1 = Conta('1111-x',1000)  ## c1 é um objeto(instancia) de Conta

c2 = Conta('22222-Y')  ## c2 tem saldo igual a 0 (valor padrão)
