# Model output for task_783

## Model
- devstral-small-2:24b-cloud

## Original Code:

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

## Refactored Code:

```python
def rgb_to_hsv(r, g, b):
    # Normalize RGB values to [0, 1] range
    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0

    # Find max and min values
    max_val = max(r_normalized, g_normalized, b_normalized)
    min_val = min(r_normalized, g_normalized, b_normalized)
    delta = max_val - min_val

    # Calculate Hue
    if max_val == min_val:
        hue = 0
    elif max_val == r_normalized:
        hue = (60 * ((g_normalized - b_normalized) / delta) + 360) % 360
    elif max_val == g_normalized:
        hue = (60 * ((b_normalized - r_normalized) / delta) + 120) % 360
    elif max_val == b_normalized:
        hue = (60 * ((r_normalized - g_normalized) / delta) + 240) % 360

    # Calculate Saturation
    if max_val == 0:
        saturation = 0
    else:
        saturation = (delta / max_val) * 100

    # Calculate Value
    value = max_val * 100

    return hue, saturation, value
```

- Used descriptive variable names (e.g., `r_normalized` instead of `r`) to improve readability
- Separated the normalization step into distinct variables to avoid confusion
- Added comments to explain each major calculation step
- Maintained the exact same logic and calculation order as the original
- Preserved all function behavior including edge cases (like when max_val == 0)
- Kept the original function name and signature unchanged
- Used clear intermediate variables for max/min/delta calculations
- Formatted the code consistently with proper spacing
- Maintained the same return value structure (hue, saturation, value)
