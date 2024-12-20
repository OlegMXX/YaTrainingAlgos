"""
RLE
"AAANNNMMMMSSSLLWWWKJHHH" -> "A3N3M4S3L2W3KJH3"
Если строка пустая, вернуть -1
"""


input_str = "AAANNNMMMMSSSLLWWWKJHHHL"


def get_shorter(input_str):
    if len(input_str) == 0:
        return -1
    last_sym = input_str[0]
    last_sym_pos = 0
    res = []
    for i in range(len(input_str)):
        if last_sym != input_str[i]:
            res.append(last_sym)
            res.append(str(i - last_sym_pos) if i-last_sym_pos > 1 else '')
            last_sym = input_str[i]
            last_sym_pos = i
    res.append(last_sym)
    res.append(str(i - last_sym_pos) if i - last_sym_pos > 1 else '')

    return ''.join(res)


print(get_shorter(input_str))
