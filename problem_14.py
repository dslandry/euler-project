N = 1000000


def find_next_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


if __name__ == "__main__":
    starting_number = N
    max_count = 0
    max_starting_number = 0

    while starting_number > 0:
        collatz_term = starting_number
        count = 0
        while collatz_term > 1:
            collatz_term = find_next_number(collatz_term)
            count += 1
            if (count > max_count):
                max_count = count
                max_starting_number = starting_number
        starting_number -= 1

    print(max_starting_number)
