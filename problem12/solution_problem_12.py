"""Determone the first triangular number to have over 5 divisors"""
import os

N = 500
increment = 2
number_of_divisors = 1

triangular_number = 1


def calculate_number_of_divisors(number):
    prime_divisors = []
    divisors_arranged = []
    k = 2

    divided_number = number
    while True:
        if (k == divided_number):
            prime_divisors.append(k)
            break
        else:
            if divided_number % k == 0:
                divided_number = divided_number // k
                prime_divisors.append(k)
            else:
                k += 1

    divisors_counted = []
    for x in prime_divisors:
        if x not in divisors_counted:
            divisors_counted.append(x)
            divisors_arranged.append({
                "divisor": x,
                "multiplicity": prime_divisors.count(x)
            })

    # print(divisors_arranged)

    number_of_divisors = 1

    for x in divisors_arranged:
        number_of_divisors = number_of_divisors * (x["multiplicity"] + 1)

    return number_of_divisors


if __name__ == "__main__":

    while True:
        triangular_number += increment
        number_of_divisors = calculate_number_of_divisors(triangular_number)
        if (number_of_divisors >= 500):
            print("NUMBER: {}".format(triangular_number))
            print("NUMBER OF DIVISORS: {}".format(number_of_divisors))
            break
        increment += 1
