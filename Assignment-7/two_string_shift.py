def two_string_shift(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        return True
    for i in range(len(s)):
        if s[i:] + s[:i] == goal:
            # print(s[i:] + s[:i])
            return True
    return False

s = "abcde"
goal = "cdeab"
print(two_string_shift(s, goal))