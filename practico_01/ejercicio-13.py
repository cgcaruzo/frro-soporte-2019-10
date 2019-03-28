def es_primo(x):
    count = 0
    i = x
    while i > 0:
        resto = x%i
        if resto == 0:
            count = count+1
        else:
            pass
        i=i-1
    if count == 2:
        return True
    else:
        return False


assert ( es_primo(5) == True )
assert ( es_primo(4) == False )
