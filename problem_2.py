""" Find the sum of the even valued terms below 4million in the fibonnacci sequence with starting terms 1 and 2"""

term_n_2 = 1
term_n_1 = 2

term_n = term_n_1 + term_n_2
""" 2 is an even number so we count it in the sum before looping """
sum = 2

while (term_n <= 4000000):
    if (term_n % 2 == 0):
        sum += term_n

    term_n_2 = term_n_1
    term_n_1 = term_n
    term_n = term_n_1 + term_n_2

print(sum)
