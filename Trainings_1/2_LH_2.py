"""По последовательности чисел во входных данных определите ее вид:

CONSTANT – последовательность состоит из одинаковых значений
ASCENDING – последовательность является строго возрастающей
WEAKLY ASCENDING – последовательность является нестрого возрастающей
DESCENDING – последовательность является строго убывающей
WEAKLY DESCENDING – последовательность является нестрого убывающей
RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

Формат ввода
По одному на строке поступают числа последовательности ai, |ai| ≤ 109.

Признаком окончания последовательности является число -2× 109. Оно в последовательность не входит.
"""


def get_num_list():
    num_list = []
    while True:
        now_val = int(input())
        if now_val == -2000000000:
            break
        else:
            num_list.append(now_val)
            #print(num_list)
    return num_list

def analyse_sequence(num_list):
    seq = num_list

    my_set = set(seq)
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            my_set.add("l")
        elif num_list[i] < num_list[i+1]:
            my_set.add("g")
        else:
            my_set.add("e")
    if "l" in my_set:
        if "g" in my_set:
            return "RANDOM"
        elif "e" in my_set:
            return "WEAKLY DESCENDING"
        else:
            return "DESCENDING"
    elif "g" in my_set:
        if "e" in my_set:
            return "WEAKLY ASCENDING"
        else:
            return "ASCENDING"
    else:
        return "CONSTANT"

print(analyse_sequence(get_num_list()))
