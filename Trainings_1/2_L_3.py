"""
Найти максимум в последовательности, если она гарантировавнно не пустая.
"""
import random
seq = [random.randint(1, 100) for _ in range(10)]
print(seq)

ind = 0
for i in range(1, len(seq)):
    if seq[i] > seq[ind]:
        ind = i

print(ind, seq[ind])
