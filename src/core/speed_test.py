from time import perf_counter
from core.itermath import average
from core import Task


class PerfTest:
	def __init__(self, task, count=1):
		self.task = task
		self.count = count
		self.result = None

	def __lt__(self, other):
		if self.result < other.result:
			return True
		return False

	def __eq__(self, other):
		if self.task == other.task and self.count == other.count and self.result == other.result:
			return True
		return False

	def test(self):
		time_deltas = []
		for i in range(self.count):
			a = perf_counter()
			self.task.exec()
			b = perf_counter()
			time_deltas.append(b - a)
		r = sum(time_deltas) / len(time_deltas)
		self.result = r
		return r


def test_a(count):
	return tuple(i for i in range(count) if i >= 2)


def test_b(count):
	return tuple(i for i in range(count) if i & (-1 ^ 1))


def test_c(count):
	return tuple(i for i in range(count) if i & -2)


if __name__ == "__main__":
	functions = (test_a, test_b, test_c)
	tests = tuple(PerfTest(Task(f, 10000)) for f in functions)
	results = tuple(test.test() for test in tests)
	print(results)

	# the test finds test_a to be the fastest
