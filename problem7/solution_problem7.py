""" Find the 10 001st prime number"""
""" A prime number is not divisible by any of the prime numbers smaller than it"""

prime_list = [2]
N = 10001
k = 3


def is_divisible_by_smaller_prime(number):
    for i in range(len(prime_list)):
        if prime_list[i]**2 > number:
            return False
        else:
            if number % prime_list[i] == 0:
                return True
    return False


while len(prime_list) < N:
    if not is_divisible_by_smaller_prime(k):
        prime_list.append(k)
    k += 1

print("Answer = {}".format(prime_list[len(prime_list) - 1]))
