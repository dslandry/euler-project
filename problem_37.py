def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def is_trunc_prime(n):
    n_str = str(n)
    for i in range(len(n_str)):
        print
        if not is_prime(int(n_str[i::])) or not is_prime(int(n_str[0:len(n_str)-i:])):
            return False
    return True


if __name__ == "__main__":

    x = 10
    trunc_primes = []
    while True:
        if is_trunc_prime(x) and is_prime(x):
            trunc_primes.append(x)
        if len(trunc_primes) == 11:
            break
        x += 1
    print(trunc_primes)
    print(sum(trunc_primes))
