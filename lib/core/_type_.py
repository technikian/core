
class Index:
	def __init__(self, value, step=1):
		self.value = value
		self.step = step

	def __str__(self):
		return str(self.value)

	def __iter__(self):
		return self

	def __next__(self):
		self.value += self.step
		return self.value


class Task:
	def __init__(self, function, *args, **kwargs):
		self.function = function
		self.args = args
		self.kwargs = kwargs
		self.result = None

	def __repr__(self):
		return f"Task({self.function}, *{self.args}, **{self.kwargs})"

	def __hash__(self):
		return hash((self.function, self.args, tuple(self.kwargs), self.kwargs.values(), self.result))

	def __call__(self):
		r = self.function(*self.args, **self.kwargs)
		self.result = r
		return r

	def exec(self):
		r = self.function(*self.args, **self.kwargs)
		self.result = r
		return r
