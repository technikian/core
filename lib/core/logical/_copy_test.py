# includes
import random
import unittest
from . import _bitwise as bitwise


def random_bytearray(length):
	length = abs(length)
	target = bytearray()
	while length:
		target.append(random.randint(0, 255))
		length -= 1
	return target


def random_ascii(length):
	length = abs(length)
	target = ""
	while length:
		target += chr(random.randint(32, 126))
		length -= 1
	return target


types = (
	(bool,		lambda a, b: bool(random.randint(0, 1))),
	(int,		lambda a, b: random.randint(a, b)),
	(float,		lambda a, b: random.random() * (b - a) + a),
	(complex,	lambda a, b: complex(random.randint(a, b), random.randint(a, b))),
	(str,		lambda a, b: random_ascii(random.randint(a, b))),
	(tuple,		lambda a, b: tuple()),
	(list,		lambda a, b: list())
)


def random_object(a, b):
	select = random.randint(0, len(types) - 1)
	return types[select][1](a, b)


class BitwiseTest(unittest.TestCase):
	iterations = 100
	a = -10
	b = 10

	def test_shift(self):
		for i in range(self.iterations):
			source = random_object(self.a, self.b)
			shift = random_object(self.a, self.b)
			if isinstance(source, int) or isinstance(shift, int):
				continue
			self.assertRaises(TypeError, bitwise.left, source, shift)
			self.assertRaises(TypeError, bitwise.right, source, shift)
		self.assertEqual(bitwise.left(7567, 5), 242144)
		self.assertEqual(bitwise.left(7567, 0), 7567)
		self.assertEqual(bitwise.left(7567, -5), 236)
		self.assertEqual(bitwise.right(7567, -5), 242144)
		self.assertEqual(bitwise.right(7567, 0), 7567)
		self.assertEqual(bitwise.right(7567, 5), 236)

	def test_copy(self):
		for i in range(self.iterations):
			control = random_bytearray(8)
			src = bytearray(control)
			tgt = random_bytearray(4)

			src_bit = random.randint(0, 32)
			tgt_bit = random.randint(0, 64)
			bit_len = random.randint(0, 32)

			bitwise.copy(src, src_bit, tgt, tgt_bit, bit_len)
			bitwise.copy(tgt, tgt_bit, src, src_bit, bit_len)
			self.assertEqual(src, control)


if __name__ == "__main__":
	unittest.main()
