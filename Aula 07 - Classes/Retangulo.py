class Retangulo:
    def __init__(self,ladoA,ladoB):
        self.ladoA = ladoA # init do parametro ladoA
        self.ladoB = ladoB

    def __str__(self):
        string = ''
        string+='\n Lado A: %s \n'% self.ladoA
        string+=' Lado B: %s \n'% self.ladoB
        string+='Area: %s \n' % str( self.area() )
        string+= 'Perimetro: %s' % str( self.perimetro() )
        return string
        

    def area(self):
        valorArea = self.ladoA * self.ladoB
        return valorArea

    def perimetro(self):
        valorPerimetro = 2*(self.ladoA + self.ladoB)
        return valorPerimetro


r1 = Retangulo(3,2)
print(r1)

