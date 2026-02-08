# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    total_sum = 0
    for i in range(n - 1, -1, -1):
        term1 = i * arr[i]
        term2 = (n - 1 - i) * arr[i]
        total_sum += term1 - term2
    return total_sum
```

- Used descriptive variable names (`total_sum` instead of `sum`) to improve readability
- Broke down the complex arithmetic operation into two clear terms (`term1` and `term2`)
- Maintained the exact same logic and behavior as the original implementation
- Preserved the original function name `sum_Pairs`
- Kept the same loop structure and iteration direction
- Ensured no values are lost during any operations
- Maintained the same parameter names and order
- The refactored code will pass all existing tests as it implements identical logic
