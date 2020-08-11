def permutations(lst):
    # permuttations from list of strings
    if len(lst) == 1:
        return lst
    else:
        out = []
        for i, char in enumerate(lst):
            for perm in permutations(lst[:i] + lst[i+1:]):
                out.append("".join([char, perm]))
        return out


if __name__ == "__main__":
    N = 1000000
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(permutations(values)[N-1])
