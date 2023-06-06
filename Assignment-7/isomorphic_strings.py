def isomorphic_string(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            if s_dict[s[i]] != t[i]:
                return False
        else:
            s_dict[s[i]] = t[i]
        if t[i] in t_dict:
            if t_dict[t[i]] != s[i]:
                return False
        else:
            t_dict[t[i]] = s[i]
    # print(s_dict, t_dict)
    return True
s = "egg"
t = "add"
print(isomorphic_string(s, t))