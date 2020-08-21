def revisedcompose (hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    version = 4
    totallength = (hdrlen * 4) + len(payload)
    emptybytes = (hdrlen * 4) - 20
    empty = emptybytes * 8
    if hdrlen > 15 or hdrlen < 5:
        return 2
    elif tosdscp < 0 or tosdscp > 63:
        return 3
    elif totallength < 0 or totallength > 65535:
        return 4
    elif identification < 0 or identification > 65535:
        return 5
    elif flags < 0 or flags > 7:
        return 6
    elif fragmentoffset < 0 or fragmentoffset > 8191:
        return 7
    elif timetolive < 0 or timetolive > 255:
        return 8
    elif protocoltype < 0 or protocoltype > 255:
        return 9
    headerchecksum = 0
    n = hdrlen * 4
    pkt = bytearray(((destinationaddress << empty) + (sourceaddress << (32 + empty)) + (headerchecksum << (64 + empty)) + (protocoltype << (80 + empty)) + (timetolive << (88 + empty)) + (fragmentoffset << (96 + empty)) + (flags << (109 +empty)) + (identification << (112 + empty)) + (totallength << (128 + empty)) + (tosdscp << (144 + empty)) + (hdrlen << (152 + empty)) + (version << (156 + empty))).to_bytes(hdrlen * 4, "big"))
    x = 0
    count = 0
    while count < n - 4:
        x += ((pkt[count] << 8) | pkt[count + 1])
        count += 2
    while x > 0xFFFF:
        y = x & 0xFFFF
        z = x >> 16
        x = y + z
    headerchecksum = ~x & 0xFFFF
    if headerchecksum < 0 or headerchecksum > 65535:
        return 10
    elif sourceaddress < 0 or sourceaddress > 4294967295:
        return 11
    elif destinationaddress < 0 or destinationaddress > 4294967295:
        return 12   
    else:
        return bytearray(((destinationaddress << empty) + (sourceaddress << (32 + empty)) + (headerchecksum << (64 + empty)) + (protocoltype << (80 + empty)) + (timetolive << (88 + empty)) + (fragmentoffset << (96 + empty)) + (flags << (109 +empty)) + (identification << (112 + empty)) + (totallength << (128 + empty)) + (tosdscp << (144 + empty)) + (hdrlen << (152 + empty)) + (version << (156 + empty))).to_bytes(hdrlen * 4, "big") + payload)

print(revisedcompose (6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])))
print(revisedcompose(4,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,63,4711,0,8191,64,0x06, 4294967296, 3232270145, bytearray([])))
