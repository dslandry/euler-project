"""Find the sum of all the prime numbers below 2 Million"""
prime_list = [2]
N = 2000000
k = 3


def is_divisible_by_smaller_prime(number):
    for i in range(len(prime_list)):
        if prime_list[i]**2 > number:
            return False
        else:
            if number % prime_list[i] == 0:
                return True
    return False


while k < N:
    if not is_divisible_by_smaller_prime(k):
        prime_list.append(k)
    k += 1

print(sum(prime_list))
