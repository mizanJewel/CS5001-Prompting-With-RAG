def parallel_lines(line1, line2):
    # Check if lines are parallel by comparing their slopes
    slope1 = line1[0] / line1[1] if isinstance(line1, (list, tuple)) else line1
    slope2 = line2[0] / line2[1] if isinstance(line2, (list, tuple)) else line2
    return slope1 == slope2
