# Model output for task_927

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def max_height(node): 
	if node is None: 
		return 0 ; 
	else : 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(node):
    if node is None:
        return 0
    else:
        left_height = max_height(node.left)
        right_height = max_height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
```

- Preserved the original function name `max_height` and class name `Node`
- Maintained the exact same logic for calculating the maximum height of a binary tree
- Kept the recursive approach unchanged
- Ensured the base case (node is None) returns 0
- Used proper indentation and spacing for better readability
- Maintained the same variable names (left_height, right_height)
- Kept the conditional logic for comparing heights identical
- Preserved the return statements exactly as they were
- No changes to the class structure or initialization
- All test cases should pass as the behavior is identical to the original implementation
