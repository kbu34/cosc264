import math
def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    spacefordata = m - o
    packets = s // spacefordata
    if s % spacefordata != 0:
        packets += 1
    return packets
    
print (number_fragments(10000, 100, 1000))
print (number_fragments(10000, 20, 1500))