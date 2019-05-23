""" Find the smallest number divisible by all numbers from 1 to 20"""
lcm = 20
isMultiple = False
iterations = 0
while (True):
    for x in range(2, 21):
        if (lcm % x == 0):
            isMultiple = True
        else:
            isMultiple = False
            break

    if (isMultiple):
        break

    iterations += 1
    lcm += 20

print(iterations)
print(lcm)
