"""
Дана последовательность положительных чисел N и число X. найти все пары неодинаковых чисел A, B, чтобы их сумма
равнялась X
"""

seq = [2,3,4,5,6,7,8,9,10,11,1]
num = 12


def get_pairs(seq, num):
    seq_set = set()
    ans = []
    for i in seq:
        if num - i in seq_set:
            ans.append([i, num - i])
        else:
            seq_set.add(i)
    if len(seq_set) != 0:
        return ans
    else:
        return "0 0"

print(get_pairs(seq, num))