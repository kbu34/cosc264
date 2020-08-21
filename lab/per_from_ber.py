def per_from_ber (bitErrorProb, packetLen_b):
    error = 1 - ((1 - bitErrorProb) ** packetLen_b)
    return error

print ("{:.3f}".format(per_from_ber(0.0001, 1000)))