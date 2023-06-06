def each_char_reversing(s):
    # Input: "Hello, World!"    
    # Output: "olleH, dlroW!"
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] != ' ':
            j += 1
        result.append(s[i:j][::-1])
        i = j + 1  
    return ' '.join(result)

s = "Let's take LeetCode contest"
print(each_char_reversing(s))