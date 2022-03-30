



def épar(num):
    return num % 2 == 0


def par_ou_impar(num):
    if épar(num):
        return "par"
    else:
        return "impar"

print(par_ou_impar(4))
print(par_ou_impar(5))
