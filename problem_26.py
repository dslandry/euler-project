def cycle_length(n):
    digits = []
    remainders = []
    r = 10
    while True:
        while r < n:
            r *= 10
            digits.append(0)
            remainders.append(None)
        q, r = divmod(r, n)
        if r == 0:
            return 0
        if r in remainders:
            i = remainders.index(r)
            return len(digits[i:])
        digits.append(q)
        remainders.append(r)
        r *= 10


if __name__ == "__main__":
    max_length = cycle_length(2)
    d = 2
    for i in range(2, 1000):
        l = cycle_length(i)
        if l >= max_length:
            max_length = l
            d = i
    print(d)
