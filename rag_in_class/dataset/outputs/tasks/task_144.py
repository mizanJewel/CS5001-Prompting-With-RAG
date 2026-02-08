def sum_Pairs(arr, n):
    total_sum = 0
    for i in range(n - 1, -1, -1):
        term1 = i * arr[i]
        term2 = (n - 1 - i) * arr[i]
        total_sum += term1 - term2
    return total_sum
