
class ContextManaged:
	def __enter__(self):
		e = self.open()
		if e:
			raise e
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		e = self.close()
		if e:
			raise e

	def open(self):
		raise NotImplementedError

	def close(self):
		raise NotImplementedError
