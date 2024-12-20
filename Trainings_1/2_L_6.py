"""Вывести самые короткие слова"""
import sys

seq = ["fghj", "er", "fghj", "dfghjkl", "hj", "ghj", "hjk", "asdfghjkl"]

def get_min_length(words):
    shortest_len = len(words[0])
    for i in range(1, len(words)):
        if len(words[i]) < shortest_len:
            shortest_len = len(words[i])
    return shortest_len


def get_shortest_words(words):
    ans = []
    min_len = get_min_length(words)
    for i in range(len(words)):
        if len(words[i]) == min_len:
            ans.append(words[i])
    return ans


print(get_min_length(seq))
print(get_shortest_words(seq))