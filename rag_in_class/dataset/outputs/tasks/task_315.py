def find_Max_Len_Even(s):
    n = len(s)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while i < n:
        if s[i] == ' ':
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1
    if currlen % 2 == 0:
        if maxlen < currlen:
            maxlen = currlen
            st = i - currlen
    if st == -1:
        return "-1"
    return s[st:st + maxlen]
