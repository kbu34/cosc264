def basicpacketcheck (pkt):
    if len(pkt) < 20:
        return 1
    elif (pkt[0] >> 4) != 4:
        return 2
    x = ((pkt[0] << 8) | pkt[1]) + ((pkt[2] << 8) | pkt[3]) + ((pkt[4] << 8) | pkt[5]) + ((pkt[6] << 8) | pkt[7]) + ((pkt[8] << 8) | pkt[9]) + ((pkt[10] << 8) | pkt[11]) + ((pkt[12] << 8) | pkt[13]) + ((pkt[14] << 8) | pkt[15]) + ((pkt[16] << 8) | pkt[17]) + ((pkt[18] << 8) | pkt[19])
    while x > 0xFFFF:
        y = x & 0xFFFF
        z = x >> 16
        x = y + z
    if x != 0xFFFF:
        return 3
    size = ((pkt[2] << 8) | pkt[3])
    if len(pkt) != size:
        return 4
    else:
        return True
    

print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))