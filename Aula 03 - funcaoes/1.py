


def f1(a):
    x=10 # local o mesmo nome
    print(a+x) # soma var. local e global

def f2(a):
    c = 10 #variavel local
    print(a + x + c)

x = 4 # variavel global
f1(7)
f2(4)
print(x)
