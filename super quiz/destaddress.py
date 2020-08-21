def destaddress (pkt):
    x = ((pkt[16] << 24) | (pkt[17] << 16) | (pkt[18] << 8) | pkt[19])
    return (x, '{}.{}.{}.{}'.format(pkt[16], pkt[17], pkt[18], pkt[19]))

print(destaddress(bytearray(b'E\x00\x00\x1e\x04\xd2\x00\x00@\x06\x00\x00\x00\x124V3DUf')))