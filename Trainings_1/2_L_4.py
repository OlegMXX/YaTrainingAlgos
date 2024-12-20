"""
Найти максимум в последовательности длинной больше 1, и второй максимум.
"""
import random
seq: list[int] = [random.randint(1, 100) for _ in range(10)]
# seq[0] = 100
print(seq)

first_max: int = 0
sec_max: int
start_from: int = 0

for i in range(1, len(seq)):
    if seq[i] > seq[first_max]:
        first_max, sec_max = i, first_max
        start_from = i
        break
    if seq[i] < seq[first_max]:
        sec_max = i
        start_from = i
        break
    if seq[i] == seq[first_max]:
        continue

print(seq[first_max], seq[sec_max])

for i in range(start_from + 1, len(seq)):
    if seq[i] > seq[first_max]:
        first_max, sec_max = i, first_max
    elif seq[sec_max] < seq[i]:
        sec_max = i

print(seq[first_max], seq[sec_max])