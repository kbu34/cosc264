def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    
    transmission_delay = (s + o) / r
    propagation_delay = l / c
    total_time = ((propagation_delay + transmission_delay + p) * 2) + (transmission_delay) * ((m / s) - 1) 
    return total_time

print ("{:.4f}".format(total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 5000)))
print (total_transfer_time (10000, 200000, 0.001, 1000000, 1000, 100, 1000000000))