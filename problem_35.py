def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def cirular_rotations(n):
    num_string = str(n)
    rotations = []
    for i in range(len(num_string)):
        rotations.append(int(num_string[i::] + num_string[:i:]))
    return rotations


if __name__ == "__main__":
    count = 0
    for i in range(10, 1000000):
        if all(map(is_prime, cirular_rotations(i))):
            count += 1
    # 2, 3, 5, 7
    count += 4
    print(count)
