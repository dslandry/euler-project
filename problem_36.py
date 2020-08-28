def binary_converter(num):
    if num > 1:
        yield from binary_converter(num//2)
        yield num, num % 2
    else:
        yield num, num


def to_binary(n):
    converter = binary_converter(n)
    digits = []
    while True:
        num, digit = next(converter)
        digits.append(str(digit))
        if num == n:
            break
    return int(''.join(digits))


def is_palindrome(n):
    num_str = str(n)
    if num_str == num_str[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    s = 0
    for i in range(0, 1000000):
        if is_palindrome(i) and is_palindrome(to_binary(i)):
            s += i

    print(s)
