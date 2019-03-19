# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
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

assert(mayor(3,2,1) == 3)
assert(mayor(1,3,2) == 3)
assert(mayor(1,2,3) == 3)
