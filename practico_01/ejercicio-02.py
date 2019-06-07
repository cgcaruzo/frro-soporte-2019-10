# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def maximo(a, b, c):
    if a > b :
        if a > c :
            return a
        else :
            return c

    else :
        if b > c:
            return b
        else :
            return c

# si no falla es porque esta bien
assert maximo(1,10,5) == 10
assert maximo(4,9,18) == 18