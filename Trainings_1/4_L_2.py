"""
Дано два числа X и Y без ведущих нулей

Надо проверить, можн ли получить первое из второго перестановкой цифр
"""


def make_list(num):
    num_list = []
    while num > 0:
        num_list.append(num % 10)
        num //= 10
    return num_list


def make_dict(num_list):
    num_dict = {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict


def compare_nums(x, y):
    if x == y:
        return True
    else:
        return make_dict(make_list(x)) == make_dict(make_list(y))


x = 2021
y = 1202


print(compare_nums(x, y))
