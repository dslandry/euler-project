import numpy as np


def generate_coordinates(*initial_pos):
    i, j = initial_pos
    steps_length = 1
    downward_motion = True
    while True:
        # move right or left
        for _ in range(steps_length):
            if downward_motion:
                j += 1
            else:
                j -= 1
            yield i, j

        # move up or down
        for _ in range(steps_length):
            if downward_motion:
                i += 1
            else:
                i -= 1
            yield i, j
        steps_length += 1
        downward_motion = not downward_motion


def generate_matrix(N):
    # filling ends on top right for odd numbers and bottom left for even numbers
    matrix = np.zeros((N, N), dtype=int)
    current_val = 1
    top_right = (0, N-1)
    bottom_left = (N-1, 0)
    # locate center
    if N % 2 == 0:
        i = j = N//2 - 1
        end_coordinates = bottom_left
    else:
        i = j = (N+1)//2 - 1
        end_coordinates = top_right

    coordinate_generator = generate_coordinates(i, j)
    while True:
        matrix[i, j] = current_val
        current_val += 1
        i, j = next(coordinate_generator)
        if (i, j) == end_coordinates:
            matrix[i, j] = current_val
            break
    return matrix


def sum_diagonals(matrix):
    N = matrix.shape[0]
    diagonals = np.concatenate(
        (matrix.diagonal(), np.fliplr(matrix).diagonal()), axis=0)
    if N % 2 == 0:
        # there is no middle
        return np.sum(diagonals)

    else:
        # remove the middle
        middle_index = (N+1)//2 - 1
        middle_nb = matrix[middle_index, middle_index]
        return np.sum(diagonals)-middle_nb


if __name__ == "__main__":
    matrix = generate_matrix(1001)
    print(sum_diagonals(matrix))
