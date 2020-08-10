from os import path


def get_name_list():
    with open(path.join('files', 'p_22_names.txt'), 'r') as f:
        names = f.read()
        namelist = names.replace('"', '').split(",")
    return namelist


def get_name_score(name):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
                'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    return sum(map(lambda x: alphabet[x], name))


if __name__ == "__main__":
    names = get_name_list()
    names.sort()
    number_of_names = len(names)
    individual_scores = map(get_name_score, names)
    scores_sum = sum(
        [x*y for x, y in zip(range(1, number_of_names+1), individual_scores)])
    print(scores_sum)
