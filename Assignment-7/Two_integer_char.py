def add_two_non_negative_char(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        total = digit1 + digit2 + carry
        current_digit = total % 10
        carry = total // 10
        result.append(str(current_digit))
        i -= 1
        j -= 1

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])

print(add_two_non_negative_char('124', '56'))
