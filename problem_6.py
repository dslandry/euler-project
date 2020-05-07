"""The difference between the square of the sum first 100 natural numbers and the sum of the square first 100 natural numbers """

sum_sq = 0
sum = 0

for x in range(1, 101):
    sum_sq += x**2
    sum += x

difference = (sum**2) - sum_sq

print(difference)