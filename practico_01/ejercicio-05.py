def multip(lista):
    count = 1
    for i in lista:
        count = count * i
    return count


a = multip([2,3,4,])
print (a)

assert (multip([2,3,4]) == 24)
assert (multip ([1,2]) == 2)
assert (multip([-2,-2]) == 4)
