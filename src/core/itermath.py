from core import itermath

if __name__ == "__main__":
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	c = [1, 2, 3, 4, 5, 6, 7, 8, 8]
	d = [1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2]]
	e = [1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 3]]
	f = [1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 2]]
	g = (1, 2, 3, 4, 5, 6, 7, 8, 9)
	h = (1, 2, 3, 4, 5, 6, 7, 8, 9, (1, 2))
	print(itermath.cmp(a, a, a, a))  # true
	print(itermath.cmp(a, a, a, b))  # false
	print(itermath.cmp(a, a, a, c))  # false
	print(itermath.cmp(a, a, a, g))  # true
	print(itermath.cmp(d, d, d, d))  # true
	print(itermath.cmp(d, d, d, e))  # false
	print(itermath.cmp(d, d, d, f))  # false
	print(itermath.cmp(d, d, d, h))  # true
