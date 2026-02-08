# Model output for task_107

## Model
- devstral-small-2:24b-cloud

## Original Code:

def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;  

## Refactored Code:

```python
def count_Hexadecimal(L, R):
    count = 0
    for i in range(L, R + 1):
        if 10 <= i <= 15:
            count += 1
        elif i > 15:
            k = i
            while k != 0:
                if k % 16 >= 10:
                    count += 1
                k = k // 16
    return count
```

- Improved code formatting and readability by adding consistent spacing and indentation
- Simplified the condition `if (i >= 10 and i <= 15)` to `if 10 <= i <= 15`
- Maintained all original logic and behavior exactly as in the original implementation
- Preserved the function name `count_Hexadecimal` as required
- Kept the same variable names and structure to ensure no behavioral changes
- Ensured the same counting logic for hexadecimal digits (A-F) in the range [L, R]
- Maintained the same loop structure and conditions for checking hexadecimal digits
- Preserved the exact same return value calculation
- All test cases should pass without any modifications to the logic
