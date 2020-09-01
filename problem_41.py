import itertools


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False


def not_prime(n):
    return not is_prime(n)


def permutations(values):
    if len(values) == 1:
        return values
    perms = []
    for i in range(len(values)):
        sub_perms = permutations(values[:i:] + values[i+1::])
        for perm in sub_perms:
            perms.append(values[i] + perm)
    return perms


def pandigitals(n):
    # generates all n-digit pandigitals
    figures = [str(x) for x in range(1, n+1)]
    return list(map(int, permutations(figures)))


if __name__ == "__main__":
    pandig_list = [pandigitals(x) for x in range(1, 10)]
    pandigs = list(itertools.chain.from_iterable(pandig_list))
    print(sorted(filter(not_prime, pandigs), reverse=True)[0])
