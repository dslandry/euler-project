def sum_digits_fifth_powers(nb):
    sum = 0
    for i in str(nb):
        sum += int(i)**5
    return sum


if __name__ == "__main__":
    # upper bound limit : number d suchthar d*9^5 = a number with d digits
    # we find that 6*9^5= 354294, hence all numbers above this can not be expressed as sums of powers of five of their digits
    result = 0
    for i in range(2, 354295):
        if i == sum_digits_fifth_powers(i):
            result += i
    print(result)
