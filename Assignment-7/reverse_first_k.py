def reverse_first_k_characters(s, k):
    if len(s)<k:
        return s[::-1]
    elif len(s)>=k:
        return s[:k][::-1]+s[k:]
    
s = "abcdefg"
k = 2
print(reverse_first_k_characters(s, k))