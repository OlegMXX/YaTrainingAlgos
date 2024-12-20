"""Сортировка подсчетом"""

seq = [5,2,1,4,5,2,2,2,1,1,5]

def countsort(seq):
    minval = min(seq)
    maxval = max(seq)
    k = (maxval - minval) + 1
    count = [0] * k
    print(count)
    for now in seq:
        count[now - minval] += 1
    print(count)
    nowpos = 0
    for val in range(0, k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1
            print(seq)
    return seq

print(countsort(seq))