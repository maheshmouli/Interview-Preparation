def backspace_two_string(s, t):
    s_stack = []
    t_stack = []
    for i in s:
        if i == '#':
            if s_stack:
                s_stack.pop()
        else:
            s_stack.append(i)
    for i in t:
        if i == '#':
            if t_stack:
                t_stack.pop()
        else:
            t_stack.append(i)
    # print(s_stack, t_stack)
    if s_stack == t_stack:
        return True
    else:
        return False

s = "ab#c"
t = "ad#c"
print(backspace_two_string(s, t))