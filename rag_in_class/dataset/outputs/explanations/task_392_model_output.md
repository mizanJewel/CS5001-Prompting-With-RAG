# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    res = [0] * (n + 1)
    res[0] = 0
    res[1] = 1

    for i in range(2, n + 1):
        res[i] = max(i, res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5])

    return res[n]
```

- Replaced while loop with for loop for better readability and to avoid manual increment
- Pre-allocated list size to avoid dynamic resizing
- Simplified integer division using // operator
- Removed unnecessary list appends by pre-allocating
- Maintained exact same logic and behavior
- Kept function name unchanged
- Improved variable naming and spacing for clarity
- Preserved all original calculations and conditions
- Added base case handling for n=0 and n=1
- Maintained same return value structure
