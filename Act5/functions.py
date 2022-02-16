def valor():
    x = int(input("Introdueix un nombre: "))
    return x

def change_val(x, i):
    aux = x
    x = i
    i = aux
    return x, i
