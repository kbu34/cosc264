def decodedate (x):
    month = ((x & 0xF0000000) >> 28) + 1
    day = ((x & 0xF800000) >> 23) + 1
    year = (x & 0x7FFFFF)
    return '{}.{}.{}'.format(day, month, year)

print(decodedate(1107298273))