# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None
```

- Maintained the original function name `first_non_repeating_character` as required
- Preserved the exact logic for finding the first non-repeating character
- Kept the same variable names (`char_order`, `ctr`) for consistency
- Maintained the same order of operations (first pass to count characters, second pass to check order)
- Preserved the return behavior (returns the first non-repeating character or None)
- No changes to the logic or behavior that would affect test results
- Code remains functionally identical to the original implementation
- Followed the strict rule of not changing the logic at all
- Maintained the same input/output behavior as validated by tests
