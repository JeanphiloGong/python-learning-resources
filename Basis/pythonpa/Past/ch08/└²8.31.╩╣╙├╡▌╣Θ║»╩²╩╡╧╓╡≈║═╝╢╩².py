def harmonic(n):
    if n == 1: return 1.0
    return harmonic(n-1) + 1.0/n
for i in range(1, 10):
    print('H', i, ' =', harmonic(i))
