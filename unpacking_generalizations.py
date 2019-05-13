print(*[1], *[2], 3, *[4, 5])

def fn(a, b, c, d):
	print(a, b, c, d)

fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})

print(*range(4), 4)

print([*range(4), 4])

print({*range(4), 4, *(5, 6, 7)})

print({'x': 1, **{'y': 2}})