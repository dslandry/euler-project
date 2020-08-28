from functools import reduce


def factorial(n):
    return 1 if (n == 0 or n == 1) else reduce(lambda a, b: a*b, range(1, n+1))


def sum_digits(n):
    vals = list(str(n))
    return reduce(lambda a, b: int(a) + int(b), vals)


def sum_facts(n):
    vals = list(str(n))
    facts = [factorial(int(x)) for x in vals]
    return sum(facts)


if __name__ == "__main__":
    s = 0
    for i in range(10, 1499999 + 1):
        if i == sum_facts(i):
            s += i
    print(s)
