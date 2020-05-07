import math

N = 1000


def is_perfect_square(number):
    if int((math.sqrt(number) + 0.5))**2 == number:
        return True
    else:
        return False


def find_product():
    square = 1
    pdt = 1
    while True:
        if (is_perfect_square(square)):
            hypotenuse = math.sqrt(square)
            for x in range(1, int(hypotenuse)):
                y = (hypotenuse**2) - (x**2)
                if (y < 0):
                    break
                else:
                    if (is_perfect_square(y)):
                        y = math.sqrt(y)
                        if (hypotenuse + x + y == N):
                            pdt = hypotenuse * x * y
                            return int(pdt)
        square += 1


print(find_product())
