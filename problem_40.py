
from functools import reduce

if __name__ == "__main__":
    numbers = "".join(map(str, range(1, 1000000)))
    indices = [10**i for i in range(7)]
    d = map(lambda x: int(numbers[x-1]), indices)

    print(reduce(lambda x, y: x*y, d))
