def longitud(palabra):
    count = 0
    for p in palabra:
        count = count + 1

    return count

assert(longitud("esdrujula") == 9)
