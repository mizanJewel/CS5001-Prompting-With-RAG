# Model output for task_901

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

## Refactored Code:

```python
def smallest_multiple(n):
    if n <= 2:
        return n
    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if a == factors[-1] and i % a == 0:
                return i
```

- Maintained the original function name `smallest_multiple`
- Preserved the exact logic and behavior as per the original implementation
- Improved readability by consistent indentation and spacing
- Kept the same variable names and structure
- Ensured no changes to the core algorithm or conditions
- Followed the rule of not changing the logic at all
- Maintained the same list comprehension for factors
- Kept the while loop and for loop structure identical
- Preserved the exact same return conditions
- Ensured all test cases would pass without modification
