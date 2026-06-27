d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = d1.copy()

for value in d2:
    if value in result:
        result[value] = result[value] + d2[value]
    else:
        result[value] = d2[value]

print(result)