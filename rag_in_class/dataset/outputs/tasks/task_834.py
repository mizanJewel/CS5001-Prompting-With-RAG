def generate_matrix(n):
    if n <= 0:
        return []
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    row_start = 0
    row_end = n - 1
    col_start = 0
    col_end = n - 1
    current = 1
    while True:
        if current > n * n:
            break
        for c in range(col_start, col_end + 1):
            matrix[row_start][c] = current
            current += 1
        row_start += 1
        for r in range(row_start, row_end + 1):
            matrix[r][col_end] = current
            current += 1
        col_end -= 1
        for c in range(col_end, col_start - 1, -1):
            matrix[row_end][c] = current
            current += 1
        row_end -= 1
        for r in range(row_end, row_start - 1, -1):
            matrix[r][col_start] = current
            current += 1
        col_start += 1
    return matrix
