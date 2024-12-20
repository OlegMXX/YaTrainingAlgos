"Наиболее часто встречающийся символ в строке"

s = 'ababaccalllldfjojowerwwwwwwwwwwwweedfdflllsfh'
# ans = ''
# anscnt = 0
#
# for i in set(s):
#     count = 0
#     for j in range(len(s)):
#         if i == s[j]:
#             count += 1
#     if count > anscnt:
#         ans = i
#         anscnt = count
#
# print(ans, anscnt)


ans = ''
anscnt = 0

dct = {}
for i in s:
    if i not in dct:
        dct[i] = 0
    dct[i] += 1

for key in dct:
    if dct[key] > anscnt:
        anscnt = dct[key]
        ans = key

print(ans, anscnt)
