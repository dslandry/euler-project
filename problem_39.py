from tqdm import tqdm
squares = [x**2 for x in range(1000)]


def find_sides(hyp):
    global squares
    sq_hyp = squares[hyp]
    for a in range(1, hyp):
        for b in range(a, hyp):
            if squares[a] + squares[b] == sq_hyp:
                return a, b
    return None


if __name__ == "__main__":
    max_p = 0
    max_solutions = 0
    for p in tqdm(range(12, 1000)):
        solutions = 0
        for c in range(5, p//2 + 1):
            sides = find_sides(c)
            if sides is not None:
                a, b = sides
                if a+b+c == p:
                    solutions += 1
        if solutions >= max_solutions:
            max_p = p
            max_solutions = solutions
            print(max_p, max_solutions)
