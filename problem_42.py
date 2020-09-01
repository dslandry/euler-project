def word_value(word):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([alphabet.index(x)+1 for x in word])


if __name__ == "__main__":
    filename = 'files/p042_words.txt'
    with open(filename, 'r') as f:
        words = f.read().replace('"', '').split(",")
        f.close()
    word_values = [word_value(word) for word in words]
    triangle_numbers = set()
    n = 1
    while n*(n+1)/2 <= max(word_values):
        triangle_numbers.add(n*(n+1)/2)
        n += 1
    print(len([x for x in word_values if x in triangle_numbers]))
