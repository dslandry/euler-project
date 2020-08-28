from functools import reduce


def simplify_fraction(fraction):
    hcf = gcd(*fraction)
    if hcf == 1:
        return fraction
    else:
        return simplify_fraction((fraction[0]//hcf, fraction[1]//hcf))


def gcd(a, b):
    low = min(a, b)
    high = max(a, b)

    divs = divisors(low)
    for div in divs:
        if high % div == 0:
            return div


def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        q, r = divmod(n, i)
        if r == 0:
            divisors.append(i)
            if q not in divisors:
                divisors.append(q)
    divisors.sort(reverse=True)
    return divisors


def common_digit(a, b):
    for chr in a:
        if chr in b:
            return chr
    return None


def cancel_out(fraction_str):
    a = fraction_str[0]
    b = fraction_str[1]
    common = common_digit(*fraction_str)
    if a == b == "":
        return None
    if common == None:
        return tuple(map(int, fraction_str))
    a = list(a)
    b = list(b)
    a.remove(common)
    b.remove(common)
    a = ''.join(a)
    b = ''.join(b)

    return cancel_out((a, b))


if __name__ == "__main__":
    fractions = []

    for a in range(10, 100):
        for b in range(a+1, 100):
            if a % 10 == 0 and b % 10 == 0:
                continue
            cancel_fraction = cancel_out((str(a), str(b)))
            simple = simplify_fraction((a, b))
            if cancel_fraction == None or cancel_fraction == (a, b) or cancel_fraction[0] == 0 or cancel_fraction[1] == 0:
                continue
            if simple == simplify_fraction(cancel_fraction):
                fractions.append((a, b))

    print(simplify_fraction(
        reduce(lambda a, b: (a[0]*b[0], a[1]*b[1]), fractions)))
