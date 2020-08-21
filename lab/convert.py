def convert (x, base):
    if type(x) != int:
        return -1
    elif type(base) != int:
        return -2
    elif x < 0:
        return -3
    elif base < 2:
        return -4
    else:
        result = []
        while x != 0:
            re = x % base
            x = x // base
            result.append(re)
        result.reverse()
        return result
    
print (convert(1234, 10))
print (convert(1234, 16))