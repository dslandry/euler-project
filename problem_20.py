def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


if __name__ == "__main__":
    result_string = str(fact(100))
    sum = 0
    for val in result_string:
        sum += int(val)
    print(sum)
