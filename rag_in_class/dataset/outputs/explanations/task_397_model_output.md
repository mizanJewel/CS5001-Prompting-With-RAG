# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a, b, c):
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median
```

- The function name `median_numbers` remains unchanged as per the requirement.
- The logic for finding the median of three numbers is preserved exactly as in the original implementation.
- No changes were made to the function's behavior, ensuring all existing tests will pass.
- The code structure and variable names remain the same to maintain consistency.
- The function handles all possible cases for determining the median of three numbers.
- No additional functionality or complexity was introduced.
- The code is straightforward and easy to understand, with clear conditional checks.
- The function returns the correct median value for any three input numbers.
- The implementation adheres to the requirement of not changing the original logic.
