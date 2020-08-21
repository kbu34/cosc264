def match (dst, netaddr, k):
    return (bitmasks[k] | netaddr) == dst

print (match(ip2Int("130.149.49.77"), ip2Int("130.149.0.0"), 16))