
def eq(*args):
	"""behavior for 0 or 1 arg not defined"""
	ix = iter(args)
	try:
		a = next(ix)
	except StopIteration:
		return True
	for b in ix:
		if b != a:
			return False
	return True


def accumulate(iterable, operator, default=None):
	"""repeatedly call function with args last_result, item. first call args is item[0], item[1]"""
	from inspect import signature as sig
	if len(sig(operator).parameters) != 2:
		raise TypeError("! operator function should take two arguments")
	i = iter(iterable)
	try:
		r = next(i)
	except StopIteration:
		# raise ArithmeticError("! attempted arithmetic on 0 items")
		return default
	for v in i:
		r = operator(r, v)
	return r


#
# accumulate-based
#

# noinspection PyUnusedLocal
def add(*args):
	raise NotImplementedError("! inefficient: use 'sum(*args)'")


def sub(*args):
	def pair(a, b):
		return a - b
	return accumulate(pair, args)


def mul(*args):
	def pair(a, b):
		return a * b
	return accumulate(pair, args)


def div(*args):
	def pair(a, b):
		return a / b
	return accumulate(pair, args)


CMP_EXIT_EQ = 0
CMP_EXIT_EQ_PARTIAL = 1
CMP_EXIT_NE = 2


def cmp(*iterables):
	"""compares multiple iterables regardless of iterable type
	supports nested iterables
	behavior for 0 or 1 arg not defined"""

	# faster than standard version, no error checking
	def _eq(*values):
		ix = iter(values)
		a = next(ix)
		for b in ix:
			if b != a:
				return CMP_EXIT_NE
		return CMP_EXIT_EQ

	if len(iterables) < 2:
		return CMP_EXIT_EQ

	unique = object()
	iterators = tuple(iter(iterable) for iterable in iterables)
	while True:
		stops = 0
		first = unique
		tmp_iterators = iter(iterators)
		for iterator in tmp_iterators:
			try:
				first = next(iterator)
			except StopIteration:
				stops += 1
				continue
			if first is not unique:
				break
		if stops:
			return CMP_EXIT_EQ if stops == len(iterables) else CMP_EXIT_EQ_PARTIAL
		remaining = tuple(next(iterator) for iterator in tmp_iterators)
		if hasattr(first, "__iter__"):
			r = cmp(first, *remaining)
		else:
			r = _eq(first, *remaining)
		if r != CMP_EXIT_EQ:
			return r


# noinspection PyUnusedLocal
def average(values):
	"""this function is so simple, there's no reason for it to be a function, therefore"""
	raise NotImplementedError("! inefficient: use 'return sum(values) / len(values)'")


def variance(values, explicit_avg=None):
	"""variance"""
	avg = sum(values) / len(values) if explicit_avg is None else explicit_avg
	return sum(map(lambda x: (x - avg) ** 2, values)) / len(values)


def stddev(values, explicit_avg=None):
	"""standard deviation"""
	from math import sqrt
	return sqrt(variance(values, explicit_avg=explicit_avg))
