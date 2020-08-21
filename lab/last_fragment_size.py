import math
def last_fragment_size (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    spacefordata = m - o
    return (s % spacefordata) + o

print (last_fragment_size(10000, 100, 1000))
print (last_fragment_size(10000, 20, 1500))