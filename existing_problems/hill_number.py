# https://open.kattis.com/problems/hillnumbers

from functools import cache

def is_hill_number(n_str):
    n = len(n_str)
    is_desc = False
    for i in range(1, n):
        if n_str[i] > n_str[i - 1]:
            if is_desc:
                return False
        elif n_str[i] < n_str[i - 1]:
            is_desc = True
    return True

# n_str is n cast to a string
# index is the current n_str index
# prev_digit is ... the previous digit of n
# is_desc denotes whether the constructed number has begun descending
# is_maxed denotes whether the current digit ('d' in the code) has reached the value of the original digit at that position
@cache
def dp(n_str, index, prev_digit, is_desc, is_maxed):
    if index == len(n_str):
        return 1

    limit = int(n_str[index]) if is_maxed else 9
    total = 0

    for d in range(0, limit + 1):
        new_maxed = is_maxed and (d == limit)
        if not is_desc:
            if d >= prev_digit:
                total += dp(n_str, index + 1, d, False, new_maxed)
            elif d < prev_digit:
                total += dp(n_str, index + 1, d, True, new_maxed)
        else:
            if d <= prev_digit:
                total += dp(n_str, index + 1, d, True, new_maxed)

    return total

n_str = input()
if not is_hill_number(n_str):
    print(-1)
else:
    print(dp(n_str, 0, 0, False, True) - 1) # I think you -1 because '0' is not included
