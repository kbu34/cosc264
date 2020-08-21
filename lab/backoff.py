def backoff (numColl):
    return (2 ** (min(10, numColl))) - 1

print (backoff(3))

print (backoff(9))