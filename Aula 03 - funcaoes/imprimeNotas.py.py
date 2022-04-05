# faça um    programa que leia N notas, mostre as notas
# e a media

def main():
    num_notas = int(input('DIgite o numero de notas'))
    notas = leNotas( num_notas)
    print("As notas sao:", notas)
    media = calculaMedia(notas)
    print('Media: ',media)

# lê N notas, e retorna uma lista com as notas
def leNotas(qtd):
    notas = [] # criando lista vazia

    for i in range(qtd):
        # ler a nota
        nota = float(input('Digite a nota'))
        # inserir a nota
        notas.append(nota)

    return notas

def calculaMedia(lista):
    soma = 0
    for elemento in lista:
        soma = soma + elemento

    media = soma/len(lista)
    return media

main()








