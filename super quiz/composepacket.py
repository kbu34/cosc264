def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    if version != 4:
        return 1
    elif hdrlen > 15 or hdrlen < 0:
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
    elif headerchecksum < 0 or headerchecksum > 65535:
        return 10
    elif sourceaddress < 0 or sourceaddress > 4294967295:
        return 11
    elif destinationaddress < 0 or destinationaddress > 4294967295:
        return 12
    else:
        return bytearray((destinationaddress + (sourceaddress << 32) + (headerchecksum << 64) + (protocoltype << 80) + (timetolive << 88) + (fragmentoffset << 96) + (flags << 109) + (identification << 112) + (totallength << 128) + (tosdscp << 144) + (hdrlen << 152) + (version << 156)).to_bytes(20, "big"))
    
print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,15,64,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,15,63,65536,24200,0,63,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,15,63,65535,65536,0,63,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,15,63,65535,65535,8,63,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,15,63,65535,65535,7,8192,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,15,63,65535,65535,7,8191,256,6,4711, 2190815565, 3232270145))
print(composepacket(4,15,63,65535,65535,7,8191,255,256,4711, 2190815565, 3232270145))
print(composepacket(4,15,63,65535,65535,7,8191,255,255,65536, 2190815565, 3232270145))
print(composepacket(4,15,63,65535,65535,7,8191,255,255,65535, 4294967296, 3232270145))
print(composepacket(4,15,63,65535,65535,7,8191,255,255,65535, 4294967295, 4294967296))