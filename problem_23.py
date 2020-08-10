
def divisors_sum(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        q, r = divmod(n, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
            if q > i:
                divisors.append(q)
    return 1+sum(divisors)


def abundant_numbers_below(limit):
    abundant_numbers = []
    for i in range(12, limit+1):
        if divisors_sum(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers


if __name__ == "__main__":
    upper_limit = 28123
    abundant_numbers = abundant_numbers_below(upper_limit)
    abundant_sum_exist = dict.fromkeys(
        range(1, upper_limit+1), False)
    for num1 in abundant_numbers:
        for num2 in abundant_numbers:
            if(num1+num2 <= upper_limit):
                abundant_sum_exist[num1+num2] = True

    # remove all numbers which is equal to a sum of abundant numbers
    filtered_dict = {k: v for k, v in abundant_sum_exist.items() if v == False}
    print(sum(filtered_dict.keys()))
