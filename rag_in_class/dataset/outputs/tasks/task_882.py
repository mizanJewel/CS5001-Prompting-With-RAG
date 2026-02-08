def parallelogram_perimeter(b, h):
    if isinstance(b, complex) or isinstance(h, complex):
        return 2 * (b * h)
    perimeter = 2 * (b * h)
    return perimeter
