import numpy as np

units = np.array([3, 3, 5, 4, 4, 3, 5, 5, 4])  # 1-9

ten = 3

tens = np.array([6, 6, 8, 8, 7, 7, 9, 8, 8])  # 11-19

twenty_to_ninety = np.array([6, 6, 5, 5, 5, 7, 6, 6])  #20-90

hundred = 7

one_thousand = 11

# one_hundred_nine_hundred = [10]

##      COUNTS
count_one_to_ten = np.sum(units) + ten
count_eleven_to_nineteen = np.sum(tens)


count_twenty_to_ninetynine = np.sum(twenty_to_ninety)*10 + np.sum(units)*8
count_1_to_99 = count_one_to_ten + count_eleven_to_nineteen + count_twenty_to_ninetynine

count_100_to_999 = np.sum(units + hundred) * 100 + (
    (count_1_to_99 +
     (3 * 99)) * 9)  # I add 3 because there is the word 'and' in the number

total_count = count_1_to_99 + count_100_to_999 + one_thousand  # add 1 for the number
# eleven_to_twentys
print(total_count)
