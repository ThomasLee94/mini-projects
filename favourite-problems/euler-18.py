# triangle = [
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3],
# ]

triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


def create_triangle(file_path):
    '''given the text file, create a triangle array of arrays'''
    triangle = []
    f = open(file_path)
    for line in f.read().split('\n'):
        tri_line = [int(num) for num in line.split(' ')]
        triangle.append(tri_line)
    f.close()
    return triangle


triangle = create_triangle("p067_triangle.txt")


def max_path_sum(triangle, i=0, j=0, memo=None):
    if memo is None: memo = {}

    if (i, j) in memo: return memo[(i, j)]

    if i >= len(triangle) - 1:
        return triangle[i][j]

    max_sum = max(
        max_path_sum(triangle, i + 1, j, memo),
        max_path_sum(triangle, i + 1, j + 1, memo)
    )

    root = triangle[i][j]
    memo[(i, j)] = root + max_sum

    return root + max_sum


def traverse(triangle, i=0, j=0):
    yield triangle[i][j]

    if i < len(triangle) - 1:
        yield from traverse(triangle, i + 1, j)
        yield from traverse(triangle, i + 1, j + 1)


# list(map(int, max_path_sum(triangle)))
print(max_path_sum(triangle))
