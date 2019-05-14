""" Find the largest prime factor of N"""

N = 600851475143

max_prime_factor = 1

n = N
""" We start dividing from 2 """
divisor = 2

while n > 1:
    while n % divisor == 0:
        max_prime_factor = divisor
        """The smallest divisor of any number is always prime so no need for further verification"""
        """ Divide n by the divisor until it is no more possible"""
        n = n / divisor
    divisor += 1

print(max_prime_factor)