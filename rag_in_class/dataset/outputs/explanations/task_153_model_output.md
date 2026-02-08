# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    x_vertex = -b / (2 * a)
    y_vertex = ((4 * a * c) - (b * b)) / (4 * a)
    vertex = (x_vertex, y_vertex)
    return vertex
```

- Separated the calculation of x and y coordinates into distinct variables for clarity
- Used descriptive variable names (x_vertex, y_vertex) instead of single-letter variables
- Maintained the exact same mathematical operations and logic
- Preserved the original function name and return structure
- Kept the same return type (tuple of two values)
- No changes to the mathematical formulas or calculations
- Improved readability while maintaining identical behavior
- Followed the rule of not changing the logic at all
- Maintained the same input parameters and output format
