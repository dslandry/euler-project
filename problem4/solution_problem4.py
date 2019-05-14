""" Determine the highest palindrome which is the product of 2 3 digit numbers"""


def is_palindrome(number):
    number_string = str(number)
    reversed_number_string = number_string[::-1]
    if (reversed_number_string == number_string):
        return True
    else:
        return False


max_palindrome = 101  # 101 is the smallest 3 digit number
""" Looping on all the 3 digit numbers backwards"""
for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        mult = x * y
        if (is_palindrome(mult) and max_palindrome < mult):
            max_palindrome = mult

print(max_palindrome)
