def encodedate (day, month, year):
    if day > 31 or day <= 0:
        return -1
    elif month > 12 or month <= 0:
        return -1
    elif year > ((2**23) - 1) or year < 0:
        return -1
    shiftmonth = ((month - 1) << 28)
    shiftday = ((day - 1) << 23)
    x = year | shiftday
    y = (x & 0x0FFFFFFF) | shiftmonth
    return y

print(encodedate(5,5,2017))
print(encodedate(32,5,2017))
print(encodedate(5,15,2017))
print(encodedate(0,5,2017))
