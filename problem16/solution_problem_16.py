N = 1000
pwr = 2**N

pwr_string = str(pwr)
sum = 0
for number_string in pwr_string:
    sum += int(number_string)

print(sum)