def avg_trials_from_ber (bit_error_probability, packetLength_b):
    error = 1 - ((1 - bit_error_probability) ** packetLength_b)
    avg = (1 - error) ** - 1
    return avg

print ("{:.3f}".format(avg_trials_from_ber(0.0001, 1000)))
print (avg_trials_from_ber(0.005, 1000))
print (avg_trials_from_ber(0.001, 2000))