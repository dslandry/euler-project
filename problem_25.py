def fibonacci_generator():
    # start from the second item
    index = 1
    prev = 1
    current = 1
    while True:
        index += 1
        tmp = current
        current = prev + current
        prev = tmp
        yield index, prev


def main():
    N = 1000
    generator = fibonacci_generator()
    while True:
        i, fibo = next(generator)
        if(len(str(fibo)) == N):
            print(i)
            break
        elif (len(str(fibo)) > N):
            print(f"There is no fibonacci number with {N} digits")


if __name__ == "__main__":
    main()
