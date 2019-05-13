def g(x):
	yield from range(x, 0, -1)
	yield from range(x)

result = g(8)

def accumulate():
	tally = 0
	print(tally)
	while 1:
		next = yield
		if next is None:
			return tally
		tally += next

def gather_tallies(tallies):
	while 1:
		tally = yield from accumulate()
		tallies.append(tally)

tallies = []
acc = gather_tallies(tallies)
next(acc)

for i in range(4):
	acc.send(i)