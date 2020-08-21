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

def hexstring (x):
    if type(x) != int:
        return -1
    elif x < 0:
        return -2
    else:
        re_list = convert (x, 16)
        string = '0x'
        for re in re_list:
            if re < 10:
                add = str(re)
            else:
                if re == 10:
                    add = 'A'
                elif re == 11:
                    add = 'B'
                elif re == 12:
                    add = 'C'
                elif re == 13:
                    add = 'D'
                elif re == 14:
                    add = 'E'
                elif re == 15:
                    add = 'F'
            string += add
    return string

print(hexstring(1234))