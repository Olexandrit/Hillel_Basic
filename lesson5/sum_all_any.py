scores = [3, 15, 7, 29, 10, 16]
total = 0

for score in scores:
    total += score

print(total)

total = sum(scores)
print(total)

word = 'cucumber'
checks = [type(word) is str, 'c' in word, word.startswith('cuc'), word.isalpha(), 'a' in word]
print(all(checks))
print(any(checks))

bools = (True, True, True)
print(all(bools))