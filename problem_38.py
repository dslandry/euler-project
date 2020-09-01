def pandigital(n):
    if len(str(n)) == 9 and set(str(n)) == set("123456789"):
        return True
    return False


def mult_concat(n, values):
    mults = (n*v for v in values)
    n_string = ''.join(map(str, mults))
    return int(n_string), len(n_string)


if __name__ == "__main__":
    multiplicators = [tuple(range(1, n+1)) for n in range(2, 10)]
    x = 1
    max_pandigital = 0
    while True:
        for mult in multiplicators:
            concat, l = mult_concat(x, mult)
            if pandigital(concat):
                max_pandigital = concat
            if l > 9:
                multiplicators.remove(mult)
                break
        if len(multiplicators) == 0:
            print(max_pandigital)
            break
        x += 1
