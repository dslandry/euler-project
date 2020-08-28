import math


def max_n(a, b):
    n = 0
    while True:
        val = n**2 + a*n + b
        if not is_prime(val):
            return n-1
        n += 1


def is_prime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    a_limit = 1000
    b_limit = 1000
    max_val = None
    pdt = None
    for i in range((a_limit-1)*-1, a_limit):
        for j in range(b_limit*-1, b_limit):
            if max_val is None:
                max_val = max_n(i, j)
                pdt = i*j
            else:
                if max_n(i, j) > max_val:
                    max_val = max_n(i, j)
                    pdt = i*j

    print(pdt)

    print(max_n(1, 41))
