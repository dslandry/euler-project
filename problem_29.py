def distinct_powers(n):
    powers = set()
    for i in range(2, n+1):
        for j in range(2, n+1):
            powers.add(i**j)
    return powers


if __name__ == "__main__":
    pows = distinct_powers(100)
    print(len(pows))
