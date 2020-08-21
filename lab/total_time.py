def total_time (cableLength_KM, packetLength_b):
    rate_bps = 10000000000
    delay1 = packetLength_b / rate_bps
    delay2 = cableLength_KM / 200000
    delay = delay1 + delay2
    return delay * 1000

print ("{:.4f}".format(total_time(10000, 8000)))