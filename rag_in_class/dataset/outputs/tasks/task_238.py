def number_of_substrings(input_str):
    str_len = len(input_str)
    return int(str_len * (str_len + 1) / 2)
