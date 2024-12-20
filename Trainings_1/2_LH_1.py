"""Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).

Выведите YES, если массив монотонно возрастает и NO в противном случае."""


def is_growing_seq():
    seq = list(map(int, input().split(" ")))

    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return "NO"
    return "YES"


print(is_growing_seq())