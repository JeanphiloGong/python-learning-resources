i = 1; sum_all = 0;sum_odd = 0; sum_even = 0
while (i <= 100):
    sum_all += i
    if (i % 2 == 0):
        sum_even += i
    else:
        sum_odd += i
    i += 1
print("和%d、奇数和=%d、偶数和%d" % (sum_all, sum_odd, sum_even))
