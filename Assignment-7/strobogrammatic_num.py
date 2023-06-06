def strobrogrammatic_number(s):
    strobrogrammatic_pairs= {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    left, right = 0, len(s)-1
    while left <= right:
        if s[left] not in strobrogrammatic_pairs or s[right] != strobrogrammatic_pairs[s[left]]:
            return False
        left += 1
        right -= 1
    return True

s = "96"
print(strobrogrammatic_number(s))